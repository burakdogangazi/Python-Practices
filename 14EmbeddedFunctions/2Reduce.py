# reduce(fonksiyon,iterasyon yapılabilecel veritipi(demet,liste,vb))

from functools import reduce

def toplama(x,y):
    return x+y

reduce(toplama,[12,18,16,10])
#12 ve 18 toplanıyor daha sonra 30 ile 16 toplamaya gönderilıyor daha sonra 46 10 ile toplama fonksiyonuna gidip 56 basar


reduce(lambda x,y : x*y , [1,2,3,4,5])
# 1*2  = 2 olur 2 *3 = 6  6*4 = 24 olur ve 24*5 =120 cevaptır.



def maksimum(x,y):
    if(x>y):
        return x
    else:
        return y

maksimum(3,4)

reduce(maksimum,[-2,-3,-4,-5,10,20])










