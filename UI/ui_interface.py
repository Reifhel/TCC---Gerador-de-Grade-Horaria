# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1000, 800)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 10, 1001, 751))
        self.stackedWidget.setObjectName("stackedWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.retangulo = QtWidgets.QFrame(self.home)
        self.retangulo.setGeometry(QtCore.QRect(40, 160, 641, 451))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.retangulo.setFont(font)
        self.retangulo.setStyleSheet("border: 1px solid black;\n"
                                     "background-color: rgb(255, 255, 255);")
        self.retangulo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.retangulo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.retangulo.setLineWidth(1)
        self.retangulo.setMidLineWidth(0)
        self.retangulo.setObjectName("retangulo")
        self.pastaTurmas = QtWidgets.QLabel(self.retangulo)
        self.pastaTurmas.setGeometry(QtCore.QRect(50, 30, 371, 51))
        self.pastaTurmas.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.pastaTurmas.setWordWrap(True)
        self.pastaTurmas.setObjectName("pastaTurmas")
        self.arquivoSalas = QtWidgets.QLabel(self.retangulo)
        self.arquivoSalas.setGeometry(QtCore.QRect(50, 140, 371, 51))
        self.arquivoSalas.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.arquivoSalas.setWordWrap(True)
        self.arquivoSalas.setObjectName("arquivoSalas")
        self.arquivoDispoProfs = QtWidgets.QLabel(self.retangulo)
        self.arquivoDispoProfs.setGeometry(QtCore.QRect(50, 250, 371, 51))
        self.arquivoDispoProfs.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.arquivoDispoProfs.setWordWrap(True)
        self.arquivoDispoProfs.setObjectName("arquivoDispoProfs")
        self.buscarTurma = QtWidgets.QPushButton(self.retangulo)
        self.buscarTurma.setGeometry(QtCore.QRect(440, 30, 141, 51))
        self.buscarTurma.setStyleSheet("background-color: rgb(150, 15, 47);\n"
                                       "color: rgb(255, 255, 255);")
        self.buscarTurma.setObjectName("buscarTurma")
        self.buscarSala = QtWidgets.QPushButton(self.retangulo)
        self.buscarSala.setGeometry(QtCore.QRect(440, 140, 141, 51))
        self.buscarSala.setStyleSheet("background-color: rgb(150, 15, 47);\n"
                                      "color: rgb(255, 255, 255);")
        self.buscarSala.setObjectName("buscarSala")
        self.buscarDispoProf = QtWidgets.QPushButton(self.retangulo)
        self.buscarDispoProf.setGeometry(QtCore.QRect(440, 250, 141, 51))
        self.buscarDispoProf.setStyleSheet("background-color: rgb(150, 15, 47);\n"
                                           "color: rgb(255, 255, 255);")
        self.buscarDispoProf.setObjectName("buscarDispoProf")
        self.buscarProf = QtWidgets.QPushButton(self.retangulo)
        self.buscarProf.setGeometry(QtCore.QRect(440, 360, 141, 51))
        self.buscarProf.setStyleSheet("background-color: rgb(150, 15, 47);\n"
                                      "color: rgb(255, 255, 255);")
        self.buscarProf.setObjectName("buscarProf")
        self.arquivoProfs = QtWidgets.QLabel(self.retangulo)
        self.arquivoProfs.setGeometry(QtCore.QRect(50, 360, 371, 51))
        self.arquivoProfs.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.arquivoProfs.setWordWrap(True)
        self.arquivoProfs.setObjectName("arquivoProfs")
        self.botaoExportar = QtWidgets.QPushButton(self.home)
        self.botaoExportar.setGeometry(QtCore.QRect(750, 560, 151, 51))
        self.botaoExportar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.botaoExportar.setObjectName("botaoExportar")
        self.botaoTurma = QtWidgets.QPushButton(self.home)
        self.botaoTurma.setGeometry(QtCore.QRect(750, 260, 151, 51))
        self.botaoTurma.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.botaoTurma.setObjectName("botaoTurma")
        self.botaoProf = QtWidgets.QPushButton(self.home)
        self.botaoProf.setGeometry(QtCore.QRect(750, 360, 151, 51))
        self.botaoProf.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.botaoProf.setObjectName("botaoProf")
        self.botaoEnsalamento = QtWidgets.QPushButton(self.home)
        self.botaoEnsalamento.setGeometry(QtCore.QRect(750, 160, 151, 51))
        self.botaoEnsalamento.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.botaoEnsalamento.setObjectName("botaoEnsalamento")
        self.tituloHome = QtWidgets.QLabel(self.home)
        self.tituloHome.setGeometry(QtCore.QRect(310, 10, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tituloHome.setFont(font)
        self.tituloHome.setAlignment(QtCore.Qt.AlignCenter)
        self.tituloHome.setObjectName("tituloHome")
        self.botaoSala = QtWidgets.QPushButton(self.home)
        self.botaoSala.setGeometry(QtCore.QRect(750, 460, 151, 51))
        self.botaoSala.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.botaoSala.setObjectName("botaoSala")
        self.stackedWidget.addWidget(self.home)
        self.turma = QtWidgets.QWidget()
        self.turma.setObjectName("turma")
        self.filtroTurma = QtWidgets.QComboBox(self.turma)
        self.filtroTurma.setGeometry(QtCore.QRect(10, 60, 371, 21))
        self.filtroTurma.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filtroTurma.setObjectName("filtroTurma")
        self.labelTurma = QtWidgets.QLabel(self.turma)
        self.labelTurma.setGeometry(QtCore.QRect(10, 40, 161, 20))
        self.labelTurma.setObjectName("labelTurma")
        self.tabelaGrade = QtWidgets.QTableWidget(self.turma)
        self.tabelaGrade.setGeometry(QtCore.QRect(10, 100, 981, 631))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabelaGrade.sizePolicy().hasHeightForWidth())
        self.tabelaGrade.setSizePolicy(sizePolicy)
        self.tabelaGrade.setSizeIncrement(QtCore.QSize(0, 0))
        self.tabelaGrade.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tabelaGrade.setAlternatingRowColors(False)
        self.tabelaGrade.setObjectName("tabelaGrade")
        self.tabelaGrade.setColumnCount(7)
        self.tabelaGrade.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaGrade.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaGrade.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaGrade.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaGrade.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaGrade.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaGrade.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaGrade.setHorizontalHeaderItem(6, item)
        self.tabelaGrade.verticalHeader().setDefaultSectionSize(30)
        self.tabelaGrade.verticalHeader().setStretchLastSection(False)
        self.botaoExportarGrade = QtWidgets.QPushButton(self.turma)
        self.botaoExportarGrade.setGeometry(QtCore.QRect(500, 60, 111, 21))
        self.botaoExportarGrade.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.botaoExportarGrade.setObjectName("botaoExportarGrade")
        self.tituloAbaTurma = QtWidgets.QLabel(self.turma)
        self.tituloAbaTurma.setGeometry(QtCore.QRect(300, 10, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tituloAbaTurma.setFont(font)
        self.tituloAbaTurma.setAlignment(QtCore.Qt.AlignCenter)
        self.tituloAbaTurma.setObjectName("tituloAbaTurma")
        self.aplicarFiltroTurma = QtWidgets.QPushButton(self.turma)
        self.aplicarFiltroTurma.setGeometry(QtCore.QRect(390, 60, 101, 21))
        self.aplicarFiltroTurma.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.aplicarFiltroTurma.setObjectName("aplicarFiltroTurma")
        self.stackedWidget.addWidget(self.turma)
        self.professor = QtWidgets.QWidget()
        self.professor.setObjectName("professor")
        self.tabelaGradeProfessor = QtWidgets.QTableWidget(self.professor)
        self.tabelaGradeProfessor.setGeometry(QtCore.QRect(10, 100, 981, 631))
        self.tabelaGradeProfessor.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tabelaGradeProfessor.setAlternatingRowColors(False)
        self.tabelaGradeProfessor.setObjectName("tabelaGradeProfessor")
        self.tabelaGradeProfessor.setColumnCount(7)
        self.tabelaGradeProfessor.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaGradeProfessor.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaGradeProfessor.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaGradeProfessor.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaGradeProfessor.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaGradeProfessor.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaGradeProfessor.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaGradeProfessor.setHorizontalHeaderItem(6, item)
        self.tabelaGradeProfessor.verticalHeader().setDefaultSectionSize(30)
        self.tabelaGradeProfessor.verticalHeader().setStretchLastSection(False)
        self.labelProfessor = QtWidgets.QLabel(self.professor)
        self.labelProfessor.setGeometry(QtCore.QRect(10, 40, 161, 20))
        self.labelProfessor.setObjectName("labelProfessor")
        self.botaoExportarGradeProf = QtWidgets.QPushButton(self.professor)
        self.botaoExportarGradeProf.setGeometry(QtCore.QRect(500, 60, 111, 21))
        self.botaoExportarGradeProf.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.botaoExportarGradeProf.setObjectName("botaoExportarGradeProf")
        self.filtroProfessor = QtWidgets.QComboBox(self.professor)
        self.filtroProfessor.setGeometry(QtCore.QRect(10, 60, 371, 21))
        self.filtroProfessor.setAutoFillBackground(False)
        self.filtroProfessor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filtroProfessor.setObjectName("filtroProfessor")
        self.tituloAbaProf = QtWidgets.QLabel(self.professor)
        self.tituloAbaProf.setGeometry(QtCore.QRect(300, 10, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tituloAbaProf.setFont(font)
        self.tituloAbaProf.setAlignment(QtCore.Qt.AlignCenter)
        self.tituloAbaProf.setObjectName("tituloAbaProf")
        self.aplicarFiltroProf = QtWidgets.QPushButton(self.professor)
        self.aplicarFiltroProf.setGeometry(QtCore.QRect(390, 60, 101, 21))
        self.aplicarFiltroProf.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.aplicarFiltroProf.setObjectName("aplicarFiltroProf")
        self.stackedWidget.addWidget(self.professor)
        self.salas = QtWidgets.QWidget()
        self.salas.setObjectName("salas")
        self.filtroSala = QtWidgets.QComboBox(self.salas)
        self.filtroSala.setGeometry(QtCore.QRect(10, 60, 371, 21))
        self.filtroSala.setAutoFillBackground(False)
        self.filtroSala.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filtroSala.setObjectName("filtroSala")
        self.botaoExportarGradeSala = QtWidgets.QPushButton(self.salas)
        self.botaoExportarGradeSala.setGeometry(QtCore.QRect(500, 60, 111, 21))
        self.botaoExportarGradeSala.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.botaoExportarGradeSala.setObjectName("botaoExportarGradeSala")
        self.labelSala = QtWidgets.QLabel(self.salas)
        self.labelSala.setGeometry(QtCore.QRect(10, 40, 161, 20))
        self.labelSala.setObjectName("labelSala")
        self.tabelaGradeSala = QtWidgets.QTableWidget(self.salas)
        self.tabelaGradeSala.setGeometry(QtCore.QRect(10, 100, 981, 631))
        self.tabelaGradeSala.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tabelaGradeSala.setAlternatingRowColors(False)
        self.tabelaGradeSala.setObjectName("tabelaGradeSala")
        self.tabelaGradeSala.setColumnCount(7)
        self.tabelaGradeSala.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaGradeSala.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaGradeSala.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaGradeSala.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaGradeSala.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaGradeSala.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaGradeSala.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaGradeSala.setHorizontalHeaderItem(6, item)
        self.tabelaGradeSala.verticalHeader().setDefaultSectionSize(30)
        self.tabelaGradeSala.verticalHeader().setStretchLastSection(False)
        self.tituloAbaSala = QtWidgets.QLabel(self.salas)
        self.tituloAbaSala.setGeometry(QtCore.QRect(300, 10, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tituloAbaSala.setFont(font)
        self.tituloAbaSala.setAlignment(QtCore.Qt.AlignCenter)
        self.tituloAbaSala.setObjectName("tituloAbaSala")
        self.aplicarFiltroSala = QtWidgets.QPushButton(self.salas)
        self.aplicarFiltroSala.setGeometry(QtCore.QRect(390, 60, 101, 21))
        self.aplicarFiltroSala.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.aplicarFiltroSala.setObjectName("aplicarFiltroSala")
        self.stackedWidget.addWidget(self.salas)
        self.menuHome = QtWidgets.QPushButton(self.centralwidget)
        self.menuHome.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.menuHome.setAutoFillBackground(False)
        self.menuHome.setStyleSheet("background-color: white;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./input/img/casa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuHome.setIcon(icon)
        self.menuHome.setObjectName("menuHome")
        self.menuProf = QtWidgets.QPushButton(self.centralwidget)
        self.menuProf.setGeometry(QtCore.QRect(60, 0, 31, 31))
        self.menuProf.setStyleSheet("background-color: white;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./input/img/homem.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuProf.setIcon(icon1)
        self.menuProf.setObjectName("menuProf")
        self.menuSala = QtWidgets.QPushButton(self.centralwidget)
        self.menuSala.setGeometry(QtCore.QRect(90, 0, 31, 31))
        self.menuSala.setStyleSheet("background-color: white;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./input/img/cadeira-de-escritorio.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuSala.setIcon(icon2)
        self.menuSala.setObjectName("menuSala")
        self.menuTurma = QtWidgets.QPushButton(self.centralwidget)
        self.menuTurma.setGeometry(QtCore.QRect(30, 0, 31, 31))
        self.menuTurma.setStyleSheet("background-color: white;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./input/img/livro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuTurma.setIcon(icon3)
        self.menuTurma.setObjectName("menuTurma")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pastaTurmas.setText(_translate("MainWindow", "Selecione a pasta com os arquivos de turmas:"))
        self.arquivoSalas.setText(_translate("MainWindow", "Selecione o arquivo de salas:"))
        self.arquivoDispoProfs.setText(_translate("MainWindow", "Selecione o arquivo de disponibilidade de horários dos professores:"))
        self.buscarTurma.setText(_translate("MainWindow", "Buscar"))
        self.buscarSala.setText(_translate("MainWindow", "Buscar"))
        self.buscarDispoProf.setText(_translate("MainWindow", "Buscar"))
        self.buscarProf.setText(_translate("MainWindow", "Buscar"))
        self.arquivoProfs.setText(_translate("MainWindow", "Selecione o arquivo de dados dos professores:"))
        self.botaoExportar.setText(_translate("MainWindow", "Exportar"))
        self.botaoTurma.setText(_translate("MainWindow", "Verificar Turma"))
        self.botaoProf.setText(_translate("MainWindow", "Verificar Professor"))
        self.botaoEnsalamento.setText(_translate("MainWindow", "Gerar Ensalamento"))
        self.tituloHome.setText(_translate("MainWindow", "Gerador de Ensalamento"))
        self.botaoSala.setText(_translate("MainWindow", "Verificar Sala"))
        self.labelTurma.setText(_translate("MainWindow", "Turma"))
        item = self.tabelaGrade.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Horário"))
        item = self.tabelaGrade.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Segunda-feira"))
        item = self.tabelaGrade.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Terça-feira"))
        item = self.tabelaGrade.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quarta-feira"))
        item = self.tabelaGrade.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Quinta-feira"))
        item = self.tabelaGrade.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Sexta-feira"))
        item = self.tabelaGrade.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Sábado"))
        self.botaoExportarGrade.setText(_translate("MainWindow", "Exportar Grade"))
        self.tituloAbaTurma.setText(_translate("MainWindow", "Visão por Turma"))
        self.aplicarFiltroTurma.setText(_translate("MainWindow", "Aplicar Filtro"))
        item = self.tabelaGradeProfessor.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Horário"))
        item = self.tabelaGradeProfessor.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Segunda-feira"))
        item = self.tabelaGradeProfessor.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Terça-feira"))
        item = self.tabelaGradeProfessor.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quarta-feira"))
        item = self.tabelaGradeProfessor.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Quinta-feira"))
        item = self.tabelaGradeProfessor.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Sexta-feira"))
        item = self.tabelaGradeProfessor.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Sábado"))
        self.labelProfessor.setText(_translate("MainWindow", "Professor"))
        self.botaoExportarGradeProf.setText(_translate("MainWindow", "Exportar Grade"))
        self.tituloAbaProf.setText(_translate("MainWindow", "Visão por Professor"))
        self.aplicarFiltroProf.setText(_translate("MainWindow", "Aplicar Filtro"))
        self.botaoExportarGradeSala.setText(_translate("MainWindow", "Exportar Grade"))
        self.labelSala.setText(_translate("MainWindow", "Sala"))
        item = self.tabelaGradeSala.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Horário"))
        item = self.tabelaGradeSala.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Segunda-feira"))
        item = self.tabelaGradeSala.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Terça-feira"))
        item = self.tabelaGradeSala.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quarta-feira"))
        item = self.tabelaGradeSala.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Quinta-feira"))
        item = self.tabelaGradeSala.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Sexta-feira"))
        item = self.tabelaGradeSala.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Sábado"))
        self.tituloAbaSala.setText(_translate("MainWindow", "Visão por Sala"))
        self.aplicarFiltroSala.setText(_translate("MainWindow", "Aplicar Filtro"))
