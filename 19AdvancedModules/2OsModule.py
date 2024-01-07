import os
from datetime import datetime

dir(os)

# os.chdir("c:/Users/user/Desktop") # bu pathe gittik
# print(os.getcwd()) # nerede olduğumuzu söyler
# print(os.listdir())# bulunan yerdeki klasör dosyaları bastırır.


os.mkdir("Deneme1")# deneme1 adında olduğu yerde klasör oluşturur.


# os.mkdir("Deneme2/Deneme3") # deneme 2 olmadığı için hata verir 
# deneme2 yok oluşturup içine deneme3 koyayım demez o yüzden

os.mkdirs("Deneme2/Deneme3")# burda oluşturup yapar deneme 2 yi oluşurup içine deneme3 koyar


os.rmdir("Deneme2/Deneme3") # deneme2 altındaki deneme3 i sil demek

os.removedirs("Deneme2/Deneme3")# hem deneme 2 hem deneme 3 siler

os.rename("test.txt","text2.txt") # ismi text2 yapar

print(os.stat("test2.txt")) # bütün özelliklerini yazar

print(datetime.fromtimestamp(os.stat("test2.txt").st_mtime)) # ne zaman dosya değiştirilde yazar.

for klasor_yolu,klasor_isimleri,dosya_isimleri in os.walk("C:/Users/user/Desktop"):
    print("Klasör yolu : ",klasor_yolu) # klasörleri hepsini gezer ve bütün dosya klasörleri yazdırır bütün elemanları demet olarak döner
    print("Klasör İsimler : ",klasor_isimleri)
    print("Dosya isimleri : ",dosya_isimleri)

for klasor_yolu,klasor_isimleri,dosya_isimleri in os.walk("C:/Users/user/Desktop"):
    for i in dosya_isimleri:
        if(i.endswith(".txt")):
            print(i)



