class Yazılımcı():

    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim = isim
        self.soyisim= soyisim
        self.numara = numara
        self.maaş =maaş
        self.diller = diller

    def bilgilerigoster(self):
        # obje üzerindeki herhangi bir şeye erişebilmek için self şart
        print("""
                Yazılımcı objesinin özellikleri
                isim : {}
                Soyisim : {}
                Numara : {}
                Maaş : {}
                Diller : {}

        """.format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))
    
    def zam_yap(self,zam_miktarı):
        print("Zam yapılıyor.")
        self.maaş += zam_miktarı

    def dil_ekle(self,yeni_dil):
        print("Dil Ekleniyor.")
        self.diller.append(yeni_dil)



yazılımcı = Yazılımcı("Burak","Doğan",12345,3000,["Python","Java","C","Javascript"])

yazılımcı.bilgilerigoster() #bilgiler ekrana gözüktü

yazılımcı.dil_ekle("GoLang")

yazılımcı.bilgilerigoster()#bilgiler eklendi

yazılımcı.zam_yap(500)

yazılımcı.bilgilerigoster()# bilgiler güncellendi
