
try:
    a = int("asdasd32")
    print("Program burada")

except:# bütün hatalarda arar
    print("Bir Hata oluştu")
print("Bloklar sona erdi")

try:
    a = int("asdasd32")
    print("Program burada")

except ValueError:# value error değilse girmez
    print("Bir Hata oluştu")
print("Bloklar sona erdi")

try:
    a = int(input("Sayı1:"))
    b = int(input("Sayı2:"))
    print(a/b)
except ValueError:
    print("Lütfen input doğru girin:")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez")
print("Bloklar sona erdi")


try:
    a = int(input("Sayı1:"))
    b = int(input("Sayı2:"))
    print(a/b)
except (ValueError,ZeroDivisionError):
    print("İki tane hata oluştu.")

print("Bloklar sona erdi")

#finally blokları

#kesinlikle uygulanması gereken

try:
    a = int(input("Sayı1:"))
    b = int(input("Sayı2:"))
    print(a/b)
except (ValueError,ZeroDivisionError):
    print("İki tane hata oluştu.")
finally:
    print("Burası çalıştı")

# Hata fırlatmak

def terscevir(s):
    if(type(s) !=str):
        raise ValueError("Lütfen string bir değer gönderin") # hatayı error listte çıkartır
    else:# hatayı attık # bize gözükür
        return s[::-1]

try:
    print(terscevir(12))
except ValueError:# hatayı yakaladık # kullanıcıyı gözükür
    print("Fonksiyon hata verdi") # hatayı konsol çıktısında verir



