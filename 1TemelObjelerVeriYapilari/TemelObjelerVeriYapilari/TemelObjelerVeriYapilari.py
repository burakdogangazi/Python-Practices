print(56/7) # 8.0 olarak değer verir
print(54.25/7.21)# 7.524271844660194 olarak verir
print(55/7)#7.857142857142857

i=10
print(i*i*i)

murat = 10
murat = 3.4
print(murat)# 3.4 basar


a=4
b=3

a,b=b,a# yer değiştirdiler.
print(a,b)

i += 1
i = i + 1

# tekli yorum satırı """ çoklu yorum satırı """

#Bu dilde bölme direk kesirli olarak yapıldığı için tam bölme operatoru bulunmaktadır.//
print(15//4)# cevap 3

#üs bulma op
print(3**4)# 81 cevap

#kalan bulma
print(15%3)# 0 cevap

# karekök
print(64 ** 0.5)# 8.0  cevap

#String oluşturma 3 farklı yol

'burak doğan'
"Burak doğan"
"""burak doğan"""

#String indeksleme

a="Merhaba"
print(a[0])# M
print(a[-1])#a sondan başlıyor

#String Parçalama

a="Python Programlama Dili"
print(a[4:10])#on Pro 4. den başla 10 a kadar git 10. yu alma
print(a[:10])#Python Pro baştan 10 a kadar git 10. alma
print(a[4:])#on Programlama Dili 4.yü al sona kadar git
print(a[:])# bütün stringi alır
print(a[:-1]) #her şeyi al sonuncu karakteri alma 
print(a[::2])#Pto rgalm ii
print(a[4:12:2])#o rg
print(a[::-1])# tersten okur

string = "burak"
print(len(string))#5 döner

burak= "burakdogan"
print(len(burak))#10

#burak[3] = 'T' hata verir string direk olarak değştirelemez.

a= 'burak'
b="dogan"
print(a+b)
print(burak * 3)#3 kere burak dogan yazar

a="Mustafa"
a = a +"Murat"+"Coskun"#önceki string yok oluyor yeni string oluşturuluyor aslında
print(a)#MustafaMuratCoskun


#Veri Tipleri dönüşümleri

a=45
float(a)
print(a)

b=34.1
int(b)
print(b)

#Sayıları stringe çevirme

c=345
str(c)
print(c)

#Stringleri ondalıklı sayıyıa çevirme

d="123123as"
#int(d)# hata verir
print(d)

e="1.233.21"
#int(e)# hata verir
print(e)

f="1.23"
float(f)# çalışır
print(f)


#Print fonksiyonu ve formatlama

print(type(34))# int basar

print(3,4,5,6,7)# normalde araya bir boşluk bırakarak yazar
print(3,4,5,6,7, sep="/")# 3/4/5/6/7
print(*"Python")# her bir karakterden sonra boşluk
print(*"Python", sep="\n")

k=5.22227
l=4.65553
print("{} + {} = {} ".format(k,l,k+l))

print("{1} + {0} = {2} ".format(k,l,k+l))# l k k+l

print("{:.2f} + {:.2f} = {:.3f} ".format(k,l,k+l)) #virgülden sonra 2 basamak alır ilk ikisini sonuncu üç


#Pyhton Liste veri tipi

liste = ["Elma",35,"Merhaba",3.14]
liste=[]# boş liste
liste = list()#boş liste

liste2 = [1,2,3,4,5,6]
print(len(liste2))

liste3 = list("Merhaba")# herkarakterin ayrı eleman olarak tutlduğu liste yapar

liste4 = [3,4,5,5,6,7,8,9,10]
print(liste4[3:5:2])

liste5= liste2+liste3

print(liste3 * 3)

liste5.append("python")
liste5.pop()#son elemanı çıkarır ya da indis ver

liste7=[43,25,67,99,23]
liste7.sort()# low to high
liste7.sort(reverse = true) #high to low

liste =[[1,2],[3,4],[5,6]]
liste[1][1]#4


#Demetler Tuplelar
#Listeden farkı değiştirilemez oluşu
# listeden daha hızlı read only olduğu için
demet = (1,23,4,5,6,7,8)
demet[4]
demet[-1]
demet[::-1]

demet2=(1,1,11,1,1,1,2,3,4)
demet2.count(1)# 1 kaç kere geçiyor
demet2.count(10) # olmadığı için 0 bastırır

demet3=("Python","php","java")
demet3.index("Pyhton")# yoksa hata verir


#Sözlükler Dictionary

sözlük1= {"sıfır":bir, "iki":üç,"dört":beş}

sözlük2 ={}
sözlük3= dict()

sözlük1["bir"]

a={"bir":[1,2,3,4],"iki":[[1,2],[3,4],[5,6]]}

a["iki"][1][1]# 4

sözlük1["bir"] = 10

a={"sayılar":[1,2,3,4],"meyveler":{"karpuz":yaz}}
a["meyveler"]["karpuz"]

sözlük1.keys()
sözlük1.values()
sözlük1.items()# anahtar ve karşılık değeri

for k,v in sözlük1.items():
    print(k,v)



#Kullanıcıdan Girdi Alma
input()#değer ister
a = int(input("Lütfen bir sayı giriniz:"))# yazı yazar değer ister
# String olarak alır her değeri c# gibi

try:
    a = int(input("a:"))
    print(a)
except ValueError:
    print("Yanlış Format")



fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# import random

# print(random.randrange(1, 10)) # 1 ile 9 arası sayılar




