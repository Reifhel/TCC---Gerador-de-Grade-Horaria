import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog  , QProgressBar
from PyQt5.QtCore import QTimer
from ui_interface import Ui_MainWindow
from scheduler import main, PROGRESSO

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
        # self.ui.botaoHome.clicked.connect(self.abrirAbaHome)
        self.ui.botaoCurso.clicked.connect(self.abrirAbaCurso)
        # self.ui.botaoAbaCurso.clicked.connect(self.abrirAbaCurso)
        self.ui.botaoProf.clicked.connect(self.abrirAbaProf)
        # self.ui.botaoAbaProf.clicked.connect(self.abrirAbaProf)
        self.ui.buscarTurma.clicked.connect(self.buscarArquivoTurmas)
        self.ui.buscarSala.clicked.connect(self.buscarArquivoSalas)
        self.ui.buscarProf.clicked.connect(self.buscarArquivoProfs)
        self.ui.botaoEnsalamento.clicked.connect(self.gerarEnsalamento)

        # Tabela
        larguraColuna = 140
        for coluna in range(self.ui.tabelaGrade.columnCount()):
            self.ui.tabelaGrade.setColumnWidth(coluna, larguraColuna)

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
        self.timer.start(100)
        main()
        cursos = ["teste", "teste1", "teste2"]
        self.ui.filtroCurso.addItems(cursos)

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = Interface()
    janela.show()
    sys.exit(app.exec_())