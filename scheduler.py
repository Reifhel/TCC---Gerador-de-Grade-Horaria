import random
import json
import pandas as pd
from model import Data, Disciplina, Professor, Sala, Turma
from utils import loadData, lerXML, criarGrade, display_grade

# Parâmetros
POPULACAO_TAMANHO = 50
GERACOES = 100
TAXA_MUTACAO = 0.1
# Definição de horários por turno
TURNOS_HORARIOS = {
    "Manhã":    range(0, 6),        # Manhã
    "Tarde":    range(7, 13),       # Tarde
    "Noite":    range(14, 19),      # Noite 
    "Integral": range(0, 13)        # Integral
}

def inicializar_populacao(turmas, professores, grade_professores, salas):
    populacao = []
    for _ in range(POPULACAO_TAMANHO):
        individuo = {}
        for turma_id, turma in turmas.items():
            grade = criarGrade()
            horarios_possiveis = list(TURNOS_HORARIOS[turma.turno])
            disciplinas = turma.disciplinas.copy()

            for i in range(len(disciplinas)):
                rand = random.randint(0, len(disciplinas)) - 1 
                disciplina = disciplinas.pop(rand)

                horarios_alocados = 0
                carga_horaria = int(disciplina.cargaHoraria)
                tentativas = 0
                while horarios_alocados < carga_horaria and tentativas < 100:
                    dia = random.randint(0, 4)  # Seg a Sexta
                    horario_inicio = random.choice(horarios_possiveis)
                    bloco = min(2, carga_horaria - horarios_alocados)  # Alocar em blocos de 2

                    # Ajustar bloco para respeitar o turno
                    if not all(horario_inicio + i in horarios_possiveis for i in range(bloco)):
                        tentativas += 1
                        continue

                    bloco_livre = all(grade[horario_inicio + i][dia] is None for i in range(bloco))

                    if bloco_livre:
                        for i in range(bloco):
                            grade[horario_inicio + i][dia] = disciplina
                        horarios_alocados += bloco

                        # Alocar na grade do professor
                        for professor in disciplina.professores:
                            matricula_professor = professores[professor].matricula
                            if matricula_professor not in grade_professores:
                                grade_professores[matricula_professor] = criarGrade()
                            for i in range(bloco):
                                grade_professores[matricula_professor][horario_inicio + i][dia] = disciplina

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
                        # Verificação de disponibilidade do professor
                        if professor.disponibilidade[horario][dia]:
                            score += 1
                        else:
                            score -= 1  # Penalidade por alocar professor em horário indisponível
                    # Verificação de capacidade da sala
                    sala = random.choice(list(salas.values()))
                    if int(sala.capacidade) >= int(disciplina.qtdEstudantes):
                        score += 1
                    else:
                        score -= 1  # Penalidade por usar sala com capacidade insuficiente
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
    for individuo in offspring:
        if random.random() < TAXA_MUTACAO:
            turma_id = random.choice(list(individuo.keys()))
            grade = individuo[turma_id]
            turma = turmas[turma_id]
            horarios_possiveis = list(TURNOS_HORARIOS[turma.turno])
            
            # Escolher aleatoriamente dois blocos para troca
            dia1 = random.randint(0, 4)
            horario1 = random.choice(horarios_possiveis)
            disciplina1 = grade[horario1][dia1]
            
            if disciplina1:
                # Encontrar um bloco diferente para troca
                dia2 = random.randint(0, 4)
                horario2 = random.choice(horarios_possiveis)
                while dia2 == dia1 and horario2 == horario1:
                    dia2 = random.randint(0, 4)
                    horario2 = random.choice(horarios_possiveis)
                
                disciplina2 = grade[horario2][dia2]
                
                if disciplina2:
                    # Trocar os blocos de horário entre as disciplinas
                    bloco1 = min(2, int(disciplina1.cargaHoraria))
                    bloco2 = min(2, int(disciplina2.cargaHoraria))
                    
                    bloco1_livre = all(
                        horario1 + i < len(grade) and grade[horario1 + i][dia1] == disciplina1 for i in range(bloco1)
                    )
                    bloco2_livre = all(
                        horario2 + i < len(grade) and grade[horario2 + i][dia2] == disciplina2 for i in range(bloco2)
                    )
                    
                    if bloco1_livre and bloco2_livre:
                        # Realizar a troca
                        for i in range(bloco1):
                            grade[horario1 + i][dia1], grade[horario2 + i][dia2] = grade[horario2 + i][dia2], grade[horario1 + i][dia1]
                    
            individuo[turma_id] = grade
    return offspring

def algoritmo_genetico(turmas, professores, grade_professores, salas):
    populacao = inicializar_populacao(turmas, professores, grade_professores, salas)
    for geracao in range(GERACOES):
        fitness_scores = [avaliar_aptidao(individuo, professores, salas) for individuo in populacao]
        parents = selecao(populacao, fitness_scores)
        offspring = cruzamento(parents)
        offspring = mutacao(offspring, turmas)
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

    grade_professores = {}

    melhor_individuo = algoritmo_genetico(data.turmas, data.professores, grade_professores, data.salas)
    for turma_id, grade in melhor_individuo.items():
        print(f"Turma: {turma_id}")
        display_grade(grade, horarios)
        print(data.turmas[turma_id].disciplinas)


if __name__ == "__main__":
    main()
