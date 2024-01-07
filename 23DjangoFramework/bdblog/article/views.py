from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("Anasayfa") #urls gidiyoruz

    # context = { # sözlük yapısı

    #     "number1":10,
    #     # "number2":20,
    #     "numbers" : [1,2,3,4,5,6]
    # }
    # return render(request,"index.html",context) # bir dosya altı olursa article/index.html diyebiliriz.
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

# def detail(request,id):# dinamik url yapısı
#     return HttpResponse("Detail:"+ str(id))
