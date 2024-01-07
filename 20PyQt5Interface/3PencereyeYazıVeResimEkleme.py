import sys

from PyQt5 import QtWidgets,QtGui



def Pencere():

    app = QtWidgets.QApplication(sys.argv)


    pencere = QtWidgets.QWidget

    pencere.setWindowTitle("PyQt5 Ders 3")

    etiket1 = QtWidgets.QLabel(pencere)

    etiket2 = QtWidgets.QLabel(pencere)

    etiket2.setPixmap(QtGui.QPixmap("python.png"))
    
    etiket2.move(70,100)

    etiket1.setText("Bu bir yazıdır")

    etiket1.move(150,30) # yazıyı taşıdık ekranda

    pencere.setGeometry(100,100,500,500) # 100 100 konumundan başlayacak ve 500 e 500 olacak şekilde pencere boyutu

    pencere.show()





Pencere()



