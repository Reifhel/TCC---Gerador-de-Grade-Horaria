def pontuacao_professores(grade_professores: dict, data_professores: dict) -> float:
    """Função para gerar a pontuação do professor pelas restrições impostas

    Args:
        grade_professores (dict): Dicionário composto por nome e grade {"Professor": [[]], ...}
        data_professores (dict): Dicionário que contem os dados de cada professor

    Returns:
        float: Pontuação alcançada ao passar pelas restrições
    """
    score = 0.0

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
                    if grade[horario][dia] is not None and (professor.disponibilidade[horario][dia] is True):
                        score += .5
                    # Verificando se tem uma disciplina no horário e está alocando em horário que professor não tem disponiblidade
                    elif grade[horario][dia] is not None and (professor.disponibilidade[horario][dia] is False):
                        score -= .5  # Penalidade por alocar professor em horário indisponível
                    else:
                        pass

                if grade[horario][dia] is not None:
                    contagem_horas_aula += 1

            # No máximo 8 horas aula por dia
            if contagem_horas_aula > 8:
                score -= 1

    return score


def pontuacao_indiviuo(individuo: dict) -> float:
    """Função para gerar a pontuação do indivuduo (turma) pelas restrições impostas

    Args:
        individuo (dict): Dicionário composto por chave da turma e grade

    Returns:
        float: Pontuação alcançada ao passar pelas restrições
    """
    score = 0.0

    for turma_id, grade in individuo.items():
        for dia in range(6):
            disciplina_dia = []
            for horario in range(20):
                disciplina = grade[horario][dia]

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
