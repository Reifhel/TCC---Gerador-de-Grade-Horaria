from datetime import datetime, timedelta


def pontuacao_professores(grade_professores: dict, data_professores: dict, horarios: list) -> float:
    """Função para gerar a pontuação do professor pelas restrições impostas.

    Args:
        grade_professores (dict): Dicionário composto por nome e grade {"Professor": [[]], ...}.
        data_professores (dict): Dicionário que contém os dados de cada professor.
        horarios (list): Lista de horários com períodos de início e término.

    Returns:
        float: Pontuação alcançada ao passar pelas restrições.
    """
    score = 0.0

    for nome_professor, grade in grade_professores.items():
        for dia in range(6):

            # Contador para verificar carga máxima diária do professor
            contagem_horas_aula = 0

            # Identificar o horário de término do dia
            horario_termino = None
            for horario in range(20):
                professor_id = nome_professor
                professor = data_professores[professor_id]

                # Verificação de Disponibilidades
                if len(professor.disponibilidade) > 0:
                    # Verificando se tem uma disciplina no horário e está alocando em horário que o professor tem disponibilidade
                    if grade[horario][dia] is not None and professor.disponibilidade[horario][dia]:
                        score += 0.5
                    # Verificando se tem uma disciplina no horário e está alocando em horário que o professor não tem disponibilidade
                    elif grade[horario][dia] is not None and not professor.disponibilidade[horario][dia]:
                        score -= 0.5  # Penalidade por alocar professor em horário indisponível
                    else:
                        pass

                if grade[horario][dia] is not None:
                    contagem_horas_aula += 1
                    horario_termino = horarios[horario]['endtime']

            # Penalização proporcional por exceder 8 horas de aula por dia
            if contagem_horas_aula > 8:
                excesso_horas = contagem_horas_aula - 8
                score -= excesso_horas * 2  # Penalização proporcional
            else:
                score += 1  # Aumento por respeitar

            # Se não for o último dia da semana, verificar interjornada
            if dia < 5 and horario_termino is not None:
                # Identificar o horário de início do próximo dia
                horario_inicio_proximo_dia = None
                for horario in range(20):
                    if grade[horario][dia + 1] is not None:
                        horario_inicio_proximo_dia = horarios[horario]['starttime']
                        break

                if horario_inicio_proximo_dia is not None:
                    # Verificando se existe interjornada ou não
                    score += calcula_interjornada(horario_termino, horario_inicio_proximo_dia)

    return score


def pontuacao_individuo(individuo: dict) -> float:
    """Função para gerar a pontuação do indivuduo (turma) pelas restrições impostas

    Args:
        individuo (dict): Dicionário composto por chave da turma e grade

    Returns:
        float: Pontuação alcançada ao passar pelas restrições
    """
    score = 0.0

    for _, grade in individuo.items():
        for dia in range(6):
            disciplina_dia = []
            aulas_por_dia = 0
            for horario in range(20):
                disciplina = grade[horario][dia]
                aulas_por_dia += 1

                # Mais de 2 disciplinas por dia
                if disciplina:
                    if disciplina.id not in disciplina_dia:
                        disciplina_dia.append(disciplina.id)

                # Mais de 2 disciplinas por dia
                if len(disciplina_dia) > 2:
                    score -= 1

            disciplina_dia = []

    return score


def pontuacao_salas(salas: dict) -> float:
    """Função para calcular a pontuação das turmas ao decorrer das restrições

    Args:
        salas (dict): Dicionário composto pela chave sendo o identificador de sala e sua grade

    Returns:
        float: Pontuação alcançada ao passar pelas restrições
    """
    score = 0.0

    return score


def calcula_interjornada(horario_termino: datetime, horario_inicio_proximo_dia: datetime) -> float:
    """Função para calcular interjornada entre 2 horários, ou seja, verificar se houve um espaço de 11 horas entre ambos

    Args:
        horario_termino (datetime): Horário de termino de um dos dias
        horario_inicio_proximo_dia (datetime): Horário de inicio para o outro dia

    Returns:
        float: Retorna uma pontuação (deficit_horas * 2) caso haja, senão 1
    """

    score = 0.0
    # Converter horários para datetime
    fmt = "%H:%M"
    termino = datetime.strptime(horario_termino, fmt)
    inicio_proximo_dia = datetime.strptime(horario_inicio_proximo_dia, fmt)

    # Se o horário do próximo dia for mais cedo que o término, adicionar 1 dia
    if inicio_proximo_dia < termino:
        inicio_proximo_dia += timedelta(days=1)

    # Calcular o intervalo entre o término de um dia e o início do próximo
    intervalo_horas = (inicio_proximo_dia - termino).total_seconds() / 3600

    # Penalização proporcional por não respeitar a interjornada de 11 horas
    if intervalo_horas < 11:
        deficit_horas = 11 - intervalo_horas
        score -= deficit_horas * 2  # Penalização proporcional
    else:
        score += 1  # Aumento por respeitar

    return score


# if __name__ == "__main__":

#     termino_teste = "21:30"
#     começo_teste = "7:50"

#     print(calcula_interjornada(termino_teste, começo_teste))
