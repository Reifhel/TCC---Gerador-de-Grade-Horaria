from model import Data, Disciplina, Professor, Sala, Turma

import json
import pandas as pd
from glob import glob
import xml.etree.ElementTree as ET

def load_data(data_professores, data_salas, data_disciplinasTurmas, disponibilidade_Professores, semestre_atual):

    # Inicializando os dicionarios
    turmas = {}
    professores = {}
    salas = {}
    disciplinas = {}

    # Carregando dado dos professores
    for _, professor in data_professores.iterrows():
        nome = professor['DOCENTE']
        matricula = professor['MATRÍCULA']

        cargaHoraria = professor["""CONTRATO
PADRÃO (2024.1)"""]
        
        prof = Professor(nome, matricula)
        prof.setCargaHoraria(cargaHoraria)
        if professores.get(nome) == None:
            professores[nome] = prof
        else:
            pass
        
    # Adicionando a carga horaria do professor
    for _, professor in disponibilidade_Professores.iterrows():
        nome,matricula = professor['name'].split(";")
        disponibilidade = arruma_disponibilidade(professor['timeoff'])

        try:    
            prof = professores[nome]
            prof.setDisponibilidade(disponibilidade)
            professores[nome] = prof
        except:
            pass

    # Populando as disciplinas e turmas
    for _, disciplina in data_disciplinasTurmas.iterrows():

        turno = sigla_turno(disciplina["Turno"])
        siglaCurso = str(disciplina["Grade Curricular"]).split(" ")[0]
        # Colocando a turma no formato
        turma = f'{siglaCurso} - {disciplina["Período"]}{disciplina["Turma"]} - {turno} - {semestre_atual}'

        # Pegando os dados da disciplina
        nome = disciplina['Nome da Disciplina']
        codigo = disciplina['Código da Disciplina']
        tipo = disciplina["Tipo de Atividade"]
        ch = disciplina['CH / Nº de Créditos']
        qtdEstudantes = 0
        if (pd.isna(disciplina["qtdEstudantes"]) == False or disciplina["qtdEstudantes"] != "-"):
            qtdEstudantes == disciplina["qtdEstudantes"]
        periodo = disciplina['Período']
        curso = disciplina['Nome do Curso']

        # Chave de disciplina turma
        chave = f'{codigo} | {turma}'

        if chave in disciplinas:
            objDiscipina = disciplinas[chave]
        else:
            objDiscipina = Disciplina(nome, codigo, turma, periodo, tipo, curso, ch, qtdEstudantes)

        if pd.isna(disciplina["DOCENTE"]) == False:

            splited = disciplina["DOCENTE"].split(";")

            for i in range(len(splited)):
                profes = splited[i].strip()
                if profes == "Elisangela F. Manffra":
                    profes = "ELISANGELA FERRETTI MANFFRA"
                objDiscipina.addProf(profes)
                try:
                    prof = professores[profes]
                    prof.addDisciplina(chave)
                    professores[profes] = prof
                except: 
                    print("Não achou")


        # Criando um objeto de turma caso não exista ou adicionando a disciplina caso exista
        
        if turma not in turmas:
            turno = disciplina["Turno"]
            if pd.isna(disciplina["Turno"]) == True:
                turno = "Manhã"
            objTurma = Turma(turma, curso, turno)
            if objDiscipina not in objTurma.disciplinas:
                objTurma.addDisciplina(objDiscipina)
            objTurma.setGrade(criar_grade())
            turmas[turma] = objTurma
        elif turma in turmas:
            t = turmas[turma]
            if objDiscipina not in t.disciplinas:
                t.addDisciplina(objDiscipina)
            turmas[turma] = t

        if chave not in disciplinas:
            disciplinas[chave] = objDiscipina

    # Populando as salas
    for _, sala in data_salas.iterrows():
        if sala['UTILIZADO NA GRADUACAO'] == "Sim":
            bloco = sala['BLOCO']
            andar = sala['ANDAR']
            nome_sala  = sala['NOME DO ESPAÇO']
            id_sala = sala['NOME ESPAÇO ASC']
            tipo_sala = sala['TIPO DE INSTALAÇÃO DETALHADO']
            capacidade =  sala['CAPACIDADE'] if pd.isna(sala['CAPACIDADE']) == False else 0
            metodologia = sala['METODOGIA ATIVA?']

            objSala = Sala(id_sala, nome_sala, capacidade, tipo_sala, bloco, andar, metodologia)
            if id_sala not in salas:
                salas[id_sala] = objSala

    # Retornando os dados gerais
    return Data(turmas, professores, salas, disciplinas)

def criar_grade() -> list:
    """Função com o objetivo de gerar uma grade em uma matriz 20x6 (horários x dias)

    Returns:
        list: Matriz dos Horários pelos dias (20x6)
    """

    # Definição da Grade
    grade = []
    dias, qtdHorarios = 6, 20                   # Seg a Sabado, 20 horários

    grade = [[None for x in range(dias)] for y in range(qtdHorarios)]

    return grade

def arruma_disponibilidade(disponibilidade: str) -> list:
    """Função que recebe como parâmetro uma string de disponilidade, faz o tratamento necessário e depois retorno uma
    matriz 20x6 de True or False para onde havia 1 e 0 respectivamente

    Args:
        disponibilidade (str): String composta de 6 valores de 20 caracteres cada, de 0 a 1 que diz respeito a disponibilidade do professor

    Raises:
        ValueError: Caso o caractere encontrado seja inválido apresenta esse erro

    Returns:
        list: Retorna matriz 20x6 de True or False para onde havia 1 e 0 respectivamente
    """
    # Definição da Grade
    linhas = disponibilidade.replace(".", "").split(',')
    grade = []
    for i in range(len(linhas[0])):
        horarios = []
        for linha in linhas:
            if linha[i] == '0':
                horarios.append(False)
            elif linha[i] == '1':
                horarios.append(True)
            else:
                raise ValueError("Caractere inválido na string de horários.")
        grade.append(horarios)

    return grade

def ler_XML(arquivo: str) -> dict:
    """Função para ler um arquivo XML e retornar todos os seus objetos internos num dicionário

    Args:
        arquivo (str): Caminho do arquivo XML

    Returns:
        dict: Dicionário com todos os objetos do XML
    """
    # lendo o arquivo
    xml_dados = open(arquivo, 'r', encoding='UTF-8').read()
    raiz = ET.XML(xml_dados)

    # definindo variaveis para os dados e para as colunas
    dados = []
    colunas = []
    datasets = {}

    # pegando os dados e passando para as variaveis
    for i, child in enumerate(raiz):
            colunas.append(child.attrib['columns'])
            for subchild in child:
                dados.append(subchild.attrib)
    
            colunas = colunas[0].split(',')

            # convertendo para dataframe
            df = pd.DataFrame(dados, columns=colunas)
            datasets[f'{child.tag}'] = df
            dados = []
            colunas = []


    return datasets

def sigla_turno(turno: str) -> str:
    """Função para pegar a sigla do turno

    Args:
        turno (str): String com o turno por extenso. Ex: Manhã

    Returns:
        str: Retorna a sigla referente ao turno. Ex: Manhã -> M
    """
    sigla_turno = ""
    if turno == "Manhã":
        sigla_turno = "M"
    elif turno == "Noite":
        sigla_turno = "N"
    elif turno == "Tarde":
        sigla_turno = "T"
    elif turno == "Manhã e Tarde":
        sigla_turno = "I"
    else:
        pass
    return sigla_turno

def display_grade(matriz: list, horarios: dict):
    """Função que ao receber uma matriz (grade) e um dicionário com os horários faz o print dela formatada

    Args:
        matriz (list): Uma matriz de 20x6 que seria referente a uma grade (Dias X Horários)
        horarios (dict): Um dicionário que lista o ininio e começo dos 20 períodos e seu identificador
    """

    days = ['Segunda-feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sabádo']

    # print heading for classrooms
    for i in range(len(matriz[0])):
        if i == 0:
            print('{:15s} {:40s}'.format('', days[i]), end='')
        else:
            print('{:40s}'.format(str(days[i])), end='')
    print()

    h_cnt = 0
    for i in range(len(matriz)):
        hora = horarios[h_cnt]
        print('{:2s} - {:2s} ->  '.format(hora['starttime'], hora['endtime']), end='')
        for j in range(len(matriz[i])):
            print('{:40s} '.format(str(matriz[i][j]) if str(matriz[i][j]) != "None" else "-"), end='')
        print()
        h_cnt += 1
        if h_cnt == 20:
            h_cnt = 0
            print()

def calcular_tamanho_bloco(grade: list, horario_inicio: int, dia: int, disciplina: Disciplina) -> int:
    """Função responsável por contar a quantidade de aulas em um bloco de disciplina específica

    Args:
        grade (list): Uma matriz 20x6 que se refere a grade curricular sendo horários por dias
        horario_inicio (int): Int que indica o horário de inicio na grade
        dia (int): Int que especifica o dia na grade
        disciplina (Disciplina): Objeto de disciplina que estamos buscando na grade

    Returns:
        int: Quantidade de aulas encontradas da disciplina passada como parametro
    """
    tamanho_bloco = 0
    while horario_inicio + tamanho_bloco < len(grade) and grade[horario_inicio + tamanho_bloco][dia] == disciplina:
        tamanho_bloco += 1
    return tamanho_bloco


if __name__ == '__main__':

    df = ler_XML("../data/magister_asctimetables_2024-04-22-15-12-35_curitiba.xml")
    df_prof = df['teachers']
    df_cargaProf = pd.read_excel("../Data/Planilha de Turmas 2024.2_Ciência da Computação.xlsm", sheet_name="CONSULTA - Professores", skiprows=8)
    df_disciplinasTurmas = pd.read_excel("../Data/Planilha de Turmas 2024.2_Ciência da Computação.xlsm", sheet_name="DISCIPLINAS REGULARES", skiprows=4)
    df_salas = pd.read_excel("../Data/Relatorio_dos_Espacos_de_Ensino 1.xlsx", skiprows=1, header=1)
    df_salas = df_salas.drop(columns=["Unnamed: 0"])

    semestre_atual = "2024/1"

    teste = load_data(df_prof, df_salas, df_disciplinasTurmas, df_cargaProf,semestre_atual)

    matriz_teste = teste.turmas

    print(matriz_teste)

    # Carregar a lista de horários
    # with open('../Data/horarios.json', 'r') as f:
    #     horarios = json.load(f)

    # display_grade(matriz_teste, horarios)


