# Iteratorlar Nedir
# For döngüleri ve list comp ,generatorlarda kullanılır
# en genel anlamıyla üzerinde gezinilebliecek bir objedir ve bu obje her seferinde bir tane eleman döner
# pythonda kendisinden iterator oluşturabileceğimiz her obje iterable bir objedir demetlerden ,listelerden,ve stringlerden oluşan
# bütün objeler iterable bir objedir.

# iterator objesini iterable bir obnjeden oluşturmak için iter() fonk kullanıyoruz
# objenin sonraki elemanını almak için next kullanıyoruz.

liste = [1,2,3,4,5]
dir(liste) # liste metodları gözükür biz iterle ilgileniyoruz.

iterator = iter(liste)

print(iterator)

next(iterator) # 1 yazar ilk eleman
next(iterator) # 2 olur
# en son 5 yazar bir kere daha yazarsan stopiteration hatası verir.


liste1 = [1,2,3,4,5,6]

for i in liste1: # python kendi içinde iteratorler kullanıyor
    print(i)

# Aşağıdaki algoritma for un kendi içinde python içindeki algoritması
iterator1 = iter(liste1)

while True:
    try:
        print(next(iterator))

    except StopIteration:
        break


#Kendi Iterable Objelerimizi Oluşturmak
#Sınıflarda iter ve next metodları tanımlanması gerekir.


class Kumanda():
    
    def __init__(self,kanal_listesi):
        
        self.kanal_listesi = kanal_listesi

        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        
        self.index += 1

        if(self.index < self.kanal_listesi):

            return self.kanal_listesi[self.index]
        
        else:

            self.index = -1

            raise StopIteration


kumanda = Kumanda(["Fox","Atv","TRT","Kanald","Habertürk"])

iterator = iter(kumanda)

next(iterator)

for i in kumanda:
    print(i) # normalde obje üzerinde çalışmaz ama kendi yazarsak dönebildik.












