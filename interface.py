import os
import re
import pandas as pd
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
from PyQt5.QtGui import QPixmap
from UI.ui_interface import Ui_MainWindow
from scheduler import carrega_arquivos, main


class WorkerThread(QThread):
    # Sinais para comunicar o status e dados da função complexa
    progress_signal = pyqtSignal(str)
    finished_signal = pyqtSignal(dict, dict, list)

    def __init__(self, arquivo_dispo_prof, arquivo_salas, arquivo_turmas, arquivo_prof):
        super().__init__()
        self.arquivo_dispo_prof = arquivo_dispo_prof
        self.arquivo_salas = arquivo_salas
        self.arquivo_turmas = arquivo_turmas
        self.arquivo_prof = arquivo_prof

    def run(self):
        # Executa a função de gerar ensalamento
        data, horarios = carrega_arquivos(self.arquivo_dispo_prof, self.arquivo_salas, self.arquivo_turmas, self.arquivo_prof, "2024/2")
        turmas, grade_professor = main(data, horarios)
        # Emite o sinal quando a função é finalizada
        self.finished_signal.emit(turmas, grade_professor, horarios)


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
        self.ui.botaoEnsalamento.clicked.connect(self.iniciarThreadEnsalamento)
        self.ui.aplicarFiltroTurma.clicked.connect(lambda _, grade="T": self.popularTabela(grade))
        self.ui.aplicarFiltroProf.clicked.connect(lambda _, grade="P": self.popularTabela(grade))
        self.ui.aplicarFiltroSala.clicked.connect(lambda _, grade="S": self.popularTabela(grade))

        # Exportar dados
        self.ui.botaoExportarGrade.clicked.connect(lambda _, contexto="T": self.exportarGradePrint(contexto))
        self.ui.botaoExportarGradeProf.clicked.connect(lambda _, contexto="P": self.exportarGradePrint(contexto))
        self.ui.botaoExportarGradeSala.clicked.connect(lambda _, contexto="S": self.exportarGradePrint(contexto))
        self.ui.botaoExportar.clicked.connect(self.exportarGrade)

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

    def iniciarThreadEnsalamento(self):
        # Desabilita o botão enquanto a função é executada
        self.ui.botaoEnsalamento.setEnabled(False)

        # Inicializa a thread com os arquivos selecionados
        self.worker = WorkerThread(self.arquivoDispoProfs, self.arquivoSalas, self.pastaTurmas, self.arquivoProfs)
        self.worker.progress_signal.connect(self.atualizarStatus)  # Se precisar de atualizações de status
        self.worker.finished_signal.connect(self.finalizarEnsalamento)
        self.worker.start()

    def finalizarEnsalamento(self, turmas, grade_professor, horarios):
        # Recebe os dados finalizados e popula os filtros
        self.turmas = turmas
        self.grade_professor = grade_professor
        self.horarios = horarios

        turmas_list = ["Selecione uma turma"]
        professores_list = ["Selecione um professor"]

        for id, _ in turmas.items():
            if id not in turmas_list:
                turmas_list.append(id)

        for id, _ in grade_professor.items():
            if id not in professores_list:
                professores_list.append(id)

        self.popularFiltros(turmas_list, professores_list)

        # Habilita os botões após a conclusão
        self.ui.botaoTurma.setEnabled(True)
        self.ui.botaoProf.setEnabled(True)
        self.ui.botaoSala.setEnabled(True)
        self.ui.botaoExportar.setEnabled(True)
        self.ui.menuTurma.setEnabled(True)
        self.ui.menuProf.setEnabled(True)
        self.ui.menuSala.setEnabled(True)
        self.ui.botaoEnsalamento.setEnabled(True)

    def atualizarStatus(self, mensagem):
        # Função opcional para atualizar status na interface
        pass

    def exportarGrade(self):
        dias = ['Segunda-feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sabádo']

        dados = []
        grades = self.turmas
        horarios = self.horarios

        for turma_id, grade in grades.items():
            for horario_idx, linha in enumerate(grade):
                hora = horarios[horario_idx]
                horario_inicio = hora['starttime']
                horario_fim = hora['endtime']  # Acessa o horário correspondente
                for dia_idx, disc in enumerate(linha):
                    if disc:  # Se houver uma aula nesse horário e dia
                        dados.append({
                            "turma": turma_id,
                            "curso": disc.curso,
                            "disciplina": disc.nome,
                            "professor": disc.professores,
                            "horario_inicio": horario_inicio,
                            "horario_fim": horario_fim,
                            "dia": dias[dia_idx]
                        })

        # Converte a lista de dados em um DataFrame
        df = pd.DataFrame(dados)
        output_dir = "./output"
        os.makedirs(output_dir, exist_ok=True)

        # Salva o DataFrame como um arquivo Excel dentro da pasta ./output
        output_path = os.path.join(output_dir, "grade_horaria_detalhada.xlsx")
        df.to_excel(output_path, index=False)

        # Salva o DataFrame como um arquivo Excel
        df.to_excel("./output/grade_horaria_detalhada.xlsx", index=False)

    def exportarGradePrint(self, contexto):
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
