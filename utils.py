from model import Data, Disciplina, Professor, Sala, Turma

import json
import pandas as pd
from glob import glob
import xml.etree.ElementTree as ET

def loadData(data_professores, data_salas, data_disciplinasTurmas, disponibilidade_Professores, semestre_atual):

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
        disponibilidade = arrumaDisponibilidade(professor['timeoff'])

        try:    
            prof = professores[nome]
            prof.setDisponibilidade(disponibilidade)
            professores[nome] = prof
        except:
            pass

    # Populando as disciplinas e turmas
    for _, disciplina in data_disciplinasTurmas.iterrows():

        turno = siglaTurno(disciplina["Turno"])
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
            objTurma.setGrade(criarGrade())
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

def criarGrade():

    # Definição da Grade
    grade = []
    dias, qtdHorarios = 6, 20                   # Seg a Sabado, 20 horários

    grade = [[None for x in range(dias)] for y in range(qtdHorarios)]

    return grade

def arrumaDisponibilidade(disponibilidade):
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

def lerXML(arquivo):
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

def siglaTurno(turno):
    siglaTurno = ""
    if turno == "Manhã":
        siglaTurno = "M"
    elif turno == "Noite":
        siglaTurno = "N"
    elif turno == "Tarde":
        siglaTurno = "T"
    elif turno == "Manhã e Tarde":
        siglaTurno = "I"
    else:
        pass
    return siglaTurno

def display_grade(matrix, horarios):
    """
    Printa a matrix recebida
    horarios: lista de horários
    """
    days = ['Segunda-feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sabádo']

    # print heading for classrooms
    for i in range(len(matrix[0])):
        if i == 0:
            print('{:15s} {:40s}'.format('', days[i]), end='')
        else:
            print('{:40s}'.format(str(days[i])), end='')
    print()

    h_cnt = 0
    for i in range(len(matrix)):
        hora = horarios[h_cnt]
        print('{:2s} - {:2s} ->  '.format(hora['starttime'], hora['endtime']), end='')
        for j in range(len(matrix[i])):
            print('{:40s} '.format(str(matrix[i][j]) if str(matrix[i][j]) != "None" else "-"), end='')
        print()
        h_cnt += 1
        if h_cnt == 20:
            h_cnt = 0
            print()

if __name__ == '__main__':

    df = lerXML("../data/magister_asctimetables_2024-04-22-15-12-35_curitiba.xml")
    df_prof = df['teachers']
    df_cargaProf = pd.read_excel("../Data/Planilha de Turmas 2024.2_Ciência da Computação.xlsm", sheet_name="CONSULTA - Professores", skiprows=8)
    df_disciplinasTurmas = pd.read_excel("../Data/Planilha de Turmas 2024.2_Ciência da Computação.xlsm", sheet_name="DISCIPLINAS REGULARES", skiprows=4)
    df_salas = pd.read_excel("../Data/Relatorio_dos_Espacos_de_Ensino 1.xlsx", skiprows=1, header=1)
    df_salas = df_salas.drop(columns=["Unnamed: 0"])

    semestre_atual = "2024/1"

    teste = loadData(df_prof, df_salas, df_disciplinasTurmas, df_cargaProf,semestre_atual)

    matrix_teste = teste.turmas

    print(matrix_teste)

    # Carregar a lista de horários
    # with open('../Data/horarios.json', 'r') as f:
    #     horarios = json.load(f)

    # display_grade(matrix_teste, horarios)


