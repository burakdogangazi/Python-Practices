import random
import time

class Kumanda():

    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi= ["TRT"],kanal = "Trt"):
        
        self.tv_durum = tv_durum

        self.tv_ses =tv_ses
        
        self.kanal_listesi = kanal_listesi

        self.kanal = kanal

    def tv_ac(self):

        if(self.tv_durum == "Açık"):
            print("Televizyon Zaten Açık")
        else:
            print("Televizyon açılıyor")
            self.tv_durum = "Açık"

    def tv_kapa(self):

        if(self.tv_durum == "Kapalı"):
            print("Televizyon Zaten Kapalı")
        else:
            print("Televizyon kapanıyor")
            self.tv_durum = "Kapalı"

    def ses_ayarları(self):
        
        while True:

            cevap = input("Sesi azalt '<'\n Sesi yükselt '>'\n Çıkış: çıkış")

            if(cevap == '<'):
                if(self.tv_ses !=0):
                    self.tv_ses -=1
                    print("Ses:",self.tv_ses)
            elif(cevap == '>'):
                if(self.tv_ses != 31):
                    self.tv_ses +=1
                    print("Ses: ",self.tv_ses)
            else:
                print("Ses Güncellendi : ",self.tv_ses)
                break

    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor")
        time.sleep(1)# 1 saniye bekler
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal Eklendi")

    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki kanal:",self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)
    
    def __str__(self):#print fonksiyonu çağırılınca gelecek
        return "Tv durumu {}\n Tv Ses {}\n Kanal Listesi: {}\n Şu anki kanal {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)


kumanda = Kumanda()
print("""

1. Tv aç
2. Tv Kapa
3. Ses Ayarları
4. Kanal Ekle
5. Kanal Sayısını Öğrenme
6. Rastgele Kanala Geçme
7. Televizyon Bilgileri

Çıkmak için 'q' ya basın


""")

while True:
    işlem = input("İşlem seçiniz:")

    if(işlem == 'q'):
        print("Programdan çıkılıyor.")
        break
    elif(işlem == "1"):
        kumanda.tv_ac()
    elif(işlem == "2"):
        kumanda.tv_kapa()
    elif(işlem=="3"):
        kumanda.ses_ayarları()
    elif(işlem =="4"):
        kanal_isimleri = input("Kanal İsimlerini virgülle ayırarak giriniz:")

        kanal_listesi = kanal_isimleri.split(",")# virgülle ayırarak listeye atar

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif(işlem =="5"):
        print("Kanal Sayısı:",len(kumanda))
    elif(işlem == "6"):
        kumanda.rastgele_kanal()
    elif(işlem == "7"):
        print(kumanda)
    else:
        print("Geçersiz İşlem...")

        
    


