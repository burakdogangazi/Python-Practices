
#Class anahtar kelimesi

class Araba():
    model = "Renault Megane"
    renk = "Gümüş"
    beygir_gücü = 110
    silindir = 4

class Araba2():
    model = "Renault Megane"
    renk = "Gümüş"
    beygir_gücü = 110
    silindir = 4   # self konmak zorunlu başına
    def __init__(self):# self anahtar kelimesi objeyi gösteren referans
        print("İnit fonksiyonu çağırıldı.")

class Araba3():
   def __init__(self,model,renk,beygir_gücü,silindir):
       self.model = model
       self.renk = renk
       self.beygir_gücü=beygir_gücü
       self.silindir = silindir

class Araba4():
   def __init__(self,model = "Bilgi Yok",renk = "Bilgi yok",beygir_gücü = -1,silindir =-1):
       self.model = model # boş gönderilirse bunlar çalışır bilgi yok ve -1
       self.renk = renk
       self.beygir_gücü=beygir_gücü
       self.silindir = silindir

araba1 = Araba()# new kullanılmıyor obje üretmek
araba2 = Araba()
print(araba1.model)# renault megane
print(araba2.beygir_gücü)#110

print(Araba.model)#Renault Megane

#Bizim her bir objeyi başlangıçta farklı değerlerle oluşturmamaız için obje değeri gönderimemiz gerekir
# init() fonksiyonu bu işe yarar constructor denir ilk çağırılan fonksiyon

araba3 = Araba2()# init fonksiyonu çağırıldı yazar
# biz araba2() parantez içini doldurmak python kendisi araba3 ü obje olarak refereansa gönderiyior ekstradan belirtmeye lüzüm yok

araba4 = Araba3("Megane","Siyah",110,4)# özellikleri verildi

araba5 =Araba3("Ferrari","Kırmızı",350,8)

araba6 = Araba4(beygir_gücü=80) # beygir hariç hepsi boş





