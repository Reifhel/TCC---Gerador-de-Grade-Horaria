class Turma:
    def __init__(self, id, curso, turno):
        self.id = id
        self.curso = curso
        self.grade = {}
        self.turno = turno
        self.disciplinas = []
    
    def setGrade(self, grade):
        self.grade = grade

    def addDisciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def __str__(self):
         return f"{self.id} - {self.curso} - {self.turno}\n{self.disciplinas}\n{self.grade}\n"
    
    def __repr__(self):
        return str(self)

        
class Professor:
    def __init__(self, nome, matricula):
        self.matricula = matricula
        self.nome = nome
        self.disponibilidade = []
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
         return f"{self.nome};{self.matricula} Carga Horaria = {self.cargaHoraria} - {self.disciplinas}\n {self.disponibilidade} \n {self.grade} \n"
    
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
    def __init__(self, nome, codDisciplina, turma, periodo, tipo, curso, cargaHoraria, qtdEstudantes):
        self.id = f"{codDisciplina} | {turma}"
        self.nome = nome
        self.codDisciplina = codDisciplina
        self.professores = []
        self.sala = ""
        self.periodo = periodo
        self.turma = turma
        self.tipo = tipo
        self.cargaHoraria = cargaHoraria
        self.curso = curso
        self.qtdEstudantes = qtdEstudantes

    def addProf(self, professor):
        self.professores.append(professor)

    def setSala(self, sala):
        self.sala = sala

    def __str__(self):
         return f"{self.codDisciplina};{self.nome}\nCreditos = {self.cargaHoraria} | Periodo = {self.periodo} | Tipo = {self.tipo}\nTurma = {self.turma} | Sala = {self.sala}\nProfessores = {self.professores}\n"
    
    def __repr__(self):
        return str(self)

class Data:
    def __init__(self, turmas, professores, salas, disciplinas):
        self.turmas = turmas
        self.professores = professores
        self.salas = salas
        self.disciplinas = disciplinas
