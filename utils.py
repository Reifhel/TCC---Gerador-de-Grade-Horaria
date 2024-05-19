from model import Data, Disciplina, Professor, Sala, Turma

import json
import pandas as pd
from glob import glob
import xml.etree.ElementTree as ET

def loadData(data_professores, data_salas, data_turmas):

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
    disponibilidadeFormatada = disponibilidade.replace(".", "").split(",")

    for dia in range(0, len(disponibilidadeFormatada)):
        grade[dias[dia]] = {}
        grade[dias[dia]]["Manhã"] = {}
        grade[dias[dia]]["Tarde"] = {}
        grade[dias[dia]]["Noite"] = {}

        for i, disponivel in enumerate((disponibilidadeFormatada[dia])):
            valor = True if disponivel == "1" else False

            if i <= 7:
                grade[dias[dia]]["Manhã"][i+1] = valor
            elif i >= 15:
                grade[dias[dia]]["Noite"][i+1] = valor
            else:
                grade[dias[dia]]["Tarde"][i+1] = valor

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


if __name__ == '__main__':

    df = lerXML("")
    df_prof = df['teachers']

    teste = loadData(df_prof, "", "")
    print(teste.professores)


