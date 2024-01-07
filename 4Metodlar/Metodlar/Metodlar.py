
a= [1,2,3,4,5]

a.insert(1,"Murat")# 1. indekse murat koy 1, murat ,2 ,3,4,5
a.append("Python")# liste sonuna ekledi
#help(a.append) ne şekilde kullanıldığını öğrenmek için

#Fonksiyonlar

def selamla():
    print("Merhaba\n Nasılsınız")

selamla()

def selamla(isim):
    print("isminiz:",isim)

selamla("Kemal")


def toplama(a,b,c):
    print(a+b+c)

toplama(3,4,5)

def fakt(sayi):
    faktoriyel=1
    if(sayi == 0 or sayi == 1):
        print(faktoriyel)
    else:
        while(sayi >= 1):
          faktoriyel*=sayi
          sayi-=1
          print(fakt)

fakt(5)

#Fonksiyonlarda Return


def toplama(a,b,c):
    return a+b+c
   #print("Toplama")çalıştırılmadı returnden sonra geldiği için

print(toplama(3,4,5))

#Fonskiyonlarda Parametre Türleri

def serlamla(isim = "İsimsiz", soyisim = "Boş"):
    print("Selam",isim,soyisim)# fonksiyona değer göndermezsek isimsiz olucak

selamla(soyisim = "doğan")# sadece soyisim verdik isim yok
selamla(burak)# sadece isim verdik soyisim yok

def topla(*a):
    print(a) # gönderilen değerler bir tuple içinde tutulur (1,2,3)

def topla1(*a):
    toplam = 0
    for i in a:
        toplam += i
    print(toplam)# demet içinde toplandı

#Global ve Yerel Değişkenler

def fonksiyon():
    a=10
    print(a)

fonksiyon()
#print(a) a değişkeni tanımlanmamış dedi çünkü fonksiyonun yerel değişkeni

b=5
def fonksiyon1():
    print(b)# hata vermez b değişkeni global
    #print(s) #hata verir fonksiyon çağrısı yapıldıktan sonra çağırıldığı için

fonksiyon()
s="python"

c = 10

def fonksiyon3():
     c = 2
     print(c)# 2 basar

fonksiyon3()
print(c)# 10 


d = 5
def fonksiyon4():
    global d# global d yazarak global kullanmak istediğimizi söyledik ve oraya 3 koyduk
    d=3
    print(d)#3

fonksiyon4()
print(d)#3


if True:
    e = 4
    print(e)# hata vermedi
print(e)
#if ve while bloğu içinde tanımlanması global değişken yapar. 
#Yerel değişken sadece fonksiyon için ve sınıf için

#Lambda ifadeleri

#List comprehesion benziyor

Liste1 = [1,2,3,4,5]
liste2 = [i*2 for i in liste1]

def ikiylecarp(x):
    return x*2

ikileçarp = lambda x: x * 2

#-----


def toplama(x,y,z):
    return x+y+z

topla = lambda x,y,z : x+y+z

#-----

def terscevir(s):
    return s[::-1]

cevirters = lambda s : s[::-1]

def cifttek(x):
    return x % 2 == 0

print(cifttek(13)) #false verir

tekcift = lambda x : x % 2 == 0
