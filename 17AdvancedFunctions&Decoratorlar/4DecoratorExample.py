def ekstra(fonk):

    def wrapper(sayılar):
        çiftler_toplamı = 0
        çift_sayılar = 0
        tekler_toplamı = 0
        tek_sayılar = 0

        for sayı in sayılar:

            if(sayı % 2 == 0):
                çiftler_toplamı += sayı
                çift_sayılar +=1
            else:
                tekler_toplamı +=sayı
                tekler_toplamı += 1

        print("Teklerin ortalaması : ",tekler_toplamı/tek_sayılar)
        print("Çiftlerin toplamı : ",çiftler_toplamı/çift_sayılar)

        fonk(sayılar)

    return wrapper




@ekstra
def ortalamabul(sayılar):
    toplam = 0

    for sayı in sayılar:
        toplam += sayı

    print("Genel Ortalama : ",toplam/len(sayılar))
































