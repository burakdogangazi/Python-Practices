# filter(fonksiyon,iterasyon yapılacak bir veritipi(liste vb))

# birinci parametre olarak mantıksal değer alır sadece true değeri veren elemanları alarak filter objesi döner

list(filter(lambda x : x % 2 == 0,[1,2,3,4,5,6,7,8]))
# sadece çift sayılar ekrana gelir

# map gibi ama sadece true false kabul eder.
def asal_mi(x):
    i = 2

    if(x == 1):
        return False

    elif(x == 2):
        return True

    else:
        while(i < x):

            if(x % i == 0):
                return False
            i+=1
        return True
    
list(filter(asal_mi,range(1,100)))
#üzerinde geznebilmek iterasyon yapılabilir











