# Dosya Açmak
# dosya açmak için open(dosya adı,dosya erişme kipi)

# w tipi dosya açar ve dosyalara yazar eğer dosya önceden varsa silip tekrar oluşturur

# file = open("örnekmetin.txt","w")
# file.close()# dosya kapama yapmak zorundasın

# file = open("C:/Users/Burak/Desktop/örnekdeneme.txt","w")

# file = open("örnekmetin.txt","w",encoding = "utf-8")
# file.write("Burak Doğan")#türkçe karakter hata verir utf-8 encode yapman lazım
# file.close()


# a tipi 
# append kısaltması dosya yoksa oluşturur 
# varsa tekrar oluşturmadan dosya içinde sona giderek ekleme yapar

# file = open("örnekmetin.txt","w",encoding = "utf-8")
# file.write("Burak Doğan")
# file.close()

#Dosya Okuma İşlemleri

# r kipi dosya okumak ve verileri almak için r kipiyle dosya açıcan eğer dosya yoksa hata verir

# try:
    # file = open("örnekmetin.tx","r")

# except FileNotFoundError:
    # print("Dosya bulunamadı")

# file.close()
# file = open("örnekmetin.tx","r")



# Dosya içi okumak
#file = open("örnekmetin.txt","r",encoding = "utf-8")
#for i in file:
 #   print(i, end = "")# bir kere for döngüsünden 
    #bir tane de dosyada alt alt olduğu için bir taneye indirgedik \n attık
#file.close()




#Dosya read komutu
#Değer vermezsek dosyanın hepsini okur.

#file = open("örnekmetin.txt","r",encoding = "utf-8")

#icerik = file.read()
#print("Dosya içeriği : ")
#print(icerik)

#icerik2 = file.read()
#print("Dosya içeriği 2: ") # içerik 2 yi birdaha okumamıza rağmen okumadı
#print(icerik)
# ilk okuduk file imleci dosya sonuna gitti ikinci okuma sonda başladı bu yüzden ikinciye okumadı


# Dosya ReadLine Komutu
# her çağırıldığında dosyanın sadece bir satırını okur dosya imleci bir satır atlayarak devam eder.

#file = open("örnekmetin.txt","r",encoding = "utf-8")
#print(file.readline()) # ilk satır okudu
#print(file.readline())# 2. okudu
#print(file.readline())# 3.okudu
#print(file.readline())#4.okudu
#print(file.readline()) # boş string döndü okunacak değer yok
#file.close()


#ReadLines fonksiyonu
# Dosyanın bütün satırlarını bir liste şeklinde döner.

#file = open("örnekmetin.txt","r",encoding = "utf-8")

#liste = file.readlines()
#print(liste)
#file.close()


#Dosyalarda kullanılan fonksiyonlar
# otomatik olarak iş bitince dosya kapamak

#with open("örnekmetin.txt","r",encoding = "utf-8") as file:
    #for i in file:
        #print(i)


#Dosyaları İleri Geri Sarmak
#Normalde okuma işlemi sonucu file imleç dosya sonu olur
# seek() ile istediğimiz yere getiriyoruz,
# tell() ile dosya imleci hangi bytta onu öğrenebiliriz.

#with open("örnekmetin.txt","r",encoding = "utf-8") as file:
    #print(file.tell())
    #file.seek(20)# 20.byte a gider

    
#with open("örnekmetin.txt","r",encoding = "utf-8") as file:
 #   file.seek(5)
  #  icerik = file.read(10)
  #  print(icerik) #5.bayttan başlattık 10 karakter okuttuk

#with open("örnekmetin.txt","r",encoding = "utf-8") as file:
 #   file.seek(5)
  #  icerik = file.read(10)
 #   file.seek(0)
  #  icerik2 = file.read(6)
   # print(icerik)
  # print(icerik2)# başa döndü okudu 6 tane


# Dosyalarda Değişiklik Yapmak
#r+ kipi
#biz bir dosyanın belli bir yerine seek onksiyonu ile gidip write() kullanırsak
#yazdığımız değerler öncesinde bulunan değerlerin üzerine yazılcaktır. bunu için hem okuma hem de yazma işlemimizi sağlayan r+ kullanılır
with open("örnekmetin.txt","r+",encoidng = "utf-8") as file:
    print(file.read())

with open("örnekmetin.txt","r+",encoidng = "utf-8") as file:
    file.seek(10)
    file.writable("Deneme")#10satırdan sonraki deneme yazısı getirdi orda olanların üzerine yazdı önceki silindi sadece 10.satır ile 16. satır arası.

# Dosyada dosya başına cümle eklemek

with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    icerik = file.read()
    icerik = "Mehmet Keper\n"+ icerik
    file.seek(0)
    file.write(icerik)


# Dosyanın ortasına eklemek ve yazdırmak

with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    liste = file.readlines()
    liste.insert(3,"Ahmet Baltacı\n")
    file.seek(0)
    for i in liste:
        file.write(i)

with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    liste = file.readlines()
    liste.insert(3,"Ahmet Baltacı\n")
    file.writelines(liste) # elemanları dosyaya yazmak
   

