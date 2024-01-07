
class Dosya():

    def __init__(self):

        with open("metin.txt","r",encoding="utf-8") as file:

            dosya_icerigi = file.read()

            kelimeler = dosya_icerigi.split(" ") # ya da split() aynı işi yapar

            self.sade_kelimeler = list()

            for i in kelimeler:
                # Sondaki otomatik gelen \n boşluk ve , aldık
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(",")

                self.sade_kelimeler.append(i)
    
    def tum_kelimeler(self):
        kelimeler_kumesi = set()
        
        for i in self.sade_kelimeler:
            kelimeler_kumesi.add(i) # her kelime sadece 1 defa

        print("Tüm kelimeler.....")

        for i in kelimeler_kumesi:
            print(i)

    def kelime_frekansı(self):
        
        kelime_sozluk = dict()

        for i in self.sade_kelimeler:
            if(i in kelime_sozluk):
                kelime_sozluk[i] +=1
            else:
                kelime_sozluk[i] = 1 # kelime varsa 1 ekler yoksa 1 değeri ile başlatır  

        for kelime,sayi in kelime_sozluk.items():
            print("{} kelimesi {} defa geçiyor..".format(kelime,sayi))
            print("--------------------------------------------------")

  
dosya = Dosya()

dosya.tum_kelimeler()

















