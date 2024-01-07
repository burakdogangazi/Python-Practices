#Tekrar yok herbirinden 1 tane olur ayrıca y[0] diyerek elemana ulaşılamaz
# eğer listeye çevirip bastırılabilir veya direk for ile yazdırılabilir.
# her bir elemandan 1 tane olacak şekilde düzenlendiği için program metod kulanımlarında hata vermez.
#1.yöntem
x = {1,2,3}
type(x)# set

#2.yöntem
x = set()

liste =[1,2,3,4,1,2,3,2,2]
x = set(liste)
print(x) # {1,2,3} olarak her elemandan en az 1 tane olacak şekilde yazılır.


x = set("Python Programlama Dili") # her bir elemenadan bir tane olmak üzere küme oluşturur

y = {"Elma","Armut","Kiraz"}

for i in y:
    print(i) # sırayla çıkmaz

y[0] # hata verir ulaşılamaz 

liste = list(y)
print(liste)


#Kümelerin metodları

#Add Metodu
z = {1,2,3,4,5}
z.add(6) # sona ekler
z.add(4) # hata vermez ama 4 olduğu için eklenmez

#Difference metodu

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
küme3 = {30,40,50}
küme1.difference(küme2) # küme 1  in küme 2 dn farklarını yazdırır.

#Difference Update Metodu

küme1.difference_update(küme2) # farkını küme 1 atar ve günceller.


#Discard Metodu

k = {1,2,3,4,5,6}

k.discard(2)# 2 değerinı çıkartır kümeden
k.discard(100) # hata vermez 


#Intersection - Intersection Update Küme Kesişimleri

küme1.intersection(küme2) # 1,2,34 
küme1.intersection_update(küme2) # küme 1 e 1,2,34 atar


# Isdisjoint() Metodu Kümeler Ayrık mı
#kesişim boş ise true değilse false

küme1.isdisjoint(küme2)# false
küme1.isdisjoint(küme3)# true


# ıssubset alt küme mi
# alt kümeyse ture değilse false döner

küme5 =  {1,2,3}
küme6 =  {1,2,3,4}
küme7 =  {5,6,7}

küme5.issubset(küme6)# true
küme5.issubset(küme7) # false


#Birleşim Kümesi union() Ve Update

küme1.union(küme2) # ortak eleman 1 defa olmak üzere birleştirir

küme1.update(küme2) # güncelledik



