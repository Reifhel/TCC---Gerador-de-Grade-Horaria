import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
from ui_interface import Ui_MainWindow
from scheduler import carrega_arquivos, main


class Interface():
    def __init__(self) -> None:
        self.janela = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.janela)

        # Definindo aba principal
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        # Arquivos
        self.pastaTurmas = ""
        self.arquivoSalas = ""
        self.arquivoDispoProfs = ""
        self.arquivoProfs = ""

        ''' Botões '''
        self.ui.botaoEnsalamento.setEnabled(False)
        self.ui.botaoCurso.setEnabled(False)
        self.ui.botaoProf.setEnabled(False)
        self.ui.botaoSala.setEnabled(False)
        self.ui.botaoExportar.setEnabled(False)
        self.ui.menuCurso.setEnabled(False)
        self.ui.menuProf.setEnabled(False)
        self.ui.menuSala.setEnabled(False)

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
        self.ui.buscarDispoProf.clicked.connect(lambda _, botao="DP": self.buscarArquivo(botao))
        self.ui.buscarProf.clicked.connect(lambda _, botao="P": self.buscarArquivo(botao))

        # Executar o código
        self.ui.botaoEnsalamento.clicked.connect(self.gerarEnsalamento)
        self.ui.aplicarFiltrosCurso.clicked.connect(lambda _, grade="C": self.popularTabela(grade))
        self.ui.aplicarFiltrosProf.clicked.connect(lambda _, grade="P": self.popularTabela(grade))
        self.ui.aplicarFiltrosSala.clicked.connect(lambda _, grade="S": self.popularTabela(grade))

        # Estrutura padrão da tabela
        larguraColuna = 135
        for coluna in range(self.ui.tabelaGrade.columnCount()):
            self.ui.tabelaGrade.setColumnWidth(coluna, larguraColuna)
            self.ui.tabelaGradeProfessor.setColumnWidth(coluna, larguraColuna)
            self.ui.tabelaGradeSala.setColumnWidth(coluna, larguraColuna)

    def show(self):
        self.janela.show()

    def abrirAba(self, aba):
        self.ui.stackedWidget.setCurrentWidget(aba)

    def buscarArquivo(self, botao):
        if botao == "T":
            file = QFileDialog.getExistingDirectory(self.janela, 'Explorador de Arquivos', os.getcwd())
            self.ui.pastaTurmas.setText(file)
            self.pastaTurmas = file
        elif botao == "S":
            file = QFileDialog.getOpenFileName(self.janela, 'Explorador de Arquivos', os.getcwd())
            self.ui.arquivoSalas.setText(file[0])
            self.arquivoSalas = file[0]
        elif botao == "DP":
            file = QFileDialog.getOpenFileName(self.janela, 'Explorador de Arquivos', os.getcwd())
            self.ui.arquivoDispoProfs.setText(file[0])
            self.arquivoDispoProfs = file[0]
        else:
            file = QFileDialog.getOpenFileName(self.janela, 'Explorador de Arquivos', os.getcwd())
            self.ui.arquivoProfs.setText(file[0])
            self.arquivoProfs = file[0]

        if self.pastaTurmas != "" and self.arquivoSalas != "" and self.arquivoDispoProfs != "" and self.arquivoProfs != "":
            self.ui.botaoEnsalamento.setEnabled(True)

    def popularFiltros(self, cursos, periodos, turmas, professores):
        filtros = {
            self.ui.filtroCurso: "Curso",
            self.ui.filtroCursoProf: "Curso",
            self.ui.filtroCursoSala: "Curso",
            self.ui.filtroPeriodo: "Período",
            self.ui.filtroPeriodoProf: "Período",
            self.ui.filtroPeriodoSala: "Período",
            self.ui.filtroTurma: "Turma",
            self.ui.filtroTurmaProf: "Turma",
            self.ui.filtroTurmaSala: "Turma",
            self.ui.filtroProfessor: "Professor"
            # Falta add filtroSala
        }

        for filtro, contexto in filtros.items():
            if contexto == "Curso":
                filtro.addItems(cursos)
            elif contexto == "Período":
                filtro.addItems(periodos)
            elif contexto == "Professor":
                filtro.addItems(professores)
            else:
                filtro.addItems(turmas)

    def popularTabela(self, grade):
        if grade == "C":
            tabela = self.ui.tabelaGrade
            valor_selecionado = self.ui.filtroTurma.currentText()
            if valor_selecionado == "Selecione uma turma":
                return
            else:
                grade_selecionada = self.turmas.get(valor_selecionado)
                self.ui.filtroTurma.removeItem(0)

        elif grade == "P":
            tabela = self.ui.tabelaGradeProfessor
            valor_selecionado = self.ui.filtroProfessor.currentText()
            if valor_selecionado == "Selecione um professor":
                return
            else:
                grade_selecionada = self.grade_professor.get(valor_selecionado)
                self.ui.filtroProfessor.removeItem(0)

        elif grade == "S":
            tabela = self.ui.tabelaGradeSala
            valor_selecionado = self.ui.filtroTurmaSala.currentText()
            grade_selecionada = self.turmas.get(valor_selecionado)

        tabela.setRowCount(0)

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

        tabela.verticalHeader().setVisible(False)

    def gerarEnsalamento(self):
        arquivo_dispo_prof = self.arquivoDispoProfs
        arquivo_salas = self.arquivoSalas
        arquivo_turmas = self.pastaTurmas
        arquivo_prof = self.arquivoProfs

        data, self.horarios = carrega_arquivos(arquivo_dispo_prof, arquivo_salas, arquivo_turmas, arquivo_prof, "2024/2")
        self.turmas, self.grade_professor = main(data, self.horarios)
        cursos = []
        periodos = []
        turmas = ["Selecione uma turma"]
        professores = ["Selecione um professor"]
        for id, value in data.turmas.items():
            if value.curso not in cursos and isinstance(value.curso, str):
                cursos.append(value.curso)
            if str(value.periodo) not in periodos and isinstance(value.periodo, float):
                periodos.append(str(value.periodo))
            if id not in turmas:
                turmas.append(id)

        for id, value in self.grade_professor.items():
            if id not in professores:
                professores.append(id)

        self.popularFiltros(cursos, periodos, turmas, professores)
        self.ui.botaoCurso.setEnabled(True)
        self.ui.botaoProf.setEnabled(True)
        self.ui.botaoSala.setEnabled(True)
        self.ui.botaoExportar.setEnabled(True)
        self.ui.menuCurso.setEnabled(True)
        self.ui.menuProf.setEnabled(True)
        self.ui.menuSala.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = Interface()
    janela.show()
    sys.exit(app.exec_())
