# Pythonda fonksiyonlarımıza dinamik olarak ekstra özellijk eklediğmiz fonksiyonlara denir
# flask gibi frameworklerde kullanılır

import time

def kareleri_hesapla(sayılar):
    sonuc = list()
    baslama = time.time()
    for i in sayılar:
        sonuc.append(i **2)

    bitis = time.time()
    print("Bu fonk 1 : "+bitis-baslama)

    return sonuc
   


def küpleri_hesapla(sayılar):
    sonuc = list()
    baslama = time.time()
    for i in sayılar:
        sonuc.append(i ** 3)

    bitis = time.time()
    print("Bu fonk 2 : "+bitis-baslama)
    return sonuc


kareleri_hesapla(range(100000))
küpleri_hesapla(range(100000))

# Bakınca zaman hesapla fonk işi değil ama hesapladığımız için kod tekrarı oldu 

def zaman_hesapla(func):
    def wrapper(sayılar):
        baslama = time.time()
        sonuc = func(sayılar)
        bitis = time.time()
        print(func.__name__ + " " + str(bitis-baslama+ "saniye sürdü."))
        return sonuc
    return wrapper

@zaman_hesapla
def kareleri_hesapladec(sayılar):
    sonuc = list()
    for i in sayılar:
        sonuc.append(i **2)
    return sonuc 

@zaman_hesapla
def küpleri_hesapladec(sayılar):
    sonuc = list()
    for i in sayılar:
        sonuc.append(i ** 3)
    return sonuc


kareleri_hesapladec(range(100000))
küpleri_hesapladec(range(100000))

# ilk önce zaman hesapla çağırıyor func içine kareleri hesapla gönderiyor
# daha sonra wrapper içine gönderiğimiz 100000 sayısını gönderiyoruz
# wrapper içinde gönderdiğimiz sayı ile sonuc = func(sayılar) diyerek normal fonksiyonumuzu kareleri hesapla uygulanıyor
# sonra wrapper objesini döndürdük


















