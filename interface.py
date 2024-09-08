import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog  
from ui_interface import Ui_MainWindow

class Interface():
    def __init__(self) -> None:
        self.janela = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.janela)

        # Definindo aba principal
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        # Botões
        self.ui.botaoHome.clicked.connect(self.abrirAbaHome)
        self.ui.botaoCurso.clicked.connect(self.abrirAbaCurso)
        self.ui.botaoAbaCurso.clicked.connect(self.abrirAbaCurso)
        self.ui.botaoProf.clicked.connect(self.abrirAbaProf)
        self.ui.botaoAbaProf.clicked.connect(self.abrirAbaProf)
        self.ui.buscarTurma.clicked.connect(self.buscarArquivoTurmas)
        self.ui.buscarSala.clicked.connect(self.buscarArquivoSalas)
        self.ui.buscarProf.clicked.connect(self.buscarArquivoProfs)

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

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = Interface()
    janela.show()
    sys.exit(app.exec_())