import sys

from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow,QMenu


class Menu(QMainWindow):

    def __init(self):
    
        super().__init__()

        menubar = self.menuBar()

        dosya = menubar.addMenu("Dosya")

        duzenle= menubar.addMenu("Düzenle")

        dosya_ac = QAction("Dosya Aç",self)

        dosya_ac.setShortcut("Ctrl+O")

        dosya_kaydet = QAction("Dosya Kaydet",self)

        dosya_kaydet.setShortcut("Ctrl+S")

        cikis = QAction("Çıkış",self)

        cikis.setShortcut("Ctrl+Q")

        dosya.addAction(dosya_ac)

        dosya.addAction(dosya_kaydet)

        dosya.addAction(cikis)

        ara_ve_degistir = duzenle.addMenu("Ara Ve Değiştir")

        ara = QAction("Ara",self)

        degistir = QAction("Değiştir",self)

        temizle = QAction("Temizle",self)

        ara_ve_degistir.addAction(ara)
        ara_ve_degistir.addAction(degistir)

        duzenle.addAction(temizle)


        cikis.triggered.connect(self.cikis_yap)

        dosya.triggered.connect(self.response)


        self.setWindowTitle("Menüler")

        self.show()



    def cikis_yap(self):
        qApp.quit(self)


    def response(self,action): # python kendisi gönderiyor 52 den

        if(action.text() == "Dosya Aç"):

            print("Dosya aç")

        elif(action.text() == "Dosya Kaydet"):

            print("Dosya kaydet")

        elif(action.text() == "Çıkış"):

            print("Dosya Çıkış")

        




app = QApplication(sys.argv)

menu = Menu()

sys.exit(app.exec_())




