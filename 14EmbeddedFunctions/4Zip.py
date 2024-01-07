
liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10,11]
liste3 = ["Python","Java","Php","Javascript"]
i = 0
sonuc = list()
while ( i < len(liste1) and i < len(liste2)):

    sonuc.append((liste1[i],liste2[i]))
    i+=1

#(1,6) (2,7) ... 11 boş yok

zip(liste1,liste2) # zip objesi oluşur

list(zip,liste1,liste2)

list(zip(liste1,liste2,liste3))

for i,j in zip(liste2,liste3):
    print(i,j)

#sözlük ler de aynı şekilde olur elma sıfır armut bir..

#elma:1 ,armut:2
#sıfır:0 , bir:1

# zip(sözlük1.values(),sözlük.values()) default keyler ziplenir values yazarsak değerler ziplenir.

