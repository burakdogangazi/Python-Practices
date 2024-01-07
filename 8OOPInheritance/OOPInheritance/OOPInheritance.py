class Çalışan():

    def __init__(self,isim,maaş,departman):
        print("Çalışan sınıfının init fonksiyonu")

        self.isim = isim
        self.maaş = maaş
        self.departman = departman

    def bilgileri_goster(self):
        print("Çalışan sınıfın bilgileri")
        print("İsim : {}\n Maaş : {}\n Departman : {}".format(self.isim,self.maaş,self.departman))

    def departman_degis(self,yeni_departman):
        self.departman = yeni_departman

class Yönetici(Çalışan):
    # inheritance etmek extends ya da c# gibi xxx:abc
    #pass içi boş yapmaki çin yoksa hata verir
    def __init__(self,isim,maas,departman,kisi_sayisi):
        print("Yönetici sınıfının init fonksiyonu")# override ettik çalışandan
        # kendi init fonksiyonumuz çalışacak
        self.isim = isim
        self.maaş = maas
        self.departman = departman
        self.kisi_sayisi = kisi_sayisi

    def zam_yap(self,yeni_zam):
        self.maaş += yeni_zam

    
    def bilgileri_goster(self):
        print("Yönetici sınıfın bilgileri")
        print("İsim : {}\n Maaş : {}\n Departman : {}\n Sorumlu Kişi Sayısı : {}".format(self.isim,self.maaş,self.departman,self.kisi_sayisi))



yönetici = Yönetici("Burak Doğan",3000,"Bilişim")
yönetici.bilgileri_goster()
yönetici.departman_degis("İnsan kaynakları")
yönetici.bilgileri_goster()
yönetici.zam_yap()
yönetici.bilgileri_goster()

#Overriding
#Eğer biz miras aldığımız metodu aynı isimle kendi sınıfımızda 
# tekrar tanımlarsak miras aldığımız değil kendi metodumuz çalışacaktır.

yönetici = Yönetici("Doğan Burak",3500,"Bilişim",10)

#Super Anahtar Kelimesi
#Override edilen metodun içinde miras aldığımız metodu kullanmak istersek kullanılabilir
#miras alınan sınıfın metodlarını alt sınıflardan kullanmamızı sağlar.

class Yönetici1(Çalışan):
    
    def __init__(self,isim,maas,departman,kisi_sayisi):
        print("Yönetici sınıfının init fonksiyonu")
        
        super().__init__(isim,maas,departman)# bu kerlime ile çalışan initini kullandık kendimizinkini aşağı ekledik
        
        self.kisi_sayisi = kisi_sayisi

    def zam_yap(self,yeni_zam):
        self.maaş += yeni_zam

    
    def bilgileri_goster(self):
        print("Yönetici sınıfın bilgileri")
        print("İsim : {}\n Maaş : {}\n Departman : {}\n Sorumlu Kişi Sayısı : {}".format(self.isim,self.maaş,self.departman,self.kisi_sayisi))

yönetici2 = Yönetici1("DDoganBBurak",3000,"Bilişim",5)
#çalışan sınıfının int fonk sonrasında yönetici sınıfının init fonk dedi

yönetici.bilgileri_goster()