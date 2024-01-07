def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True

liste = [True,False,True,False,True]


liste2 = [1,2,3,4,5]


def herhangi(liste):
    for i in liste:
        if i:
            return True
    return False

# all fonksiyonu içinde gönderilen bütün değerler true en az bir değer false ise false döndürür

all(liste) # false döner

# any bütün değerler false ise false en az bir true var ise true döner

any(liste) # true










