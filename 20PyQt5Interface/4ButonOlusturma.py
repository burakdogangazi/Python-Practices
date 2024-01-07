import sys

from PyQt5 import QtWidgets,QtGui



def Pencere():

    app = QtWidgets.QApplication(sys.argv)

    

    pencere = QtWidgets.QWidget

    pencere.setWindowTitle("PyQt5 Ders 4")

    pencere.setGeometry(100,100,500,500) 

    buton = QtWidgets.QPushButton(pencere)

    buton.setText("Burası Bir butondur")

    etiket = QtWidgets.QLabel(pencere)

    etiket.setText("Merhaba Burak")

    etiket.move(200,30)

    buton.move(190,80)

    pencere.show()





Pencere()