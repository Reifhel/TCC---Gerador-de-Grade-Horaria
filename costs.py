def custo_professores(grade_professores, data_professores):
    custo_total = 0

    for nome_professor, grade in grade_professores.items():
        for dia in range(6):

            # contador para verificar carga máxima diaria do professor
            contagem_horas_aula = 0

            for horario in range(20):
                professor_id = nome_professor
                professor = data_professores[professor_id]

                # Verificação de Disponibilidades
                if len(professor.disponibilidade) > 0:
                    # Verificando se tem uma disciplina no horário e está alocando em horário que professor tem disponiblidade
                    if grade[horario][dia] != None and (professor.disponibilidade[horario][dia] == True):
                        custo_total += .5
                    # Verificando se tem uma disciplina no horário e está alocando em horário que professor não tem disponiblidade
                    elif grade[horario][dia] != None and (professor.disponibilidade[horario][dia] == False):
                        custo_total -= .5  # Penalidade por alocar professor em horário indisponível
                    else:
                        pass

                if grade[horario][dia] != None:
                    contagem_horas_aula += 1

            # No máximo 8 horas aula por dia
            if contagem_horas_aula > 8:
                custo_total -= 1

    return custo_total

def custo_indiviuo(individuo):
    custo_total = 0

    for turma_id, grade in individuo.items():
        for dia in range(6):
            disciplinasDia = []
            for horario in range(20):
                disciplina = grade[horario][dia]

                # Mais de 2 disciplinas por dia
                if disciplina:
                    if disciplina.id not in disciplinasDia:
                        disciplinasDia.append(disciplina.id)

                # Mais de 2 disciplinas por dia
                if len(disciplinasDia) > 2:
                    custo_total -= 1

            disciplinasDia = []


    return custo_total

def custo_sala(salas):
    return

