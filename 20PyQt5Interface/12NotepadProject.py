from _typeshed import Self
import sys
from PyQt5 import QtWidgets
import os
from PyQt5.QtWidgets import QAction, QFileDialog, QMainWindow, QWidget,QHBoxLayout,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout, qApp


class NotePad(QWidget):

    def __init__(self):

        super().__init__

        self.init_ui()


    def init_ui(self):

        self.yazi_alani = QTextEdit()

        self.temizle = QPushButton("Temizle")

        self.ac = QPushButton("Aç")

        self.kaydet = QPushButton("Kaydet")


        h_box = QHBoxLayout()

        h_box.addWidget(self.temizle)

        h_box.addWidget(self.ac)

        h_box.addWidget(self.kaydet)

        v_box = QVBoxLayout()

        v_box.addWidget(self.yazi_alani)

        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.setWindowTitle("NotePad")

        self.temizle.clicked.connect(self.yaziyi_temizle)

        self.ac.clicked.connect(self.dosya_ac)

        self.kaydet.clicked.connect(self.dosya_kaydet)



    def yaziyi_temizle(self):
        
        self.yazi_alani.clear()

    def dosya_ac(self):
        
        dosya_ismi = QFileDialog.getOpenFileName(Self,"Dosya Aç",os.getenv("HOME"))

        with open(dosya_ismi[0],"r") as file:
            self.yazi_alani.setText(file.read())


    def dosya_kaydet(self):
        dosya_ismi = QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("Home"))

        with open(dosya_ismi[0],"w") as file:
            file.write(self.yazi_alani.toPlainText())


class Menu(QMainWindow):

    def __init__(self):

        super().__init__()

        self.pencere = NotePad()

        self.setCentralWidget(self.pencere)


        self.menuleri_olustur()

    def menuleri_olustur(self):

        menubar = self.menuBar()

        dosya = menubar.addMenu("Dosya")

        dosya_ac = QAction("Dosya Aç",self)

        dosya_ac.setShortcut("Ctrl+O")

        dosya_kaydet =QAction("Dosya Kaydet",self)

        dosya_kaydet.setShortcut("Ctrl+S")

        temizle = QAction("Dosyayı Temizle",self)

        temizle.shortcut("Ctrl+D")

        cikis = QAction("Çıkış",self)

        cikis.shortcut("Ctrl+Q")

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(temizle)
        dosya.addAction(cikis)


        dosya.triggered.connect(self.response)


        self.setWindowTitle("Metin Editoru")

        self.show()


    def response(self,action):

        if(action.text() == "Dosya Aç"):
            self.pencere.dosya_ac()
        elif(action.text() == "Dosya Kaydet"):
            self.pencere.dosya_kaydet()
        elif(action.text() == "Dosya Temizle"):
            self.pencere.yaziyi_temizle()
        elif(action.text() == "Çıkış"):
            qApp.quit()



app = QApplication(sys.argv)

menu = Menu()

sys.exit(app.exec_())
























