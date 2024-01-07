import sqlite3
import sqlite3

con = sqlite3.connect("library.db")

cursor = con.cursor() # imleç atadı databes üzerindeki işlemleri gerçekleştirebiliriz cursıor ile


def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS library (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit() # sorgu çalıştırır yukarıda yazılan
    # con.commit güncelleme işlemi


def veri_ekle():
    cursor.execute("Insert into library Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()

def veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("Insert into library Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()

def verileri_al():
    cursor.execute("Select * From library")
    liste = cursor.fetchall()
    print("Bilgiler...")
    for i in liste:
        print(i)

def verileri_al2():
    cursor.execute("Select İsim,Yazar From library")
    liste1 = cursor.fetchall()
    print("Bilgiler isim ve yazar")
    for i in liste1:
        print(i)

def verileri_al3():
    cursor.execute("Select * From library where Yayınevi = '?'",(yayınevi))
    liste2 = cursor.fetchall()
    for i in liste2:
        print(i)

def verileri_guncelle(eski_yayınevi,yeni_yayınevi):
    cursor.execute("Update library set Yayınevi = ? where = Yayınevi = ?",(yeni_yayınevi,eski_yayınevi))
    con.commit()

def verileri_sil():
    cursor.execute("Delete From library where Yazar = ?"(yazar,))
    con.commit()

#Mysql de yeni veri tablo altına eklenirken sqlite da yeni veri 1. sıraya üste yerleştirilir.

# Veri Eklemek
# isim = input("İsim:")
# yazar = input("Yazar:")
# yayınevi = input("Yayınevi:")
# sayfa_sayısı = (int(input("Sayfa sayısı:")))
# veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı)


#Veri Seçmek
# Select * From library tümünü alır
# Select İsim,Yazar From library
# Select * From library where Yayınevi = 'Everest'
# yayınevi = input("Yayınevi : ")


# Verileri Güncellemek Ve Silmek
# Update library set Yayınevi = 'Everest' where Yayınevi 'Doğan Kitap'
# Delete From library where Yazar = 'Ahmet Ümit'
# verileri_guncelle("Doğan Kitap","Everest")
# verileri_sil("Ahmet Ümit")




con.close()











