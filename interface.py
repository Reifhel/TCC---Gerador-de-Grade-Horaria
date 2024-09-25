import sys
import os
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
from PyQt5.QtGui import QPixmap
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

        # Botões iniciais
        self.ui.botaoEnsalamento.setEnabled(False)
        self.ui.botaoTurma.setEnabled(False)
        self.ui.botaoProf.setEnabled(False)
        self.ui.botaoSala.setEnabled(False)
        self.ui.botaoExportar.setEnabled(False)
        self.ui.menuTurma.setEnabled(False)
        self.ui.menuProf.setEnabled(False)
        self.ui.menuSala.setEnabled(False)

        # Alternar abas
        self.ui.menuHome.clicked.connect(lambda _, aba=self.ui.home: self.abrirAba(aba))
        self.ui.botaoTurma.clicked.connect(lambda _, aba=self.ui.turma: self.abrirAba(aba))
        self.ui.menuTurma.clicked.connect(lambda _, aba=self.ui.turma: self.abrirAba(aba))
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
        self.ui.aplicarFiltroTurma.clicked.connect(lambda _, grade="T": self.popularTabela(grade))
        self.ui.aplicarFiltroProf.clicked.connect(lambda _, grade="P": self.popularTabela(grade))
        self.ui.aplicarFiltroSala.clicked.connect(lambda _, grade="S": self.popularTabela(grade))

        # Exportar dados
        #self.ui.botaoExportar.clicked.connect(lambda _, tabela=self.ui.tabelaGrade: self.exportarGrade(tabela))
        self.ui.botaoExportarGrade.clicked.connect(lambda _, contexto="T": self.exportarGrade(contexto))
        self.ui.botaoExportarGradeProf.clicked.connect(lambda _, contexto="P": self.exportarGrade(contexto))
        self.ui.botaoExportarGradeSala.clicked.connect(lambda _, contexto="S": self.exportarGrade(contexto))

        # Estrutura padrão da tabela
        larguraColuna = 136
        nColunas = 7
        for coluna in range(nColunas):
            self.ui.tabelaGrade.setColumnWidth(coluna, larguraColuna)
            self.ui.tabelaGradeProfessor.setColumnWidth(coluna, larguraColuna)
            self.ui.tabelaGradeSala.setColumnWidth(coluna, larguraColuna)


    def show(self):
        self.janela.show()


    def abrirAba(self, aba):
        self.ui.stackedWidget.setCurrentWidget(aba)


    def exportarGrade(self, contexto):
        if contexto == "T":
            tabela = self.ui.tabelaGrade
            nome_arquivo = self.ui.filtroTurma.currentText()
        elif contexto == "P":
            tabela = self.ui.tabelaGradeProfessor
            nome_arquivo = self.ui.filtroProfessor.currentText()
        elif contexto == "S":
            tabela = self.ui.tabelaGradeSala
            nome_arquivo = self.ui.filtroSala.currentText()

        nome_arquivo = re.sub(r'[\/:*?"<>|]', '_', nome_arquivo)
        output_dir = "./output/"
        os.makedirs(output_dir, exist_ok=True)
        pixmap = QPixmap(tabela.size())
        tabela.render(pixmap)

        caminho = os.path.join(output_dir, f"{nome_arquivo}.png")
        pixmap.save(caminho)



    def buscarArquivo(self, botao):
        if botao == "T":
            file = QFileDialog.getExistingDirectory(self.janela, 'Explorador de Arquivos', os.getcwd())
            if file != "":
                self.ui.pastaTurmas.setText(file)
                self.pastaTurmas = file
        elif botao == "S":
            file = QFileDialog.getOpenFileName(self.janela, 'Explorador de Arquivos', os.getcwd())
            if file != "":
                self.ui.arquivoSalas.setText(file[0])
                self.arquivoSalas = file[0]
        elif botao == "DP":
            file = QFileDialog.getOpenFileName(self.janela, 'Explorador de Arquivos', os.getcwd())
            if file != "":
                self.ui.arquivoDispoProfs.setText(file[0])
                self.arquivoDispoProfs = file[0]
        else:
            file = QFileDialog.getOpenFileName(self.janela, 'Explorador de Arquivos', os.getcwd())
            if file != "":
                self.ui.arquivoProfs.setText(file[0])
                self.arquivoProfs = file[0]

        if self.pastaTurmas != "" and self.arquivoSalas != "" and self.arquivoDispoProfs != "" and self.arquivoProfs != "":
            self.ui.botaoEnsalamento.setEnabled(True)


    def popularFiltros(self, turmas, professores):
        filtros = {
            self.ui.filtroTurma: "Turma",
            self.ui.filtroProfessor: "Professor",
            self.ui.filtroSala: "Sala"
        }

        for filtro, contexto in filtros.items():
            if contexto == "Turma":
                filtro.addItems(turmas)
            elif contexto == "Professor":
                filtro.addItems(professores)
            elif contexto == "Sala":
                pass


    def popularTabela(self, grade):
        if grade == "T":
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
        turmas = ["Selecione uma turma"]
        professores = ["Selecione um professor"]
        for id, _ in data.turmas.items():
            if id not in turmas:
                turmas.append(id)

        for id, _ in self.grade_professor.items():
            if id not in professores:
                professores.append(id)

        self.popularFiltros(turmas, professores)
        self.ui.botaoTurma.setEnabled(True)
        self.ui.botaoProf.setEnabled(True)
        self.ui.botaoSala.setEnabled(True)
        self.ui.botaoExportar.setEnabled(True)
        self.ui.menuTurma.setEnabled(True)
        self.ui.menuProf.setEnabled(True)
        self.ui.menuSala.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = Interface()
    janela.show()
    sys.exit(app.exec_())
