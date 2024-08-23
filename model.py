class Turma:
    """
    Objeto de Turma
    """

    def __init__(self, id: str, curso: str, turno: str):
        """
        Iniciador de uma nova instância de Turma
        Args:
            id (str): Identificador da turma, EX: CCCO - 4.0U - N - 2024/1
            curso (str): Nome do curso
            turno (str): Turno da turma (Manhã, tarde, noite ou integral)
        """
        self.id = id
        self.curso = curso
        self.grade: list[list] = []
        self.turno = turno
        self.disciplinas: list[object] = []

    def set_grade(self, grade: list[list]) -> None:
        """
        Set para o método de Grade

        Args:
            grade (list[list]): Matriz que referencia a grade da turma
        """
        self.grade = grade

    def add_disciplina(self, disc: object) -> None:
        """Adiciona uma disciplina ao Array de disciplinas do professor

        Args:
            disc (Disciplina): Objeto da classe Disciplina
        """
        self.disciplinas.append(disc)

    def __str__(self) -> str:
        return f"{self.id} - {self.curso} - {self.turno}\n{self.disciplinas}\n{self.grade}\n"

    def __repr__(self) -> str:
        return f'Turma(id={self.id} curso={self.curso} turno={self.turno} disciplinas={self.disciplinas} grade={self.grade})'


class Professor:
    """
    Objeto de Professor
    """

    def __init__(self, nome: str, matricula: str):
        """
        Iniciador de uma nova instância de Professor

        Args:
            nome (str): String que simboliza o nome completo do professor
            matricula (str): String que simboliza a matricula do professsor
        """
        self.matricula = matricula
        self.nome = nome
        self.disponibilidade: list[list] = []
        self.carga_horaria = 0
        self.disciplinas: list[object] = []

    def set_disponibilidade(self, disponibilidade: list[list]) -> None:
        """Setter para a disponibilidade do professor

        Args:
            disponibilidade (list): Matriz de True or False que trazem a disponibilidade do professor ao longo da semana
        """
        self.disponibilidade = disponibilidade

    def add_disciplina(self, disciplina: object) -> None:
        """Função com o objetivo de adicionar um objeto da classe Disciplina ao array de Disciplinas do professor

        Args:
            disciplina (object): Objeto de Disciplina
        """
        self.disciplinas.append(disciplina)

    def set_carga_horaria(self, carga: int) -> None:
        """Setter para a carga horária do professor

        Args:
            carga (int): Quantidade de carga horária máxima do professor
        """
        self.carga_horaria = carga

    def __str__(self) -> str:
        return f"{self.nome};{self.matricula} Carga Horaria = {self.carga_horaria} - {self.disciplinas}\n {self.disponibilidade} \n"

    def __repr__(self) -> str:
        return str(self)


class Sala:
    """
    Objeto que faz referencia aos Ambientes de Aprendizado
    """

    def __init__(self, id: str, nome: str, capacidade: int, tipo: str, bloco: str, andar: str, metodologia: str) -> None:
        """
        Iniciador de uma nova instância de sala

        Args:
            id (str): Nome de Registro no ASC. Ex: Bloco 01 - Amarelo;Auditório Maria Montessori
            nome (str): Nome do ambiente de aprendizado
            capacidade (int): Capacidade de estudantes
            tipo (str): Tipo de instalação
            bloco (str): Bloco localizado
            andar (str): Andar
            metodologia (str): Tipo de metodologia do ambiente
        """
        self.capacidade = capacidade
        self.tipo = tipo
        self.nome = nome
        self.bloco = bloco
        self.andar = andar
        self.id = id
        self.metodologia = metodologia

    def __str__(self) -> str:
        return f"{self.nome};{self.id} - Capacidade: {self.capacidade}\nTipo = {self.tipo} - Metodologia Ativa? {self.metodologia}\n {self.bloco}  {self.andar} \n"

    def __repr__(self) -> str:
        return str(self)


class Disciplina:
    """
    Objeto que define uma disciplina
    """

    def __init__(self, nome: str, cod_disciplina: str, turma: str, periodo: int, tipo: str, curso: str, carga_horaria: int, qtd_estudantes: int) -> None:
        """
        Iniciador de uma nova instância de Disciplina

        Args:
            nome (str): Nome da disciplina
            cod_disciplina (str): Código da disciplina
            turma (str): Id da turma
            periodo (int): Ciclo da disciplina
            tipo (str): Tipo da disciplina
            curso (str): Curso de oferta da disciplina
            carga_horaria (int): Quantidade de horas semanais da disciplinas
            qtd_estudantes (int): Quantidade de estudantes na disciplina
        """
        self.id = f"{cod_disciplina} | {turma}"
        self.nome = nome
        self.cod_disciplina = cod_disciplina
        self.professores: list[Professor] = []
        self.sala
        self.periodo = periodo
        self.turma = turma
        self.tipo = tipo
        self.carga_horaria = carga_horaria
        self.curso = curso
        self.qtd_estudantes = qtd_estudantes

    def add_prof(self, professor: Professor) -> None:
        """Função para adicionar o professor a lista de professores da disciplina

        Args:
            professor (Professor): Objeto que faz referência ao professor alocado
        """
        self.professores.append(professor)

    def set_sala(self, sala: Sala) -> None:
        """Setter para definir a sala da disciplina

        Args:
            sala (Sala): Objeto que faz referencia a sala alocada a disciplina
        """
        self.sala = sala

    def __str__(self) -> str:
        return f"{self.id}"

    def __repr__(self) -> str:
        return str(self)


class Data:
    """
    Objeto de controle de dados para guardar os dados de turmas, professores, salas e disciplinas

    Args:
        turmas (dict): Dicionário com todos os objetos de turmas
        professores (dict): Dicionário com todos os objetos de professores
        salas (dict): Dicionário com todos os objetos de salas
        disciplinas (dict): Dicionário com todos os objetos de disciplinas
    """

    def __init__(self, turmas: dict, professores: dict, salas: dict, disciplinas: dict):
        """
        Iniciador de uma nova instância do objeto Data
        """
        self.turmas = turmas
        self.professores = professores
        self.salas = salas
        self.disciplinas = disciplinas
