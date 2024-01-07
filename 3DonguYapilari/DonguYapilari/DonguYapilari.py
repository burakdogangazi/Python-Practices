

# in operatörü

6 in [1,2,3,4,5,6] # true döner


#Liste üzerinde gezinmek

liste=[1,2,3,4,5,6]

for eleman in liste:
    print(eleman)

toplam = 0
for eleman1 in liste:
    toplam +=eleman1

liste1 =[1,2,3,4,45,56,76]

for eleman1 in liste1:
    if(eleman%2 ==0):
        print(eleman)

s = "Python"
for i in s:
    print(i)

liste3 =[(1,2),(3,4),(5,6)]


    
for (i,j) in liste3:
    print("i: {}   j:  {}".format(i,j))

    
sözlük = {"bir":1, "iki":2, "üç":3}

for eleman in sözlük.values():
    print(eleman)

for (i,j) in sözlük.items:
    print("anahtar: {}   değer:  {}".format(i,j))


# While Döngüsü

i=0

while(i <10):
    print("i nin değeri",i)
    i+=1

liste = [1,2,3,4,5]
print(len(liste))
index = 0

while(index <len(liste)):
    print("Index ",index,"Liste elemanı",liste[index])
    index+=1

#range fonksiyonu

print(*range(0,20))# 0 1 2 3 4 5...
print(*range(0,20,5))# 0 5 10 15 

liste=[1,2,3,4,5]

for i in liste:
    print(i)

for i in range(1,101):
    print(i)

#Break ifadesi

# break sadece içinde kullanılan döngüyü sonlanıdırır iç içe for var ise en içerideki döngüyü sonlandırır.

liste = [1,2,3,4,5,6,7,8,9]
for i in liste:
    if(i==5):
        break
    print(i)

while True:
    isim = input("İsim(çıkmak için q'ya basın)")

    if(isim == 'q'):
        print("Programdan çıkılıyor")
        break

    print(isim)

#Continue ifadesi
#Döngü bloğunun başına döner

liste = list(range(11))
for i in liste:
    if(i == 3 or i == 5):
        continue
    print("i: ",i)

while(i < 10):
    if(i == 2):
        continue
    print(i)
    i+=1 # sonsuza akdar değer 2 de döner değer arttırılmasına gelemez

#List Comprehension
liste1 = [1,2,3,4,5]

liste2 = list()

for i in liste1:
    liste2.append(i)
print(liste2)



liste3 = [1,2,3,4,5]
liste4 = [i for i in liste3]# list comprehension
print(liste4)

liste5 = [3,4,5]
liste6 = [i * 2 for i in liste5]# 6 8 10

liste7=[(1,2),(3,4),(5,6)]
liste8 = [i*j for i,j in liste7]# 2 12 30

s = "Python"
liste9 = [i*3 for i in s]



liste10 = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste11= list()
for i in liste:
    for x in i:
        liste11.append(x)

liste12 = [x for i in liste for x in i]
print(liste12)




