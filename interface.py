import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QProgressBar, QTableWidgetItem
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

        # Criando Timer para atualização da barra de progresso
        self.timer = QTimer(self.janela)
        self.timer.timeout.connect(self.atualizarProgresso)

        # Barra de progresso
        #self.ui.progressoEnsalamento.hide()

        # Botões
        #self.ui.botaoCurso.setEnabled(False)
        #self.ui.botaoProf.setEnabled(False)
        self.ui.pushButton.clicked.connect(self.abrirAbaHome)
        self.ui.botaoCurso.clicked.connect(self.abrirAbaCurso)
        self.ui.pushButton_2.clicked.connect(self.abrirAbaCurso)
        self.ui.botaoProf.clicked.connect(self.abrirAbaProf)
        self.ui.pushButton_3.clicked.connect(self.abrirAbaProf)
        self.ui.buscarTurma.clicked.connect(self.buscarArquivoTurmas)
        self.ui.buscarSala.clicked.connect(self.buscarArquivoSalas)
        self.ui.buscarProf.clicked.connect(self.buscarArquivoProfs)
        self.ui.botaoEnsalamento.clicked.connect(self.gerarEnsalamento)

        # Tabela
        larguraColuna = 139
        for coluna in range(self.ui.tabelaGrade.columnCount()):
            self.ui.tabelaGrade.setColumnWidth(coluna, larguraColuna)
            self.ui.tabelaGradeProfessor.setColumnWidth(coluna, larguraColuna)
            self.ui.tabelaGradeSala.setColumnWidth(coluna, larguraColuna)

    def show(self):
        self.janela.show()

    def abrirAbaHome(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

    def abrirAbaCurso(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.curso)

    def abrirAbaProf(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.professor)

    def buscarArquivoTurmas(self):
        file = QFileDialog.getOpenFileName(self.janela, 'Explorador de Arquivos', os.getcwd())
        self.ui.arquivoTurmas.setText(file[0])

    def buscarArquivoSalas(self):
        file = QFileDialog.getOpenFileName(self.janela, 'Explorador de Arquivos', os.getcwd())
        self.ui.arquivoSalas.setText(file[0])

    def buscarArquivoProfs(self):
        file = QFileDialog.getOpenFileName(self.janela, 'Explorador de Arquivos', os.getcwd())
        self.ui.arquivoProfs.setText(file[0])

    def atualizarProgresso(self):
        self.ui.progressoEnsalamento.setProperty("value", PROGRESSO)

        if PROGRESSO >= 100:
            self.timer.stop()

    def gerarEnsalamento(self):
        #self.ui.progressoEnsalamento.show()
        #self.timer.start(100)
        arquivo_dispo_prof = "../data/magister_asctimetables_2024-04-22-15-12-35_curitiba.xml"
        arquivo_salas = "../Data/Relatorio_dos_Espacos_de_Ensino 1.xlsx"
        arquivo_turmas = "../Data/politecnica/"
        arquivo_prof = "../Data/Planilha_Geral_Professores.xlsm"

        data, horarios = carrega_arquivos(arquivo_dispo_prof, arquivo_salas, arquivo_turmas, arquivo_prof, "2024/2")
        melhor_individuo, grade_professores = main(data, horarios)
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

        self.ui.filtroCurso.addItems(cursos)
        self.ui.filtroPeriodo.addItems(periodos)
        self.ui.filtroTurma.addItems(turmas)

        turma_selecionada = self.ui.filtroTurma.currentText()
        print(turma_selecionada)
        grade_selecionada = melhor_individuo.get(turma_selecionada)
        print(grade_selecionada)

        h_cnt = 0
        for i in range(len(grade_selecionada)):
            posicao_atual = self.ui.tabelaGrade.rowCount()
            self.ui.tabelaGrade.insertRow(posicao_atual)
            hora = horarios[h_cnt]
            intervalo = f"{hora['starttime']:2s} - {hora['endtime']:2s}"
            intervalo_atual = QTableWidgetItem(intervalo)
            self.ui.tabelaGrade.setItem(posicao_atual, 0, intervalo_atual)
            for j in range(len(grade_selecionada[i])):
                id = str(grade_selecionada[i][j]) if str(grade_selecionada[i][j]) != "None" else "-"
                id_atual = QTableWidgetItem(id)
                self.ui.tabelaGrade.setItem(posicao_atual, j+1, id_atual)
            h_cnt += 1
            

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = Interface()
    janela.show()
    sys.exit(app.exec_())