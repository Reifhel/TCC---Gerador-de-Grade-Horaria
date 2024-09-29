import sys

from PyQt5.QtWidgets import QApplication
from interface import Interface

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = Interface()
    janela.show()
    sys.exit(app.exec_())
