import sys
#horizontal yatay --  vertical dikey -- layout yerleşim
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtCore import Qt



def Pencere():

    app = QtWidgets.QApplication(sys.argv)

    okay = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("İptal")

    h_box = QtWidgets.QHBoxLayout()

    # v_box = QtWidgets.QHBoxLayout()# vertical için aynısı horizontal için de geçerli


    # h_box.addStretch() # butonları sağda kaldı 

    # h_box.addWidget(okay)
    # # h_box.addStretch() butonların arasında başlık oldu
    # h_box.addWidget(cancel)

    # h_box.addStretch() #  ekranı genişletince butonların solda kalmasını nasıl sağlayabiliriz genişlentince
    # #pencereyi çeksen bile solda kalır butonlar
    
    
    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)
    
    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)
    
    
    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("PyQt5 Ders 5")

    pencere.setGeometry(100,100,500,500) 

    pencere.setLayout(h_box)


    pencere.show()


# pip install pyqt5-tools
# Then restart the cmd, just type "designer" and press enter.


Pencere()