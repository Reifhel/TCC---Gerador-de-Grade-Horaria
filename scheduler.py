import random
import json
import pandas as pd
from model import Data, Disciplina, Professor, Sala, Turma
from utils import loadData, lerXML, criarGrade, arrumaDisponibilidade, siglaTurno, display_grade

# Parâmetros
POPULACAO_TAMANHO = 50
GERACOES = 1000
TAXA_MUTACAO = 0.1
# Definição de horários por turno
TURNOS_HORARIOS = {
    "Manhã":    range(0, 7),        # Manhã
    "Tarde":    range(8, 14),       # Tarde
    "Noite":    range(15, 20),      # Noite 
    "Integral": range(0, 14)        # Integral
}

def inicializar_populacao(turmas, grade_professores, grade_salas):
    populacao = []
    for _ in range(POPULACAO_TAMANHO):
        individuo = {}
        for turma_id, turma in turmas.items():
            grade = criarGrade()
            horarios_possiveis = list(TURNOS_HORARIOS[turma.turno])
            for disciplina in turma.disciplinas:
                horarios_alocados = 0
                carga_horaria = int(disciplina.cargaHoraria)
                tentativas = 0
                while horarios_alocados < carga_horaria and tentativas < 100:
                    dia = random.randint(0, 5)  # Seg a Sabado
                    horario_inicio = random.choice(horarios_possiveis)
                    bloco = min(2, carga_horaria - horarios_alocados)  # Alocar em blocos de 2

                    # Ajustar bloco para respeitar o turno
                    if horario_inicio + bloco - 1 not in horarios_possiveis:
                        tentativas += 1
                        continue

                    bloco_livre = True
                    for i in range(bloco):
                        if grade[horario_inicio + i][dia] is not None:
                            bloco_livre = False
                            break

                    if bloco_livre:
                        for i in range(bloco):
                            grade[horario_inicio + i][dia] = disciplina
                        horarios_alocados += bloco
                    tentativas += 1
            individuo[turma_id] = grade
        populacao.append(individuo)
    return populacao

def avaliar_aptidao(individuo, professores, salas):
    score = 0
    for turma_id, grade in individuo.items():
        for dia in range(6):
            for horario in range(20):
                disciplina = grade[horario][dia]
                if disciplina:
                    if len(disciplina.professores) > 0:
                        professor_id = disciplina.professores[0]
                        professor = professores[professor_id]
                        if professor.disponibilidade[horario][dia]:
                            score += 1
                    sala = random.choice(list(salas.values()))
                    if int(sala.capacidade) >= int(disciplina.qtdEstudantes):
                        score += 1
    return score

def selecao(populacao, fitness_scores):
    selected = random.choices(populacao, weights=fitness_scores, k=POPULACAO_TAMANHO//2)
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

def mutacao(offspring):
    for individuo in offspring:
        if random.random() < TAXA_MUTACAO:
            turma_id = random.choice(list(individuo.keys()))
            grade = individuo[turma_id]
            dia = random.randint(0, 5)
            horario = random.randint(0, 19)
            disciplina = grade[horario][dia]
            if disciplina:
                novo_dia = random.randint(0, 5)
                novo_horario = random.randint(0, 19)
                grade[horario][dia] = None
                grade[novo_horario][novo_dia] = disciplina
            individuo[turma_id] = grade
    return offspring

def algoritmo_genetico(turmas, professores, salas):
    populacao = inicializar_populacao(turmas, professores, salas)
    for geracao in range(GERACOES):
        fitness_scores = [avaliar_aptidao(individuo, professores, salas) for individuo in populacao]
        parents = selecao(populacao, fitness_scores)
        offspring = cruzamento(parents)
        offspring = mutacao(offspring)
        populacao = parents + offspring
        if geracao % 10 == 0:
            print(f'Geração {geracao}, melhor aptidão: {max(fitness_scores)}')
    melhor_individuo = max(populacao, key=lambda individuo: avaliar_aptidao(individuo, professores, salas))
    return melhor_individuo
                             

def main():
    with open('../Data/horarios.json', 'r') as f:
        horarios = json.load(f)

    df = lerXML("../data/magister_asctimetables_2024-04-22-15-12-35_curitiba.xml")
    df_prof = df['teachers']
    df_cargaProf = pd.read_excel("../Data/Planilha de Turmas 2024.2_Ciência da Computação.xlsm", sheet_name="CONSULTA - Professores", skiprows=8)
    df_disciplinasTurmas = pd.read_excel("../Data/Planilha de Turmas 2024.2_Ciência da Computação.xlsm", sheet_name="DISCIPLINAS REGULARES", skiprows=4)
    df_salas = pd.read_excel("../Data/Relatorio_dos_Espacos_de_Ensino 1.xlsx", skiprows=1, header=1)
    df_salas = df_salas.drop(columns=["Unnamed: 0"])

    semestre_atual = "2024/1"
    data = loadData(df_prof, df_salas, df_disciplinasTurmas, df_cargaProf, semestre_atual)

    melhor_individuo = algoritmo_genetico(data.turmas, data.professores, data.salas)
    for turma_id, grade in melhor_individuo.items():
        print(f"Turma: {turma_id}")
        display_grade(grade, horarios)


if __name__ == "__main__":
    main()
