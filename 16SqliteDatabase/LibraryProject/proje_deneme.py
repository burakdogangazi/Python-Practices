from library import *


print("""

***********************************************
Kütüphane Programına Hoşgeldiniz...

İşlemler : 

1.Kitapları Göster
2.Kitap Sorgula
3.Kitap Ekle
4.Kitap Sil
5.Baskı Yükselt

Çıkmak için q'ya basın.

***********************************************

""")

library = Kütüphane()


while True:

    işlem = input("Yapacağınız İşlem : ")

    if(işlem == "q"):
        print("Program Sonlandırılıyor")
        break

    elif(işlem == "1"):
        library.kitaplari_goster()

    elif(işlem == "2"):
        isim = input("Hangi kitabı istiyorsunuz? : ")
        print("Kitap sorgulanıyor")
        time.sleep(2)
        library.kitap_sorgula(isim)

    elif(işlem == "3"):
        isim = input("İsim : ")
        yazar = input("Yazar : ")
        yayınevi = input("Yayınevi : ")
        tür = input("Tür : ")
        baskı = input("Baskı : ")

        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baskı)

        print("Kitap Ekleniyor")
        time.sleep(2)
        library.kitap_ekle(yeni_kitap)
        print("Kitap Eklendi.")

    elif(işlem == "4"):
        isim = input("Hangi kitabı silmek istiyorsunuz?")
        cevap = input("Emin misiniz? E/H")
        if(cevap == "E"):
            print("Kitap Siliniyor.")
            time.sleep(2)
            library.kitap_sil(isim)
            print("Kitap Silindi.")

    elif(işlem == "5"):
        isim  = input("Hangi kitabın baskısını yükseltmek istiyorsunuz ? ")
        print("Baskı yükseltiliyor.")
        time.sleep(2)
        library.baskı_yükselt(isim)
        print("Baskı yükseltildi.")

    else:
        print("Geçersiz İşlem")













