class Turma:
    def __init__(self, qtdAlunos, id, turno):
        self.qtdAlunos = qtdAlunos
        self.id = id
        self.grade = {}
        self.turno = turno
    
    def setGrade(self, grade):
        self.disponibilidade = grade
        
class Professor:
    def __init__(self, nome, matricula):
        self.matricula = matricula
        self.nome = nome
        self.disponibilidade = {}
        self.grade = {}
        self.cargaHoraria = 0
        self.disciplinas = []

    def setDisponibilidade(self, disponibilidade):
        self.disponibilidade = disponibilidade

    def setGrade(self, grade):
        self.grade = grade

    def addDisciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def setCargaHoraria(self, carga):
        self.cargaHoraria = carga

    def __str__(self):
         return f"{self.nome};{self.matricula} - {self.disciplinas}\n {self.disponibilidade} \n {self.grade} \n"
    
    def __repr__(self):
        return str(self)

class Sala:
    def __init__(self, capacidade, tipo, nome, bloco, andar, id, metodologia):
        self.capacidade = capacidade
        self.tipo = tipo
        self.nome = nome 
        self.bloco = bloco
        self.andar = andar
        self.id = id
        self.andar = metodologia
        self.grade = {}

    def setGrade(self, grade):
        self.disponibilidade = grade

class Disciplina:
    def __init__(self, professor, sala, disciplina, turma, periodo, tipo, curso, cargaHoraria):
        self.id = f"{disciplina} | {turma}"
        self.disciplina = disciplina
        self.professor = professor
        self.sala = sala
        self.periodo = periodo
        self.tipo = tipo
        self.cargaHoraria = cargaHoraria
        self.curso = curso

class Data:
    def __init__(self, turmas, professores, salas, disciplinas):
        self.turmas = turmas
        self.professores = professores
        self.salas = salas
        self.disciplinas = disciplinas
