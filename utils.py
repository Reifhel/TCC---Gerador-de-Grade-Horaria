from model import Data, Disciplina, Professor, Sala, Turma

import json
import pandas as pd
from glob import glob
import xml.etree.ElementTree as ET

def loadData(data_professores, data_salas, data_disciplinasTurmas, carga_Professores):

    # Inicializando os dicionarios
    turmas = {}
    professores = {}
    salas = {}
    disciplinas = {}

    # Carregando dado dos professores
    for _, professor in data_professores.iterrows():
        nome,matricula = professor['name'].split(";")
        disponibilidade = arrumaDisponibilidade(professor['timeoff'])

        prof = Professor(nome, matricula)
        prof.setDisponibilidade(disponibilidade)
        prof.setGrade(criarGrade())

        if professores.get(matricula) == None:
            professores[matricula] = prof
        else:
            pass
        
    # Adicionando a carga horaria do professor
    for _, professor in carga_Professores.iterrows():
        matricula = professor['MATRÍCULA']
        cargaHoraria = professor["""CONTRATO
PADRÃO (2024.1)"""]
        
        if str(matricula) in professores:
            prof = professores[str(matricula)]
            prof.setCargaHoraria(cargaHoraria)
            professores[matricula] = prof

    # Populando as disciplinas e turmas
    for _, disciplina in data_disciplinasTurmas.iterrows():

        turno = siglaTurno(disciplina["Turno"])
        siglaCurso = disciplina["Grade Curricular"].split(" ")[0]
        # Colocando a turma no formato
        turma = f'{siglaCurso} - {disciplina["Período"]}{disciplina["Turma"]} - {turno} - {semestre_atual}'

        # Pegando os dados da disciplina
        nome = disciplina['Nome da Disciplina']
        codigo = disciplina['Código da Disciplina']
        tipo = disciplina["Tipo de Atividade"]
        ch = disciplina['CH / Nº de Créditos']
        qtdEstudantes = disciplina["qtdEstudantes"]
        periodo = disciplina['Período']
        curso = disciplina['Nome do Curso']

        # Chave de disciplina turma
        chave = f'{codigo} | {turma}'

        # Criando um objeto de Disciplina
        objDiscipina = Disciplina(nome, codigo, turma, periodo, tipo, curso, ch, qtdEstudantes)
        if disciplina["DOCENTE"] != "nan":
            objDiscipina.addProf(disciplina["DOCENTE"])

        # Criando um objeto de turma caso não exista ou adicionando a disciplina caso exista
        if turma not in turmas:
            objTurma = Turma(turma, curso, disciplina["Turno"])
            objTurma.addDisciplina(chave)
            objTurma.setGrade(criarGrade())
            turmas[turma] = objTurma
        elif turma in turmas:
            t = turmas[turma]
            if chave not in t.disciplinas:
                t.addDisciplina(chave)
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
            capacidade = sala['CAPACIDADE']
            metodologia = sala['METODOGIA ATIVA?']

            objSala = Sala(id_sala, nome_sala, capacidade, tipo_sala, bloco, andar, metodologia)
            salas[id_sala] = objSala


    return Data(turmas, professores, salas, disciplinas)

def criarGrade():
    # Definições Básicas
    dias = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado"]

    # Importando os Horários
    df = pd.read_json("../data/horarios.json")

    # Definição da Grade
    grade = {}

    for dia in dias:
        grade[dia] = {}
        grade[dia]["Manhã"] = {}
        grade[dia]["Tarde"] = {}
        grade[dia]["Noite"] = {}

        for _,periodo in df.iterrows():

            if int(periodo['period']) <= 7:
                grade[dia]["Manhã"][periodo['period']] = ""
            elif int(periodo['period']) >= 15:
                grade[dia]["Noite"][periodo['period']] = ""
            else:
                grade[dia]["Tarde"][periodo['period']] = ""

    return grade

def arrumaDisponibilidade(disponibilidade):
    dias = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado"]

    # Definição da Grade
    grade = {}
    splitDisponibilidade = disponibilidade.replace(".", "").split(",")

    for i, dia in enumerate(dias):
        disponibilidadeDia = list(splitDisponibilidade[i])

        grade[dia] = disponibilidadeDia

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

if __name__ == '__main__':

    df = lerXML("../data/magister_asctimetables_2024-04-22-15-12-35_curitiba.xml")
    df_prof = df['teachers']
    df_cargaProf = pd.read_excel("../Data/Planilha de Turmas 2024.2_Ciência da Computação.xlsm", sheet_name="CONSULTA - Professores", skiprows=8)
    df_disciplinasTurmas = pd.read_excel("../Data/Planilha de Turmas 2024.2_Ciência da Computação.xlsm", sheet_name="DISCIPLINAS REGULARES", skiprows=4)
    df_salas = pd.read_excel("../Data/Relatorio_dos_Espacos_de_Ensino 1.xlsx", skiprows=1, header=1)
    df_salas = df_salas.drop(columns=["Unnamed: 0"])

    semestre_atual = "2024/1"

    teste = loadData(df_prof, df_salas, df_disciplinasTurmas, df_cargaProf)

    print(teste.salas)


