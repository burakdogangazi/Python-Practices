#Append Metodu
# en sona element ekler

liste = [1,2,3,4,5]
liste.append(6)
liste.append("Python")


#Extender 
#Bir listeye başka bir listenin elemanları eklemeyi sağlar

liste2 = [10,20,30,40]
liste.extend(liste2) # liste 1 e en sona liste 2 ekledik


#Insert Metodu
#İndexe göre eleman eklemek

liste.insert(2,15) # 2. indekse 15 ekledik


#Pop Metodu
# hiçbir değer verilmezse listenin sol elemanı siler ve ekrana basar indeks verilebilir

liste.pop()# sondakini siler elemanı ekrana basar
liste.pop(3)# 3. indekstekini siler ve ekrana basar.


#Remove Metodu
#Verilen Değeri listeden çıkarır.

liste.remove("Python")# değere göre silme işlemi ekrana silineni basmaz
# Olmayanı silmeye çalışırsan hata verir.


#Index Metodu
# değerin baştan başlayarak hangi indekste olduğunu söyler yoksa hata döner
#eğer ekstra index değeri belirtilirse metodu bu değerden itibaren arar.


liste3 = [1,2,3,3,3,4,56,6,7,8]
liste.index(3)# 2 basar
liste.index(3,3) # 4 basar 3 değerini 3.indexten itibaren arar.
#liste.index(10)# hata verir


#Count Metodu
#Değerin listede kaç defa geçtiğini sayar.

liste3.count(3)# 3  basar 3 tane 3 var


#Sort Metodu
#Sayı ise küçükten büyüğe kelime ise harf sırasına göre sıralar.
#Reverse = true ile büyükten küçüğe sıralanabilir


liste4 = [12,-2,3,1,34,100]

liste4.sort()# low to high

liste5 = ["Python","Java","Javascript","Php"]
liste5.sort() # alfabetik olarak

liste4.sort(reverse=True) # high to low

liste5.sort(reverse=True) # alfabetik olarak sondan başa
















