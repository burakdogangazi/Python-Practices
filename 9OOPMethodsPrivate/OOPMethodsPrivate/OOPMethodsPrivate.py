class Kitap():
    def __init__(self,isim,yazar,sayfa_sayısı,tür):
        print("İnit Fonksiyonu")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
        self.tür = tür
    def __str__(self):
        return "İsim : {}\n Yazar : {}\n Sayfa Sayısı : {}\n Tür : {}".format(self.isim,self.yazar,self.sayfa_sayısı,self.tür)
    def __len__(self):
        return self.sayfa_sayısı
    def __del__(self):
        print("Kitap objesi siliniyor.")
#print(kitap) kendi metodumuzu yazmadan önce python kendi __str__ adı altında tanımlamış ve değişik bilgi yazdırdı bellek no vb
# biz kendi strmizi yazarak print fonksiyonumuzu kullandık
#del kitap #__del__ metodunu çağırır objeyi siler

kitap = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye")
print(kitap)# bizim yazdığımız strden kullanır.

#len(kitap) direk hata verir çünkü tanımlı değil kendimiz yazmalıyız
#len(kitap)# sayfa sayısını bastırır

# del kitap der isek hala pythonun kendi delini kullanıyoruz ama kendimiz özellik ekliyoruz
