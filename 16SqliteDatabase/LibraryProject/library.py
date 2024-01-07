import sqlite3,time


class Kitap():
    def __init__(self,isim,yazar,yayınevi,tür,baskı):

        self.isim = isim
        self.yazar = yazar
        self.yayınevi = yayınevi
        self.tür = tür
        self.baskı = baskı
        
    def __str__(self):
        return "Kitap İsmi : {}\nYazar : {}\nYayınevi : {}\nTür : {}\nBaskı : {}".format(self.isim,self.yazar,self.yayınevi,self.tür,self.baskı)
        
        
class Kütüphane():

    def __init__(self):
        self.baglanti_olustur()


    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("library.db")
        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If not exists library (isim TEXT,yazar Text,yayınevi TEXT,tür TEXT,baski INT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()


    def baglantiyi_kes(self):
        self.baglanti.close()

    def kitaplari_goster(self):
        sorgu = "Select * From library"
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()

        if(len(kitaplar) == 0):
            print("Kütüphanede kitap bulunmuyor.")

        else:
            for i in kitaplar:

                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)

    def kitap_sorgula(self,isim):

        sorgu = "Select * From library kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        kitaplar = self.cursor.fetchall()

        if(len(kitaplar) == 0):
            print("Böyle Bir Kitap Bulunmuyor.")

        else:
            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])# kitaplar ismini  yazar yayınevialdık
            print(kitap)

    def kitap_ekle(self,kitap):

        sorgu = "Insert into library Values(?,?,?,?)"

        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayınevi,kitap.tür,kitap.baskı))

        self.baglanti.commit()


    def kitap_sil(self,isim):

        sorgu = "Delete From library where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        self.baglanti.commit()


    def baskı_yükselt(self,isim):

        sorgu = "Select * From library where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        kitaplar = self.cursor.fetchall()

        if(len(kitaplar) == 0):
            print("Böyle bir kitap bulunmuyor...")

        else:
            baskı = kitaplar[0][4]

            baskı += 1

            sorgu2 = "Update library set baskı = ? where isim = ?"

            self.cursor.execute(sorgu2,(baskı,isim))
            
            self.baglanti.commit()
