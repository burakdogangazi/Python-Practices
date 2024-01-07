#Generatorlar

#Iterable objeler oluşturmak için kullanılan objelerdir bellekte yer kaplamıyorlar
#Eğer 100000 tane değeri listede tutmak çok fazla bellek harcar bu yüzden generator şeklinde yazmak mantıklı olacaktır. Hiç bellek kaplamaz.

# Çok fazla sayıda iş yaparsak bunları listede tutmak mantıklı değildir
def kareleri_al():
    sonuc = list()

    for i in range(1,6):
        sonuc.append(i **2)

    return sonuc


def kareleri_alg():

    for i in range(1,6):

        yield i ** 2

generator = kareleri_alg()


iterator = iter(generator)

next(iterator) # normalde direk çalışıp tutmaz biz next diyince 
# üretir o anlık kullanır ve bir daha next der isek ilk değer ulaşılamaz.

next(iterator)


iterator2 = iter(generator)

next(iterator2) # yeniden yaparsak 
# ve daha önce o değer maxlanmış ve stopıteration sıfatı alınmışşsa
# 2. kez oluşturduğumuz iterator de o yerden devam eder ve o hatayı verir
# generator işi bitmiştir daha fazla yield ile ugrasmaz.



#List comp

liste = [i*3 for i in range(5)]

generator1 = (i*3 for i in range(5))


iterator = iter(generator1)

next(generator)


def carpımtablosu():

    for i in range(1,11):
        for j in range(1,11):
            yield("{} x {} = {}".format(i,j,i*j))


for i in carpımtablosu():
    print(i) 

# range generator ile kullanılır
# generatorlar sadece o anda üretlip kullanılır hafıza kullanmaz.