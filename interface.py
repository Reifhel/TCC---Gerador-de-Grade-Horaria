import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
from PyQt5.QtCore import QTimer
from ui_interface import Ui_MainWindow
from scheduler import carrega_arquivos, main, PROGRESSO

class Interface():
    def __init__(self) -> None:
        self.janela = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.janela)

        # Definindo aba principal
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        ''' Botões '''
        #self.ui.botaoCurso.setEnabled(False)
        #self.ui.botaoProf.setEnabled(False)

        # Alternar abas
        self.ui.menuHome.clicked.connect(lambda _, aba=self.ui.home: self.abrirAba(aba))
        self.ui.botaoCurso.clicked.connect(lambda _, aba=self.ui.curso: self.abrirAba(aba))
        self.ui.menuCurso.clicked.connect(lambda _, aba=self.ui.curso: self.abrirAba(aba))
        self.ui.botaoProf.clicked.connect(lambda _, aba=self.ui.professor: self.abrirAba(aba))
        self.ui.menuProf.clicked.connect(lambda _, aba=self.ui.professor: self.abrirAba(aba))
        self.ui.botaoSala.clicked.connect(lambda _, aba=self.ui.salas: self.abrirAba(aba))
        self.ui.menuSala.clicked.connect(lambda _, aba=self.ui.salas: self.abrirAba(aba))

        # Buscar arquivos
        self.ui.buscarTurma.clicked.connect(lambda _, botao="T": self.buscarArquivo(botao))
        self.ui.buscarSala.clicked.connect(lambda _, botao="S": self.buscarArquivo(botao))
        self.ui.buscarProf.clicked.connect(lambda _, botao="P": self.buscarArquivo(botao))

        # Executar o código
        self.ui.botaoEnsalamento.clicked.connect(self.gerarEnsalamento)
        self.ui.aplicarFiltrosCurso.clicked.connect(self.popularTabela)
        self.ui.aplicarFiltrosProf.clicked.connect(self.popularTabela)
        self.ui.aplicarFiltrosSala.clicked.connect(self.popularTabela)

        # Estrutura padrão da tabela
        larguraColuna = 139
        for coluna in range(self.ui.tabelaGrade.columnCount()):
            self.ui.tabelaGrade.setColumnWidth(coluna, larguraColuna)
            self.ui.tabelaGradeProfessor.setColumnWidth(coluna, larguraColuna)
            self.ui.tabelaGradeSala.setColumnWidth(coluna, larguraColuna)

    def show(self):
        self.janela.show()

    def abrirAba(self, aba):
        self.ui.stackedWidget.setCurrentWidget(aba)

    def buscarArquivo(self, botao):
        file = QFileDialog.getOpenFileName(self.janela, 'Explorador de Arquivos', os.getcwd())
        if botao == "T":
            self.ui.arquivoTurmas.setText(file[0])
            self.arquivoTurmas = file[0]
        elif botao == "S":
            self.ui.arquivoSalas.setText(file[0])
            self.arquivoSalas = file[0]
        else:
            self.ui.arquivoProfs.setText(file[0])
            self.arquivoProf = file[0]

    def popularFiltros(self, cursos, periodos, turmas):
        filtros = {
            self.ui.filtroCurso: "Curso",
            self.ui.filtroCursoProf: "Curso",
            self.ui.filtroCursoSala: "Curso",
            self.ui.filtroPeriodo: "Período",
            self.ui.filtroPeriodoProf: "Período",
            self.ui.filtroPeriodoSala: "Período",
            self.ui.filtroTurma: "Turma",
            self.ui.filtroTurmaProf: "Turma",
            self.ui.filtroTurmaSala: "Turma"
            # Falta add filtroProfessor e filtroSala
        }

        for filtro, contexto in filtros.items():
            if contexto == "Curso":
                filtro.addItems(cursos)
            elif contexto == "Período":
                filtro.addItems(periodos)
            else:
                filtro.addItems(turmas)

    def popularTabela(self):
        tabelas = {
            self.ui.tabelaGrade: self.ui.filtroTurma,
            self.ui.tabelaGradeProfessor: self.ui.filtroTurmaProf,
            self.ui.tabelaGradeSala: self.ui.filtroTurmaSala
        }

        for tabela, filtro in tabelas.items():
            # Limpando conteúdo da tabela
            tabela.setRowCount(0)

            # Selecionando grade de acordo com filtro
            turma_selecionada = filtro.currentText()
            grade_selecionada = self.melhor_individuo.get(turma_selecionada)

            h_cnt = 0
            for i in range(len(grade_selecionada)):
                posicao_atual = tabela.rowCount()
                tabela.insertRow(posicao_atual)
                hora = self.horarios[h_cnt]
                intervalo = f"{hora['starttime']:2s} - {hora['endtime']:2s}"
                intervalo_atual = QTableWidgetItem(intervalo)
                tabela.setItem(posicao_atual, 0, intervalo_atual)
                for j in range(len(grade_selecionada[i])):
                    id = str(grade_selecionada[i][j]) if str(grade_selecionada[i][j]) != "None" else "-"
                    id_atual = QTableWidgetItem(id)
                    tabela.setItem(posicao_atual, j+1, id_atual)
                h_cnt += 1

    def gerarEnsalamento(self):
        arquivo_dispo_prof = "../data/magister_asctimetables_2024-04-22-15-12-35_curitiba.xml"
        arquivo_salas = "../Data/Relatorio_dos_Espacos_de_Ensino 1.xlsx"
        arquivo_turmas = "../Data/politecnica/"
        arquivo_prof = "../Data/Planilha_Geral_Professores.xlsm"

        data, self.horarios = carrega_arquivos(arquivo_dispo_prof, arquivo_salas, arquivo_turmas, arquivo_prof, "2024/2")
        self.melhor_individuo, _ = main(data, self.horarios)
        cursos = []
        periodos = []
        turmas = []
        for id, value in data.turmas.items():
            if value.curso not in cursos and isinstance(value.curso, str):
                cursos.append(value.curso)
            if str(value.periodo) not in periodos and isinstance(value.periodo, float):
                periodos.append(str(value.periodo))
            if id not in turmas:
                turmas.append(id)

        self.popularFiltros(cursos, periodos, turmas)
        self.popularTabela()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = Interface()
    janela.show()
    sys.exit(app.exec_())