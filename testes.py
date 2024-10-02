import random
import json
import pandas as pd
from model import Data, Disciplina, Professor, Sala, Turma
from utils import load_data, ler_XML, criar_grade, display_grade, calcular_tamanho_bloco
from utils import carrega_dispo_prof, carrega_salas, carrega_prof, carrega_turmas, carregar_dados
from costs import pontuacao_individuo, pontuacao_professores, pontuacao_salas

# Parâmetros
POPULACAO_TAMANHO = 50
GERACOES = 1
TAXA_MUTACAO = 0.5
# Definição de horários por turno
TURNOS_HORARIOS = {
    "Manhã":    range(1, 7),        # Manhã
    "Tarde":    range(7, 13),       # Tarde
    "Noite":    range(14, 20),      # Noite
    "Integral": range(0, 13),        # Integral
    "nan": range(0, 20)
}


def inicializar_populacao(turmas: dict, professores: dict, salas: dict) -> list[dict]:
    """Função de inicialização da população usando o algoritmo 'best fit'.

    Args:
        turmas (dict): Dicionário que contém os objetos de Turma.
        professores (dict): Dicionário que contém os objetos de Professor.
        salas (dict): Dicionário que contém os objetos de Salas.

    Returns:
        list[dict]: Lista com dicionários de Individuos (Turmas) e Grade Professores.
    """
    populacao = []

    for _ in range(POPULACAO_TAMANHO):
        individuo = {}
        grade_professores = {}

        # Criar grade vazia para cada professor
        for nome_professor in professores:
            grade_professores[nome_professor] = criar_grade()

        for turma_id, turma in turmas.items():
            grade = criar_grade()
            horarios_possiveis = list(TURNOS_HORARIOS[turma.turno])

            # Separar disciplinas por carga horária (maior carga primeiro)
            disciplinas_prioritarias = [d for d in turma.disciplinas if int(d.carga_horaria) == 6]
            disciplinas_normais = [d for d in turma.disciplinas if int(d.carga_horaria) != 6]
            disciplinas = disciplinas_prioritarias + disciplinas_normais

            # Para cada Disciplina da Turma
            for disciplina in disciplinas:
                horarios_alocados = 0
                carga_horaria = int(disciplina.carga_horaria)

                # Tentativa de encontrar o melhor bloco contínuo
                while horarios_alocados < carga_horaria:
                    melhor_bloco = None
                    melhor_dia = None
                    melhor_horario_inicio = None
                    melhor_bloco_livre = False

                    for dia in range(5):  # Segunda a Sexta
                        for horario_inicio in horarios_possiveis:
                            # Verificar quantos blocos consecutivos estão livres
                            blocos_disponiveis = sum(
                                1 for i in range(carga_horaria)
                                if horario_inicio + i in horarios_possiveis and grade[horario_inicio + i][dia] is None
                            )
                            if blocos_disponiveis >= carga_horaria:
                                # Verificar disponibilidade dos professores no mesmo horário
                                professores_disponiveis = all(
                                    all(grade_professores[professor][horario_inicio + i][dia] is None
                                        for i in range(carga_horaria))
                                    for professor in disciplina.professores
                                )

                                if professores_disponiveis:
                                    melhor_bloco = blocos_disponiveis
                                    melhor_dia = dia
                                    melhor_horario_inicio = horario_inicio
                                    melhor_bloco_livre = True
                                    break  # Encontrou o melhor bloco possível

                    if melhor_bloco_livre:
                        # Alocar o bloco na disciplina e nos professores
                        for i in range(carga_horaria):
                            grade[melhor_horario_inicio + i][melhor_dia] = disciplina
                            for professor in disciplina.professores:
                                nome_professor = professores[professor].nome
                                grade_professores[nome_professor][melhor_horario_inicio + i][melhor_dia] = disciplina

                        horarios_alocados += carga_horaria
                    else:
                        # Não conseguiu alocar, continuar tentando
                        break

            individuo[turma_id] = grade

        populacao.append({'Individuo': individuo, 'Grade Professor': grade_professores})

    return populacao


def avaliar_aptidao(populacao: dict, professores: dict, salas: dict, horarios: dict) -> float:
    """Função com o objetivo de avaliar a aptidão da população atráves de diversas restrições impostas ao conjunto

    Args:
        populacao (dict): Dicionário que contem as grades tanto para individuos (Turmas) quanto para Professores
        professores (dict): Dicionário que contem os objetos de professores
        salas (dict): Dicionário que contem os objetos de salas

    Returns:
        float: Pontuação total obtida ao longo das restrições
    """

    individuo = populacao.get('Individuo')
    grade_professores = populacao.get('Grade Professor')
    score = 0.0

    score += pontuacao_individuo(individuo)
    score += pontuacao_professores(grade_professores, professores, horarios)

    return score


def selecao(populacao: list[dict], fitness_scores: list) -> list:
    """Função que faz a seleção de individuos pelo metodo de torneio, selecionando 3 individuos

    Args:
        populacao (list[dict]): list de dicionário com os individuos
        fitness_scores (list): Pontuação por individuo

    Returns:
        list: Retorna a lista de individuos selecionados
    """
    selected = []
    torneio_tamanho = 5
    for _ in range(POPULACAO_TAMANHO):
        torneio = random.sample(
            list(zip(populacao, fitness_scores)), torneio_tamanho)
        vencedor = max(torneio, key=lambda x: x[1])
        selected.append(vencedor[0])
    return selected


def cruzamento(parents: list) -> list[dict]:
    """
    Função com o objetivo de mesclar as "caracteristicas" dos pais para assim gerar uma grade completamente nova

    Args:
        parents (list): List de individuos dos quais serão extraidos os dados

    Returns:
        list[dict]: retorna uma lista de dicionário {"Individuo": child, "Grade Professor": grade_professores_child}
    """
    offspring = []
    for _ in range(len(parents) // 2):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        child = {}
        grade_professores_child = {}

        # Inicializa a grade de professores do filho
        for professor in parent1['Grade Professor']:
            grade_professores_child[professor] = [row[:] for row in parent1['Grade Professor'][professor]]

        # Para cada turma, processamos as disciplinas em blocos/dias
        for turma_id in parent1['Individuo']:
            turma_parent1 = parent1['Individuo'][turma_id]
            turma_parent2 = parent2['Individuo'][turma_id]

            # Inicializar a grade da turma no filho
            child[turma_id] = [[None for _ in range(len(turma_parent1[0]))] for _ in range(len(turma_parent1))]

            # Escolha de qual pai herdar por dia
            for horario in range(len(turma_parent1)):
                if random.random() > 0.5:
                    # Herdar o dia inteiro do parent1
                    for dia in range(len(turma_parent1[horario])):
                        child[turma_id][horario][dia] = turma_parent1[horario][dia]
                        if turma_parent1[horario][dia]:
                            for professor in turma_parent1[horario][dia].professores:
                                grade_professores_child[professor][horario][dia] = turma_parent1[horario][dia]
                else:
                    # Herdar o dia inteiro do parent2
                    for dia in range(len(turma_parent2[horario])):
                        child[turma_id][horario][dia] = turma_parent2[horario][dia]
                        if turma_parent2[horario][dia]:
                            for professor in turma_parent2[horario][dia].professores:
                                grade_professores_child[professor][horario][dia] = turma_parent2[horario][dia]

        offspring.append({
            'Individuo': child,
            'Grade Professor': grade_professores_child
        })

    return offspring


def mutacao(offspring: list[dict], turmas: dict) -> list[dict]:
    """
    Função que de forma aleatória dependendo da TAXA_MUTACAO transforma a grade do individuo

    Args:
        offspring (list[dict]): Lista de Individuos após o cruzamento entre os pais
        turmas (dict): Dicionário de Objetos de Turma para suporte

    Returns:
        list[dict]: Retorno a população mutacionada
    """
    for populacao in offspring:
        individuo = populacao.get('Individuo')
        grade_professores = populacao.get('Grade Professor')

        # Para cada turma na população
        for turma_id, grade in individuo.items():
            # Caso o valor seja selecionado para mutação
            if random.random() < TAXA_MUTACAO:
                turma = turmas[turma_id]
                horarios_possiveis = list(TURNOS_HORARIOS[turma.turno])

                # Verificando o maior espaço vazio na grade
                maior_espaco, dia_espaco = verificar_maior_espaco(grade, horarios_possiveis)

                # Se tiver um espaço
                if len(maior_espaco) > 1:
                    # Escolher uma disciplina na grade
                    disciplina: Disciplina = random.choice(turma.disciplinas)
                    print(disciplina)

                    for i, horario in enumerate(grade):
                            if disciplina in horario:
                                print(disciplina)
                else:
                    pass

                individuo[turma_id] = grade
            # Se não entrar na mutação passa
            else:
                pass
            
    return offspring

def verificar_maior_espaco(grade: list, horarios_possiveis: list) -> list:
    # Verificar maior espaço vago
    maior_espaco = []
    dia_escolhido = 0
    for dia in range(5):
        espaco_atual = []
        espacos = []
        for horario in horarios_possiveis:
            if grade[horario][dia] is None:
                espaco_atual.append(horario)
            else:
                if espaco_atual:
                    espacos.append(espaco_atual)  # Adiciona o espaço atual à lista de espaços
                    espaco_atual = []  # Reseta o espaço atual
        if espaco_atual:
            espacos.append(espaco_atual)  # Adiciona o último bloco de horários vagos, se existir

        # Encontra o maior bloco de horários vagos
        for espaco in espacos:
            if len(espaco) > len(maior_espaco):
                maior_espaco = espaco
                dia_escolhido = dia

    return maior_espaco, dia_escolhido


def algoritmo_genetico(turmas: dict[str, Turma], professores: dict[str, Professor], salas: dict[str, Sala], horarios: dict):
    """
    Função do algoritmo genético que atráves dos dados de entrada encontrada o melhor caso com base nas restrições

    Args:
        turmas (dict[str, Turma]): Dicionário com Objetos de Turmas
        professores (dict[str, Professor]): Dicionário com Objetos de Professores
        salas (dict[str, Sala]): Dicionário com Objetos de Salas

    Returns:
        dict[str, Turma]: Dicionário composto pela melhor população encontrada
        dict[str, Professor]: Dicionário composto pela grade horaria dos professores para a melhor população encontrada
    """

    # Inicializa a população com possíveis soluções iniciais (cromossomos)
    populacao = inicializar_populacao(turmas, professores, salas)

    # Define o número de gerações para a execução do algoritmo
    for geracao in range(GERACOES):
        # Avalia a aptidão de cada indivíduo na população
        fitness_scores = [avaliar_aptidao(individuo, professores, salas, horarios) for individuo in populacao]

        # Seleciona os pais para a próxima geração com base nas pontuações de aptidão
        parents = selecao(populacao, fitness_scores)

        # Gera descendentes através do cruzamento dos pais selecionados
        offspring = cruzamento(parents)

        # Aplica mutação nos descendentes para introduzir variabilidade
        offspring = mutacao(offspring, turmas)

        # Atualiza a população combinando pais e descendentes
        populacao = parents + offspring

        # A cada 10 gerações, imprime a melhor aptidão encontrada até o momento
        if geracao % 10 == 0:
            print(f'Geração {geracao}, melhor aptidão: {max(fitness_scores)}')

    # Após todas as gerações, seleciona o melhor indivíduo da população final
    melhor_alvo = max(populacao, key=lambda individuo: avaliar_aptidao(individuo, professores, salas, horarios))
    melhor_individuo = melhor_alvo.get('Individuo')
    grade_professores = melhor_alvo.get('Grade Professor')

    # Retorna o melhor indivíduo encontrado como solução
    return melhor_individuo, grade_professores


def carrega_arquivos(dispo_profes: str, salas: str, turmas: str, prof: str, semestre_atual: str):
    with open('./input/Data/horarios.json', 'r') as f:
        horarios = json.load(f)

    df_dispo_profes = carrega_dispo_prof(dispo_profes)
    df_salas = carrega_salas(salas)
    df_turmas = carrega_turmas(turmas)
    df_prof = carrega_prof(prof)

    semestre_atual = "2024/2"

    data = carregar_dados(df_prof, df_salas, df_turmas, df_dispo_profes, semestre_atual)
    return data, horarios


def main(data, horarios):
    melhor_individuo, grade_professores = algoritmo_genetico(data.turmas, data.professores, data.salas, horarios)

    # TESTES
    prof = grade_professores.get("ANDREY CABRAL MEIRA")
    teste1 = melhor_individuo.get("CCCO - 2.0A - M - 2024/2")
    teste2 = melhor_individuo.get("CCCO - 2.0B - M - 2024/2")
    teste3 = melhor_individuo.get("CCCO - 3.0U - M - 2024/2")
    teste4 = melhor_individuo.get("CCCO - 1.0U - M - 2024/2")
    teste5 = melhor_individuo.get("CESF - 1.0U - M - 2024/2")

    display_grade(teste1, horarios)
    display_grade(teste2, horarios)
    display_grade(teste3, horarios)
    display_grade(teste4, horarios)
    display_grade(teste5, horarios)

    display_grade(prof, horarios)

    return melhor_individuo, grade_professores

    # for turma_id, grade in melhor_individuo.items():
    #     print(f"Turma: {turma_id}")
    #     display_grade(grade, horarios)
    #     print(data.turmas[turma_id].disciplinas)


if __name__ == "__main__":
    arquivo_dispo_prof = "../data/magister_asctimetables_2024-04-22-15-12-35_curitiba.xml"
    arquivo_salas = "../Data/Relatorio_dos_Espacos_de_Ensino 1.xlsx"
    arquivo_turmas = "../Data/politecnica/"
    arquivo_prof = "../Data/Planilha_Geral_Professores.xlsm"

    data, horarios = carrega_arquivos(arquivo_dispo_prof, arquivo_salas, arquivo_turmas, arquivo_prof, "2024/2")
    main(data, horarios)
