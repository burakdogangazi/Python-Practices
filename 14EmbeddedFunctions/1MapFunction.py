# map(fonksiyon,iterasyon,tapılabilecek veritipi(liste,demet,vb))
#map objesi şeklinde döner


def double(x):
    return x*2
# her bir liste elemanına 1,2,3,4,5,6,7 double fonksiyonunu uygular sonucu map objesi şeklinde döner.

list(map(double,[1,2,3,4,5,6,7])) # sonucu list olarak döndürdük.

list(map(lambda x : x **2,(1,2,3,4,5,6,7,8)))

liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste3 = [9,10,11,12,13]

list(map(lambda x,y : x*y,liste1,liste2)) #1*5 çarpıp liste oluşturduk

list(map(lambda x,y,z : x*y*z,liste1,liste2,liste3))
# 13 almıyor çükü x ve y de yok çarpmada sadece 4 değerli list ortaya çıkıyor













