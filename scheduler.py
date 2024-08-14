import random
import json
import pandas as pd
import glob
import os
from model import Data, Disciplina, Professor, Sala, Turma
from utils import loadData, lerXML, criarGrade, display_grade

# Parâmetros
POPULACAO_TAMANHO = 50
GERACOES = 100
TAXA_MUTACAO = 0.7
# Definição de horários por turno
TURNOS_HORARIOS = {
    "Manhã":    range(1, 7),        # Manhã
    "Tarde":    range(7, 13),       # Tarde
    "Noite":    range(14, 20),      # Noite 
    "Integral": range(0, 13),        # Integral
    "nan": range(0,20)
}

def calcular_tamanho_bloco(grade, horario_inicio, dia, disciplina):
    tamanho_bloco = 0
    while horario_inicio + tamanho_bloco < len(grade) and grade[horario_inicio + tamanho_bloco][dia] == disciplina:
        tamanho_bloco += 1
    return tamanho_bloco

def inicializar_populacao(turmas, professores, salas):
    populacao = []

    for _ in range(POPULACAO_TAMANHO):
        individuo = {}
        grade_professores = {}

        for professor in professores.items():
            nome_professor = professor[0]
            if nome_professor not in grade_professores:
                grade_professores[nome_professor] = criarGrade()

        for turma_id, turma in turmas.items():
            grade = criarGrade()
            horarios_possiveis = list(TURNOS_HORARIOS[turma.turno])
            
            # Separar disciplinas por carga horária
            disciplinas_prioritarias = [d for d in turma.disciplinas if int(d.cargaHoraria) == 6]
            disciplinas_normais = [d for d in turma.disciplinas if int(d.cargaHoraria) != 6]
            
            # Combinar disciplinas prioritárias primeiro
            disciplinas = disciplinas_prioritarias + disciplinas_normais

            # Para cada Disciplina da Turma
            for disciplina in disciplinas:
                horarios_alocados = 0
                carga_horaria = int(disciplina.cargaHoraria)
                tentativas = 0
                while horarios_alocados < carga_horaria and tentativas < 100:
                    dia = random.randint(0, 4)  # Seg a Sexta

                    primeiroHorarioDia = horarios_possiveis[0]

                    if(grade[primeiroHorarioDia][dia] == None):
                        horario_inicio = horarios_possiveis[0]
                    else:
                        horario_inicio = random.choice(horarios_possiveis)

                    max_bloco = 6 if carga_horaria == 6 else 0
                    if carga_horaria != 6:
                        for h in range(len(horarios_possiveis)):
                            if horarios_possiveis[h] in horarios_possiveis:
                                max_bloco += 1
                            else:
                                break
                    bloco = min(max_bloco, carga_horaria - horarios_alocados) 

                    # Ajustar bloco para respeitar o turno
                    if not all(horario_inicio + i in horarios_possiveis for i in range(bloco)):
                        tentativas += 1
                        continue

                    bloco_livre = all(grade[horario_inicio + i][dia] is None for i in range(bloco))

                    if bloco_livre:
                        # Verificando se os professores estão livres nesse horário também
                        professor_disponivel = all(
                            all(grade_professores[professor][horario_inicio + i][dia] is None 
                                for i in range(bloco))
                            for professor in disciplina.professores
                        )
                        
                        # caso esteja
                        if professor_disponivel:
                            # Aloca o bloco na disciplina
                            for i in range(bloco):
                                grade[horario_inicio + i][dia] = disciplina
                            horarios_alocados += bloco

                            #Alocar na grade do professor
                            for professor in disciplina.professores:
                                nome_professor = professores[professor].nome
                                for i in range(bloco):
                                    grade_professores[nome_professor][horario_inicio + i][dia] = disciplina

                    tentativas += 1
            individuo[turma_id] = grade
        populacao.append({'Individuo': individuo, 'Grade Professor': grade_professores})
    return populacao

def avaliar_aptidao(populacao, professores, salas):
    individuo = populacao.get('Individuo')
    score = 0
    for turma_id, grade in individuo.items():
        for dia in range(6):
            disciplinasDia = []
            for horario in range(20):
                disciplina = grade[horario][dia]

                # Mais de 2 disciplinas por dia
                if disciplina:
                    if disciplina.id not in disciplinasDia:
                        disciplinasDia.append(disciplina.id)

                if disciplina:
                    if len(disciplina.professores) > 0:
                        professor_id = disciplina.professores[0]
                        professor = professores[professor_id]
                        # Verificação de disponibilidade do professor
                        if professor.disponibilidade[horario][dia]:
                            score += .5
                        else:
                            score -= .5  # Penalidade por alocar professor em horário indisponível
                    # Verificação de capacidade da sala
                    sala = random.choice(list(salas.values()))
                    if int(sala.capacidade) >= int(disciplina.qtdEstudantes):
                        score += .5
                    else:
                        score -= .5  # Penalidade por usar sala com capacidade insuficiente

                # Mais de 2 disciplinas por dia
                if len(disciplinasDia) > 2:
                    score -= 1

            disciplinasDia = []
     
    return score

def selecao(populacao, fitness_scores):
    selected = []
    torneio_tamanho = 3
    for _ in range(POPULACAO_TAMANHO):
        torneio = random.sample(list(zip(populacao, fitness_scores)), torneio_tamanho)
        vencedor = max(torneio, key=lambda x: x[1])
        selected.append(vencedor[0])
    return selected

def cruzamento(parents):
    offspring = []
    for _ in range(len(parents) // 2):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        child = {}
        for turma_id in parent1:
            if random.random() > 0.5:
                child[turma_id] = parent1[turma_id]
            else:
                child[turma_id] = parent2[turma_id]
        offspring.append(child)
    return offspring

def mutacao(offspring, turmas):
    for populacao in offspring:
        individuo = populacao.get('Individuo')
        grade_professores = populacao.get('Grade Professor')
        if random.random() < TAXA_MUTACAO:
            turma_id = random.choice(list(individuo.keys()))
            grade = individuo[turma_id]
            turma = turmas[turma_id]
            horarios_possiveis = list(TURNOS_HORARIOS[turma.turno])
            
            # Escolher aleatoriamente um dia e horário para o primeiro bloco de disciplina1
            dia1 = random.randint(0, 4)
            horario1 = random.choice(horarios_possiveis)
            disciplina1 = grade[horario1][dia1]
            
            # Verificar se a disciplina1 está no primeiro horário do seu bloco
            while disciplina1 and (horario1 > 0 and grade[horario1 - 1][dia1] == disciplina1):
                horario1 = random.choice(horarios_possiveis)
                disciplina1 = grade[horario1][dia1]
            
            if disciplina1:
                # Encontrar um bloco diferente para troca
                dia2 = random.randint(0, 4)
                horario2 = random.choice(horarios_possiveis)
                disciplina2 = grade[horario2][dia2]
                while (dia2 == dia1 and horario2 == horario1) or (horario2 > 0 and grade[horario2 - 1][dia2] == disciplina2):
                    dia2 = random.randint(0, 4)
                    horario2 = random.choice(horarios_possiveis)
                
                if disciplina2:
                    # Calcular o tamanho do bloco de cada disciplina
                    bloco1 = calcular_tamanho_bloco(grade, horario1, dia1, disciplina1)
                    bloco2 = calcular_tamanho_bloco(grade, horario2, dia2, disciplina2)
                    
                    # Verificar se os blocos estão dentro dos limites da grade
                    if horario1 + bloco1 <= len(horarios_possiveis) and horario2 + bloco2 <= len(horarios_possiveis):
                        bloco1_livre = all(
                            horario1 + i < len(horarios_possiveis) and grade[horario1 + i][dia1] == disciplina1 for i in range(bloco1)
                        )
                        bloco2_livre = all(
                            horario2 + i < len(horarios_possiveis) and grade[horario2 + i][dia2] == disciplina2 for i in range(bloco2)
                        )

                        if bloco1_livre and bloco2_livre:
                            # Verificar disponibilidade de todos os professores de disciplina1 nos novos horários
                            professor1_disponivel = all(
                                all(grade_professores[professor][horario2 + i][dia2] is None 
                                    for i in range(bloco1))
                                for professor in disciplina1.professores
                            )
                            # Verificar disponibilidade de todos os professores de disciplina2 nos novos horários
                            professor2_disponivel = all(
                                all(grade_professores[professor][horario1 + i][dia1] is None 
                                    for i in range(bloco2))
                                for professor in disciplina2.professores
                            )

                            if professor1_disponivel and professor2_disponivel:
                                # Realizar a troca
                                
                                for i in range(min(bloco1, bloco2)):
                                    t = grade[horario1 + i][dia1]
                                    grade[horario1 + i][dia1] = grade[horario2 + i][dia2]
                                    grade[horario2 + i][dia2] = t

                                    # Atualizar a grade dos professores usando o nome dos professores
                                    for professor in disciplina1.professores:
                                        grade_professores[professor][horario1 + i][dia1] = None
                                        grade_professores[professor][horario2 + i][dia2] = disciplina1

                                    for professor in disciplina2.professores:
                                        grade_professores[professor][horario2 + i][dia2] = None
                                        grade_professores[professor][horario1 + i][dia1] = disciplina2
                    
            individuo[turma_id] = grade
    return offspring



def algoritmo_genetico(turmas, professores, salas):
    # Inicializa a população com possíveis soluções iniciais (cromossomos)
    populacao = inicializar_populacao(turmas, professores, salas)
    
    # Define o número de gerações para a execução do algoritmo
    for geracao in range(GERACOES):
        # Avalia a aptidão de cada indivíduo na população
        fitness_scores = [avaliar_aptidao(individuo, professores, salas) for individuo in populacao]
        
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
    melhor_alvo = max(populacao, key=lambda individuo: avaliar_aptidao(individuo, professores, salas))
    melhor_individuo = melhor_alvo.get('Individuo')
    grade_professores = melhor_alvo.get('Grade Professor')
    
    # Retorna o melhor indivíduo encontrado como solução
    return melhor_individuo, grade_professores

                             
def main():
    with open('../Data/horarios.json', 'r') as f:
        horarios = json.load(f)

    df = lerXML("../data/magister_asctimetables_2024-04-22-15-12-35_curitiba.xml")
    df_dispo_profes = df['teachers']
    df_salas = pd.read_excel("../Data/Relatorio_dos_Espacos_de_Ensino 1.xlsx", skiprows=1, header=1)
    df_salas = df_salas.drop(columns=["Unnamed: 0"])

    all_files = glob.glob(os.path.join("../Data/politecnica/" , "*.xlsm"))

    print(all_files)

    lit = []

    for filename in all_files:
        df_t = pd.read_excel(filename, sheet_name="DISCIPLINAS REGULARES", skiprows=4)
        lit.append(df_t)

    df_turmas = pd.concat(lit, axis=0, ignore_index=True)
    df_turmas = df_turmas.dropna(thresh=6)
    df_turmas = df_turmas.rename(columns={'DOCENTE 2024.2\nConsulte aqui\n\n(possível fazer seleção múltipla)':"DOCENTE", "Previsão de número de estudantes": 'qtdEstudantes'})

    df_prof = pd.read_excel("../Data/Planilha_Geral_Professores.xlsm", sheet_name="CONSULTA - Professores", skiprows=8)

    semestre_atual = "2024/1"
    data = loadData(df_prof, df_salas, df_turmas, df_dispo_profes, semestre_atual)

    melhor_individuo, grade_professores = algoritmo_genetico(data.turmas, data.professores, data.salas)

    prof = grade_professores.get("ANDREY CABRAL MEIRA")
    teste1 = melhor_individuo.get("CCCO - 2.0A - M - 2024/1")
    teste2 = melhor_individuo.get("CCCO - 2.0B - M - 2024/1")
    display_grade(prof, horarios)

    display_grade(teste1, horarios)
    display_grade(teste2, horarios)

    # for turma_id, grade in melhor_individuo.items():
    #     print(f"Turma: {turma_id}")
    #     display_grade(grade, horarios)
    #     print(data.turmas[turma_id].disciplinas)



if __name__ == "__main__":
    main()
