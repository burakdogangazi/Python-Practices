
from flask import Flask,render_template # web sunucunu oluşturmak için


app = Flask(__name__)

@app.route("/") # bu bir reposne için flaskta hazır decorator bunun hemen altına yazmak zorudnayız fonksiyonu
def index():

    #Template Inheritance ve Bloklar
    #Layout.html oluşturduk
    # index2.html e extends ediyoruz layoutu index2.html django template olmalı
    #index2.html sadece layoutu extends ediyor ama layout içindeki yazılıyor 
    # eğer biz extends yapmak istiyoruz ama bir yeri değiştirmek istiyoruz
    # değiştirmek istediğimiz kısmı overwrite etmiş oluyoruz blok kullanarak index2 de yeniden yazıyoruz.
    # ana html sayfamızda title blok yapısında yaptık ve index2 de blok yapısı sayesinde değiştirebildik extends ile
    return render_template("index2.html")

    #Sözlük Göndermek
    # article = dict()
    # article["title"] = "Deneme"
    # article["body"] = "Deneme 123"
    # article["author"] = "Burak Doğan"
    # return render_template("index.html",article = article)
   
    #Sayı Göndermek
    # sayi = 10
    # sayi2 = 20
    # return render_template("index.html",number = sayi,number2 = sayi2) # index html response dedik
    # bu numberı index.html içinde kullandık
    
    
    #String Göndermek
     # return "Ana Sayfa" # response dönmüş olduk

    #Bilgiler
    #templates dosyası içinde index.html içine baktı

@app.route("/about")
def about():
    return "Hakkımda" # yazınca çıktı http://localhost:5000/about

@app.route("/about/burak")
def burak():
    return "Burak Hakkında" #http://localhost:5000/about/burak


if(__name__ == "__main__"):
    app.run(debug = True) # hata olunca hata mesajı göstersin debug = true




# terminalden çalıştırmak istersen __name__ değeri main oluyor
# ama başka bir dosyadan modulden alırsak main olmuyor onu kontrol etmiş oluyoruz

# cd ile kurulu olan dsoyaya gidip python 2blog.py  yazıp server çalıştırıyoruz.
#ctrl + c local host durur localhost:5000 yazarak url yerine girdik





