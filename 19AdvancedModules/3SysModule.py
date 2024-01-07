import sys

print(dir(sys))
#Daha çok terminalden kullanılır

#SYS EXIT
# a = int(input("a:"))
# b = int(input("b:"))
# sys.exit()
# c = int(input("c:")) sys exitten sonrası okunmaz


#STDERR STDOUT

#stdin : bu standard dosya işlemimizin kullanıcıdan input almasını sağlar
#stdout : bu standard dosya işlemimizin kullanıcıdan çıkış almasını sağlar
#stderr : hata mesejlarını çıktı olarak vermek için kullanılır.


# sys.stderr.write("Bu bir hata mesajıdır")
# sys.stderr.flush()# buffer a yazdığımız direk yazdırmak için kullanıyoruz. Kullanamasan da yazar.
# sys.stdout.write("Bu bir normal yazıdır")



# SYSARGV
# print(sys.argv)

for i in sys.argv:
    print(i) # dosyaya cmd den açıp dosya adı değerleri yan yana yazarsak değer girmiş oluruz ve for ile sıralarız


def kok_bulma(a,b,c):
    delta = b ** 2 -4*a*c

    if(delta < 0):
        print("Reel kök yok")

    else:
        x1 = (-b -delta **0.5)/(2*a)
        x2 = (-b +delta **0.5)/(2*a)
        return(x1,x2)


if(len(sys.argv) == 4):
    print("Kök bulma",kok_bulma(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))

else:
    sys.stderr.write("Lütfen doğru değerler girin")
    sys.stderr.flush()


# termaili aç dosyaya git xxxx.py 1 2 3 gibi değerleri gir sonra kök bulunur