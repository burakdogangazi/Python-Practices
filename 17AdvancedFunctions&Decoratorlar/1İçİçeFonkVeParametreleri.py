def fonksiyon(*args): # yıldız istediğimiz kadar gönderebiliriz
    for i in args:
        print(i)
    # gönderilenler demete dönüştürülür ve for la gezinebiliriz

def fonksiyon(isim,*args):
    print("İsim : ",isim)

    print("------")

    for i in args:
        print(i)

def fonksiyon(**kwargs): # keyword argument
    print(kwargs) # sözlük yapısı oluşturur
    for i,j in kwargs.items():
        print("Arguman ismi",i,"Arguman Degeri",j)


def fonksiyon(*args,**kwargs):
    for i in args:
        print(i)

    print("---------")

    for i,j in kwargs.items():
        print(i,j)


fonksiyon("Murat",1,2,3,3,4,5,56) # murat isime gidiyor diğerleri args da demet oluyor


fonksiyon(isim = "Murat", soyisim = "Coskun") # sözlük yapısı


fonksiyon(1,2,3,4,5,6,isim = "Burak",soyisim = "Doğan")


# İç İçe Fonksiyonlar
# Pythonda fonksiyonlar birer obje oldukları için bir tane değişkene veya farklı bir fonksiyon
# içinde tanımlanabilirler.


def selamla(isim):
    print("selam ",isim)

def fonk():
    def fonk2():
        print("Küçük fonk")
    fonk2()
    print("Büyük fonk")

def fonk3(*args):

    def toplama(args):
        toplam = 0
        for i in args:
            toplam +=i
            return toplam
    print(toplama(args))



merhaba  = selamla

merhaba("burak")


del selamla

# selamlayı sildik ama merhaba duruyor referansı silmiyor sadece o objeyi siliyor

# fonk2() tanımlı değil local değişken

fonk3(1,2,3,4,5,6,7)


# decorator fonksiyona ekstra özellik dinamik özellik eklemektir.








