import sys

from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv) # sys.argv komut satırından göndereceğimiz için

    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("PyQt5 Ders 1")

    pencere.show()

    sys.exit(app.exec_())


Pencere()
























