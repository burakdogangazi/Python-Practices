liste = ["Elma","Armut","Muz","Kiraz"]

i = 0

sonuc = list()


while(i < len(liste)):
    sonuc.append(i,liste[i])
    i+=1


list(enumerate(liste)) # obje verir yukarıdaki gibi işlem yapar 0 elma 1 armut ...


for i,j in enumerate(liste):
    print(i,j)


liste1 = ["a","b","c","d","e","f","g"]

for i,j in enumerate(liste1):
    if(i  % 2 == 0):
        print(j)

        

















