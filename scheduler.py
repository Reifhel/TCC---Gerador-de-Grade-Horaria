import random
import json
import pandas as pd
from model import Data, Disciplina, Professor, Sala, Turma
from utils import load_data, ler_XML, criar_grade, display_grade, calcular_tamanho_bloco, cria_excel
from utils import carrega_dispo_prof, carrega_salas, carrega_prof, carrega_turmas, carregar_dados
from costs import pontuacao_individuo, pontuacao_professores, pontuacao_salas

# Parâmetros
POPULACAO_TAMANHO = 50
GERACOES = 2
TAXA_MUTACAO = 0.7
# Definição de horários por turno
TURNOS_HORARIOS = {
    "Manhã":    range(1, 7),        # Manhã
    "Tarde":    range(7, 13),       # Tarde
    "Noite":    range(14, 20),      # Noite
    "Integral": range(0, 13),        # Integral
    "nan": range(0, 20)
}

# De -> Para Escolas
ESCOLAS = {
    1: "Bloco 01",
    2: "Bloco 02",
    3: "Bloco 03",
    4: "Bloco 04",
    5: "Bloco 05",
    6: "Bloco 06"
}


def inicializar_populacao(turmas: dict, professores: dict, salas: dict) -> list[dict]:
    """Função de inicialização da população usando o algoritmo 'best fit' com alocação de disciplinas divididas.

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

                # Tentar alocar em blocos menores se necessário
                while horarios_alocados < carga_horaria:
                    melhor_dia = None
                    melhor_horario_inicio = None
                    melhor_bloco = 0

                    for dia in range(5):  # Segunda a Sexta
                        for horario_inicio in horarios_possiveis:
                            # Verificar se o horário de início está dentro dos limites da grade
                            if horario_inicio >= len(grade):
                                continue

                            # Procurar blocos de 2, 4 ou 6 horários livres
                            for bloco_tamanho in [6, 4, 2]:
                                if horarios_alocados + bloco_tamanho > carga_horaria:
                                    bloco_tamanho = carga_horaria - horarios_alocados

                                if bloco_tamanho == 0:
                                    continue

                                # Garantir que todos os horários do bloco estão dentro dos limites da grade
                                if horario_inicio + bloco_tamanho > len(grade):
                                    continue

                                # Verificar se há blocos livres na grade da turma
                                bloco_livre = all(
                                    (grade[horario_inicio + i][dia] is None)
                                    and
                                    (horario_inicio + i in horarios_possiveis)
                                    for i in range(bloco_tamanho)
                                )

                                # Verificar se os professores estão disponíveis
                                professores_disponiveis = all(
                                    all(
                                        (grade_professores[professor][horario_inicio + i][dia] is None)
                                        and
                                        (horario_inicio + i in horarios_possiveis)
                                        for i in range(bloco_tamanho)
                                    )
                                    for professor in disciplina.professores
                                )

                                if bloco_livre and professores_disponiveis:
                                    melhor_dia = dia
                                    melhor_horario_inicio = horario_inicio
                                    melhor_bloco = bloco_tamanho
                                    break  # Encontrou o melhor ajuste

                    if melhor_bloco > 0:
                        # Alocar o bloco na disciplina e nos professores
                        for i in range(melhor_bloco):
                            if melhor_horario_inicio + i < len(grade) and melhor_dia < len(grade[0]):
                                grade[melhor_horario_inicio + i][melhor_dia] = disciplina
                                for professor in disciplina.professores:
                                    grade_professores[professor][melhor_horario_inicio + i][melhor_dia] = disciplina

                        horarios_alocados += melhor_bloco
                    else:
                        # Se não encontrar mais blocos, parar a tentativa de alocação dessa disciplina
                        break

            individuo[turma_id] = grade

        populacao.append({'Individuo': individuo, 'Grade Professor': grade_professores})

    return populacao


def avaliar_aptidao_nsga(populacao: dict, professores: dict, salas: dict, horarios: dict) -> list:
    """Avalia aptidão multiobjetivo."""
    individuo = populacao.get('Individuo')
    grade_professores = populacao.get('Grade Professor')

    # Objetivo 1: minimizar conflitos de horários de professores
    objetivo_1 = pontuacao_professores(grade_professores, professores, horarios)

    # Objetivo 2: minimizar janelas (gaps) para os alunos
    objetivo_2 = pontuacao_individuo(individuo)

    return [objetivo_1, objetivo_2]  # Retorna uma lista com os valores de cada objetivo


def calcular_fronteira_pareto(populacao, aptidoes):
    """Classifica a população com base na fronteira de Pareto."""
    fronteiras = []
    dominado_por = [0] * len(populacao)
    domina_outros = [[] for _ in range(len(populacao))]

    for i in range(len(populacao)):
        for j in range(len(populacao)):
            if i != j:
                if domina(aptidoes[i], aptidoes[j]):
                    domina_outros[i].append(j)
                elif domina(aptidoes[j], aptidoes[i]):
                    dominado_por[i] += 1

        if dominado_por[i] == 0:
            fronteiras.append(i)

    return fronteiras


def domina(objetivos1, objetivos2):
    """Verifica se uma solução domina a outra."""
    return all(x <= y for x, y in zip(objetivos1, objetivos2)) and any(x < y for x, y in zip(objetivos1, objetivos2))


def calcular_distancia_crowding(populacao, aptidoes):
    """Calcula a distância de crowding."""
    distancias = [0] * len(populacao)

    for m in range(len(aptidoes[0])):  # Para cada objetivo
        sorted_populacao = sorted(range(len(aptidoes)), key=lambda i: aptidoes[i][m])
        distancias[sorted_populacao[0]] = float('inf')
        distancias[sorted_populacao[-1]] = float('inf')

        min_val = aptidoes[sorted_populacao[0]][m]
        max_val = aptidoes[sorted_populacao[-1]][m]

        if max_val - min_val == 0:
            continue

        for i in range(1, len(populacao) - 1):
            distancias[sorted_populacao[i]] += (aptidoes[sorted_populacao[i + 1]][m] - aptidoes[sorted_populacao[i - 1]][m]) / (max_val - min_val)

    return distancias


def selecao_nsga(populacao, aptidoes):
    """Seleciona indivíduos com base no NSGA-II."""
    fronteira_pareto = calcular_fronteira_pareto(populacao, aptidoes)
    crowding_distances = calcular_distancia_crowding(populacao, aptidoes)

    # Classificar pela fronteira e pela distância de crowding,
    # priorizando maiores valores de aptidão
    populacao_classificada = sorted(zip(populacao, aptidoes, crowding_distances), key=lambda x: (x[1], x[2]), reverse=True)

    # Selecionar os melhores
    selecionados = [individuo for individuo, _, _ in populacao_classificada[:POPULACAO_TAMANHO]]

    return selecionados


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
            grade = parent1['Grade Professor'][professor]
            grade_professores_child[professor] = [[None for _ in range(len(grade[0]))] for _ in range(len(grade))]

        # Para cada turma, processamos as disciplinas em blocos/dias
        for turma_id in parent1['Individuo']:
            turma_parent1 = parent1['Individuo'][turma_id]
            turma_parent2 = parent2['Individuo'][turma_id]

            # Inicializar a grade da turma no filho
            child[turma_id] = [[None for _ in range(len(turma_parent1[0]))] for _ in range(len(turma_parent1))]

            # Escolha de qual pai herdar por dia
            if random.random() > 0.5:
                for dia in range(5):
                    # Herdar o dia inteiro do parent1
                    for horario in range(len(turma_parent1)):
                        child[turma_id][horario][dia] = turma_parent1[horario][dia]
            else:
                # Herdar o dia inteiro do parent2
                for dia in range(5):
                    # Herdar o dia inteiro do parent2
                    for horario in range(len(turma_parent2)):
                        child[turma_id][horario][dia] = turma_parent2[horario][dia]

        for turma_id, grade in child.items():
            turma = child[turma_id]
            for dia in range(5):
                # Herdar o dia inteiro do parent2
                for horario in range(len(grade)):
                    if turma[horario][dia]:
                        for professor in turma[horario][dia].professores:
                            grade_professores_child[professor][horario][dia] = turma[horario][dia]

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

                # Se tiver um espaço para 4 aulas ou mais
                if len(maior_espaco) > 3:
                    # Escolher uma disciplina na grade
                    disciplina: Disciplina = random.choice(turma.disciplinas)
                    carga_horaria = disciplina.carga_horaria

                    # Pegando o espaço da Disciplina
                    espaço_disc = []
                    dia_disc = []
                    for dia in range(5):
                        horas = []
                        for horario in horarios_possiveis:
                            if disciplina == grade[horario][dia]:
                                horas.append(horario)
                        if horas:
                            espaço_disc = horas
                            dia_disc = dia

                    # Trocar os blocos
                    qtd_a_trocar = int(min(carga_horaria, len(maior_espaco), len(espaço_disc)))

                    professor_disponivel = all(
                        all(grade_professores[professor][maior_espaco[i]][dia_espaco] is None
                            for i in range(qtd_a_trocar))
                        for professor in disciplina.professores
                    )

                    if professor_disponivel:
                        for i in range(qtd_a_trocar):
                            t = grade[espaço_disc[i]][dia_disc]
                            grade[espaço_disc[i]][dia_disc] = None
                            grade[maior_espaco[i]][dia_espaco] = t

                            for professor in disciplina.professores:
                                grade_professores[professor][espaço_disc[i]][dia_disc] = None
                                grade_professores[professor][maior_espaco[i]][dia_espaco] = t

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


def algoritmo_genetico_nsga(turmas, professores, salas, horarios):
    populacao = inicializar_populacao(turmas, professores, salas)

    for geracao in range(GERACOES):
        # Avaliar aptidões multiobjetivo
        aptidoes = [avaliar_aptidao_nsga(individuo, professores, salas, horarios) for individuo in populacao]

        # Seleção NSGA-II
        pais = selecao_nsga(populacao, aptidoes)

        # Cruzamento e mutação
        descendentes = cruzamento(pais)
        descendentes = mutacao(descendentes, turmas)

        # Combinar pais e filhos
        populacao = pais + descendentes

        # Imprimir melhores indivíduos periodicamente
        if geracao % 10 == 0:
            print(f'\nGeração {geracao}:')
            for i, fitness in enumerate(aptidoes):
                total_fitness = fitness[0]+fitness[1]
                print(f'[Gen {geracao}] Ind {i}: Aptidão [objetivo 1: {fitness[0]}, objetivo 2: {fitness[1]}] -> Total = {total_fitness}')

    # Seleciona o melhor da última população
    melhores_individuos = selecao_nsga(populacao, aptidoes)
    melhor_individuo = melhores_individuos[0]

    return melhor_individuo.get('Individuo'), melhor_individuo.get('Grade Professor')


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
    melhor_individuo, grade_professores = algoritmo_genetico_nsga(data.turmas, data.professores, data.salas, horarios)

    # TESTES
    prof = grade_professores.get("ANDREY CABRAL MEIRA")
    teste1 = melhor_individuo.get("CCCO - 2.0A - M - 2024/2")
    teste2 = melhor_individuo.get("CCCO - 2.0B - M - 2024/2")
    teste3 = melhor_individuo.get("CCCO - 3.0U - M - 2024/2")
    teste4 = melhor_individuo.get("CCCO - 1.0U - M - 2024/2")
    teste5 = melhor_individuo.get("CCCO - 4.0U - N - 2024/2")
    teste6 = melhor_individuo.get("CCCO - 2.0U - N - 2024/2")

    display_grade(teste1, horarios)
    display_grade(teste2, horarios)
    display_grade(teste3, horarios)
    display_grade(teste4, horarios)
    display_grade(teste5, horarios)
    display_grade(teste6, horarios)

    display_grade(prof, horarios)

    # for turma_id, grade in melhor_individuo.items():
    #     print(f"Turma: {turma_id}")
    #     display_grade(grade, horarios)
    #     print(data.turmas[turma_id].disciplinas)

    return melhor_individuo, grade_professores


if __name__ == "__main__":
    arquivo_dispo_prof = "../data/magister_asctimetables_2024-04-22-15-12-35_curitiba.xml"
    arquivo_salas = "../Data/Relatorio_dos_Espacos_de_Ensino 1.xlsx"
    arquivo_turmas = "../Data/politecnica/"
    arquivo_prof = "../Data/Planilha_Geral_Professores.xlsm"

    data, horarios = carrega_arquivos(arquivo_dispo_prof, arquivo_salas, arquivo_turmas, arquivo_prof, "2024/2")
    melhor_individuo, _ = main(data, horarios)

    cria_excel(horarios, melhor_individuo)
