def anafonksiyon(işlem_adı):
    
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam +=i
        return toplam

    def carpım(*args):
        carpım  = 1
        for i in args:
            carpım*=i
        return carpım

    if(işlem_adı == "toplama"):
        return toplama
    else:
        return carpım


fonk = anafonksiyon("toplama")

fonk(1,2,3,4,5)

fonk2 = anafonksiyon("carpım")

fonk2(2,3,4,5,6)

def toplama(a,b):
    return a+b
def cıkarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def anafonksiyon1(func1,func2,func3,func4,işlem_adı):

    if(işlem_adı  == "toplama"):
        print(func1(3,4))
    elif(işlem_adı == "cıkarma"):
        print(func2(4,6))
    elif(işlem_adı == "carpma"):
        print(func3(3,5))    
    elif(işlem_adı == "bolme"):
        print(func3(14,7))  
    else:
        print("Geçersiz.")


anafonksiyon(toplama,cıkarma,carpma,bolme,"toplama")










