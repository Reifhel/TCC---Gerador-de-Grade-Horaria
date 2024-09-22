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
        MainWindow.resize(1000, 800)
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
        self.arquivoTurmas = QtWidgets.QLabel(self.retangulo)
        self.arquivoTurmas.setGeometry(QtCore.QRect(50, 50, 371, 51))
        self.arquivoTurmas.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.arquivoTurmas.setObjectName("arquivoTurmas")
        self.arquivoSalas = QtWidgets.QLabel(self.retangulo)
        self.arquivoSalas.setGeometry(QtCore.QRect(50, 190, 371, 51))
        self.arquivoSalas.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.arquivoSalas.setObjectName("arquivoSalas")
        self.arquivoProfs = QtWidgets.QLabel(self.retangulo)
        self.arquivoProfs.setGeometry(QtCore.QRect(50, 330, 371, 51))
        self.arquivoProfs.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.arquivoProfs.setObjectName("arquivoProfs")
        self.buscarTurma = QtWidgets.QPushButton(self.retangulo)
        self.buscarTurma.setGeometry(QtCore.QRect(440, 50, 141, 51))
        self.buscarTurma.setStyleSheet("background-color: rgb(150, 15, 47);\n"
"color: rgb(255, 255, 255);")
        self.buscarTurma.setObjectName("buscarTurma")
        self.buscarSala = QtWidgets.QPushButton(self.retangulo)
        self.buscarSala.setGeometry(QtCore.QRect(440, 190, 141, 51))
        self.buscarSala.setStyleSheet("background-color: rgb(150, 15, 47);\n"
"color: rgb(255, 255, 255);")
        self.buscarSala.setObjectName("buscarSala")
        self.buscarProf = QtWidgets.QPushButton(self.retangulo)
        self.buscarProf.setGeometry(QtCore.QRect(440, 330, 141, 51))
        self.buscarProf.setStyleSheet("background-color: rgb(150, 15, 47);\n"
"color: rgb(255, 255, 255);")
        self.buscarProf.setObjectName("buscarProf")
        self.botaoExportar = QtWidgets.QPushButton(self.home)
        self.botaoExportar.setGeometry(QtCore.QRect(750, 560, 151, 51))
        self.botaoExportar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.botaoExportar.setObjectName("botaoExportar")
        self.botaoCurso = QtWidgets.QPushButton(self.home)
        self.botaoCurso.setGeometry(QtCore.QRect(750, 260, 151, 51))
        self.botaoCurso.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.botaoCurso.setObjectName("botaoCurso")
        self.botaoProf = QtWidgets.QPushButton(self.home)
        self.botaoProf.setGeometry(QtCore.QRect(750, 360, 151, 51))
        self.botaoProf.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.botaoProf.setObjectName("botaoProf")
        self.botaoEnsalamento = QtWidgets.QPushButton(self.home)
        self.botaoEnsalamento.setGeometry(QtCore.QRect(750, 160, 151, 51))
        self.botaoEnsalamento.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.botaoEnsalamento.setObjectName("botaoEnsalamento")
        self.tituloHome = QtWidgets.QLabel(self.home)
        self.tituloHome.setGeometry(QtCore.QRect(299, 20, 411, 80))
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
        self.curso = QtWidgets.QWidget()
        self.curso.setObjectName("curso")
        self.filtroCurso = QtWidgets.QComboBox(self.curso)
        self.filtroCurso.setGeometry(QtCore.QRect(10, 60, 311, 21))
        self.filtroCurso.setAutoFillBackground(False)
        self.filtroCurso.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filtroCurso.setObjectName("filtroCurso")
        self.filtroPeriodo = QtWidgets.QComboBox(self.curso)
        self.filtroPeriodo.setGeometry(QtCore.QRect(330, 60, 221, 21))
        self.filtroPeriodo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filtroPeriodo.setObjectName("filtroPeriodo")
        self.filtroTurma = QtWidgets.QComboBox(self.curso)
        self.filtroTurma.setGeometry(QtCore.QRect(570, 60, 311, 21))
        self.filtroTurma.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filtroTurma.setObjectName("filtroTurma")
        self.labelCurso = QtWidgets.QLabel(self.curso)
        self.labelCurso.setGeometry(QtCore.QRect(10, 40, 161, 20))
        self.labelCurso.setObjectName("labelCurso")
        self.labelPeriodo = QtWidgets.QLabel(self.curso)
        self.labelPeriodo.setGeometry(QtCore.QRect(330, 40, 161, 20))
        self.labelPeriodo.setObjectName("labelPeriodo")
        self.labelTurma = QtWidgets.QLabel(self.curso)
        self.labelTurma.setGeometry(QtCore.QRect(570, 40, 161, 20))
        self.labelTurma.setObjectName("labelTurma")
        self.tabelaGrade = QtWidgets.QTableWidget(self.curso)
        self.tabelaGrade.setGeometry(QtCore.QRect(10, 110, 981, 551))
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
        self.botaoExportarGrade = QtWidgets.QPushButton(self.curso)
        self.botaoExportarGrade.setGeometry(QtCore.QRect(420, 680, 151, 51))
        self.botaoExportarGrade.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.botaoExportarGrade.setObjectName("botaoExportarGrade")
        self.tituloAbaCurso = QtWidgets.QLabel(self.curso)
        self.tituloAbaCurso.setGeometry(QtCore.QRect(300, 10, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tituloAbaCurso.setFont(font)
        self.tituloAbaCurso.setAlignment(QtCore.Qt.AlignCenter)
        self.tituloAbaCurso.setObjectName("tituloAbaCurso")
        self.aplicarFiltrosCurso = QtWidgets.QPushButton(self.curso)
        self.aplicarFiltrosCurso.setGeometry(QtCore.QRect(890, 60, 101, 21))
        self.aplicarFiltrosCurso.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.aplicarFiltrosCurso.setObjectName("aplicarFiltrosCurso")
        self.stackedWidget.addWidget(self.curso)
        self.professor = QtWidgets.QWidget()
        self.professor.setObjectName("professor")
        self.tabelaGradeProfessor = QtWidgets.QTableWidget(self.professor)
        self.tabelaGradeProfessor.setGeometry(QtCore.QRect(10, 110, 981, 551))
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
        self.botaoExportarGradeProf.setGeometry(QtCore.QRect(420, 680, 151, 51))
        self.botaoExportarGradeProf.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.botaoExportarGradeProf.setObjectName("botaoExportarGradeProf")
        self.labelTurmaProf = QtWidgets.QLabel(self.professor)
        self.labelTurmaProf.setGeometry(QtCore.QRect(660, 40, 161, 20))
        self.labelTurmaProf.setObjectName("labelTurmaProf")
        self.filtroTurmaProf = QtWidgets.QComboBox(self.professor)
        self.filtroTurmaProf.setGeometry(QtCore.QRect(660, 60, 221, 21))
        self.filtroTurmaProf.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filtroTurmaProf.setObjectName("filtroTurmaProf")
        self.labelPeriodoProf = QtWidgets.QLabel(self.professor)
        self.labelPeriodoProf.setGeometry(QtCore.QRect(510, 40, 161, 20))
        self.labelPeriodoProf.setObjectName("labelPeriodoProf")
        self.filtroPeriodoProf = QtWidgets.QComboBox(self.professor)
        self.filtroPeriodoProf.setGeometry(QtCore.QRect(510, 60, 141, 21))
        self.filtroPeriodoProf.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filtroPeriodoProf.setObjectName("filtroPeriodoProf")
        self.filtroCursoProf = QtWidgets.QComboBox(self.professor)
        self.filtroCursoProf.setGeometry(QtCore.QRect(280, 60, 221, 21))
        self.filtroCursoProf.setAutoFillBackground(False)
        self.filtroCursoProf.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filtroCursoProf.setObjectName("filtroCursoProf")
        self.labelCursoProf = QtWidgets.QLabel(self.professor)
        self.labelCursoProf.setGeometry(QtCore.QRect(280, 40, 161, 20))
        self.labelCursoProf.setObjectName("labelCursoProf")
        self.filtroProfessor = QtWidgets.QComboBox(self.professor)
        self.filtroProfessor.setGeometry(QtCore.QRect(10, 60, 261, 21))
        self.filtroProfessor.setAutoFillBackground(False)
        self.filtroProfessor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filtroProfessor.setObjectName("filtroProfessor")
        self.tituloAbaProf = QtWidgets.QLabel(self.professor)
        self.tituloAbaProf.setGeometry(QtCore.QRect(300, 10, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tituloAbaProf.setFont(font)
        self.tituloAbaProf.setAlignment(QtCore.Qt.AlignCenter)
        self.tituloAbaProf.setObjectName("tituloAbaProf")
        self.aplicarFiltrosProf = QtWidgets.QPushButton(self.professor)
        self.aplicarFiltrosProf.setGeometry(QtCore.QRect(890, 60, 101, 21))
        self.aplicarFiltrosProf.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.aplicarFiltrosProf.setObjectName("aplicarFiltrosProf")
        self.stackedWidget.addWidget(self.professor)
        self.salas = QtWidgets.QWidget()
        self.salas.setObjectName("salas")
        self.filtroTurmaSala = QtWidgets.QComboBox(self.salas)
        self.filtroTurmaSala.setGeometry(QtCore.QRect(660, 60, 221, 21))
        self.filtroTurmaSala.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filtroTurmaSala.setObjectName("filtroTurmaSala")
        self.filtroSala = QtWidgets.QComboBox(self.salas)
        self.filtroSala.setGeometry(QtCore.QRect(10, 60, 231, 21))
        self.filtroSala.setAutoFillBackground(False)
        self.filtroSala.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filtroSala.setObjectName("filtroSala")
        self.filtroPeriodoSala = QtWidgets.QComboBox(self.salas)
        self.filtroPeriodoSala.setGeometry(QtCore.QRect(480, 60, 171, 21))
        self.filtroPeriodoSala.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filtroPeriodoSala.setObjectName("filtroPeriodoSala")
        self.labelCursoSala = QtWidgets.QLabel(self.salas)
        self.labelCursoSala.setGeometry(QtCore.QRect(250, 40, 161, 20))
        self.labelCursoSala.setObjectName("labelCursoSala")
        self.botaoExportarGradeSala = QtWidgets.QPushButton(self.salas)
        self.botaoExportarGradeSala.setGeometry(QtCore.QRect(420, 680, 151, 51))
        self.botaoExportarGradeSala.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.botaoExportarGradeSala.setObjectName("botaoExportarGradeSala")
        self.labelPeriodoSala = QtWidgets.QLabel(self.salas)
        self.labelPeriodoSala.setGeometry(QtCore.QRect(480, 40, 161, 20))
        self.labelPeriodoSala.setObjectName("labelPeriodoSala")
        self.labelSala = QtWidgets.QLabel(self.salas)
        self.labelSala.setGeometry(QtCore.QRect(10, 40, 161, 20))
        self.labelSala.setObjectName("labelSala")
        self.tabelaGradeSala = QtWidgets.QTableWidget(self.salas)
        self.tabelaGradeSala.setGeometry(QtCore.QRect(10, 110, 981, 551))
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
        self.filtroCursoSala = QtWidgets.QComboBox(self.salas)
        self.filtroCursoSala.setGeometry(QtCore.QRect(250, 60, 221, 21))
        self.filtroCursoSala.setAutoFillBackground(False)
        self.filtroCursoSala.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filtroCursoSala.setObjectName("filtroCursoSala")
        self.labelTurmaSala = QtWidgets.QLabel(self.salas)
        self.labelTurmaSala.setGeometry(QtCore.QRect(660, 40, 161, 20))
        self.labelTurmaSala.setObjectName("labelTurmaSala")
        self.tituloAbaSala = QtWidgets.QLabel(self.salas)
        self.tituloAbaSala.setGeometry(QtCore.QRect(290, 10, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tituloAbaSala.setFont(font)
        self.tituloAbaSala.setAlignment(QtCore.Qt.AlignCenter)
        self.tituloAbaSala.setObjectName("tituloAbaSala")
        self.aplicarFiltrosSala = QtWidgets.QPushButton(self.salas)
        self.aplicarFiltrosSala.setGeometry(QtCore.QRect(890, 60, 101, 21))
        self.aplicarFiltrosSala.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.aplicarFiltrosSala.setObjectName("aplicarFiltrosSala")
        self.stackedWidget.addWidget(self.salas)
        self.menuHome = QtWidgets.QPushButton(self.centralwidget)
        self.menuHome.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.menuHome.setAutoFillBackground(False)
        self.menuHome.setStyleSheet("background-color: white;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Downloads/casa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuHome.setIcon(icon)
        self.menuHome.setObjectName("menuHome")
        self.menuProf = QtWidgets.QPushButton(self.centralwidget)
        self.menuProf.setGeometry(QtCore.QRect(60, 0, 31, 31))
        self.menuProf.setStyleSheet("background-color: white;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../Downloads/homem.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuProf.setIcon(icon1)
        self.menuProf.setObjectName("menuProf")
        self.menuSala = QtWidgets.QPushButton(self.centralwidget)
        self.menuSala.setGeometry(QtCore.QRect(90, 0, 31, 31))
        self.menuSala.setStyleSheet("background-color: white;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../Downloads/cadeira-de-escritorio.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuSala.setIcon(icon2)
        self.menuSala.setObjectName("menuSala")
        self.menuCurso = QtWidgets.QPushButton(self.centralwidget)
        self.menuCurso.setGeometry(QtCore.QRect(30, 0, 31, 31))
        self.menuCurso.setStyleSheet("background-color: white;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../Downloads/livro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuCurso.setIcon(icon3)
        self.menuCurso.setObjectName("menuCurso")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.arquivoTurmas.setText(_translate("MainWindow", "Selecione o arquivo de turmas:"))
        self.arquivoSalas.setText(_translate("MainWindow", "Selecione o arquivo de salas:"))
        self.arquivoProfs.setText(_translate("MainWindow", "Selecione o arquivo de horário dos professores:"))
        self.buscarTurma.setText(_translate("MainWindow", "Buscar"))
        self.buscarSala.setText(_translate("MainWindow", "Buscar"))
        self.buscarProf.setText(_translate("MainWindow", "Buscar"))
        self.botaoExportar.setText(_translate("MainWindow", "Exportar"))
        self.botaoCurso.setText(_translate("MainWindow", "Verificar Curso"))
        self.botaoProf.setText(_translate("MainWindow", "Verificar Professor"))
        self.botaoEnsalamento.setText(_translate("MainWindow", "Gerar Ensalamento"))
        self.tituloHome.setText(_translate("MainWindow", "Gerador de Ensalamento"))
        self.botaoSala.setText(_translate("MainWindow", "Verificar Sala"))
        self.labelCurso.setText(_translate("MainWindow", "Curso"))
        self.labelPeriodo.setText(_translate("MainWindow", "Período"))
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
        self.tituloAbaCurso.setText(_translate("MainWindow", "Visão por Curso"))
        self.aplicarFiltrosCurso.setText(_translate("MainWindow", "Aplicar Filtros"))
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
        self.labelTurmaProf.setText(_translate("MainWindow", "Turma"))
        self.labelPeriodoProf.setText(_translate("MainWindow", "Período"))
        self.labelCursoProf.setText(_translate("MainWindow", "Curso"))
        self.tituloAbaProf.setText(_translate("MainWindow", "Visão por Professor"))
        self.aplicarFiltrosProf.setText(_translate("MainWindow", "Aplicar Filtros"))
        self.labelCursoSala.setText(_translate("MainWindow", "Curso"))
        self.botaoExportarGradeSala.setText(_translate("MainWindow", "Exportar Grade"))
        self.labelPeriodoSala.setText(_translate("MainWindow", "Período"))
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
        self.labelTurmaSala.setText(_translate("MainWindow", "Turma"))
        self.tituloAbaSala.setText(_translate("MainWindow", "Visão por Sala"))
        self.aplicarFiltrosSala.setText(_translate("MainWindow", "Aplicar Filtros"))