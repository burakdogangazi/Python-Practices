from logging import log
import re
from MySQLdb.cursors import Cursor
from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL, MySQLdb
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.handlers.sha2_crypt import sha256_crypt
from functools import wraps

#Searchbox snippets
# https://bootsnipp.com/snippets/9bA4


# CKEditör
# scripti eklerken bizim özelliğimizin textareanın name özelliği content olduğu için content yazdık


#Makaleler Veritabanı oluşturma bdblog içinde
# id int A_I title text author text content text created_date timesatamp current_time


#Dinamik Url yapısı
# BİZ localhost:5000/article/54 diyerek veritabanından dinamik url alabiliriz


#Gerekli Moduller ve Mysql Veritabanı oluşturma
# pip install flask-mysqldb
# pip install Flask-WTF
# pip install passlib
# pip install email_validator
# phpmyadmin açtık ve users adına utf8_general_ci ile tablo oluşturduk bdblog adında
# id belirdledik A_I yı açtık isme id türüne int indexe primary verdik unique olması için
# name text yaptık türü
# email text yaptık türü
# username text yaptık türü
# password text yaptık türü
# app.configleri yazdık
#Mysql objesini oluşturduk içine app yollayarak


# Kullanıcı Giriş decorator
def login_required(f): # dashboard f yerine gelcek
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if("logged_in") in session: # giriş yapmışsa
            return f(*args,**kwargs)
        
        else:
            flash("Bu sayfayı görüntülemek için lütfen giriş yapın.","danger")
            return redirect(url_for("login"))
    
    return decorated_function

#Kullanıcı Kayıt Formu WTForms ile

class RegisterForm(Form):
    name = StringField("İsim Soyisim",validators=[validators.length(min = 4,max = 25)])
    username = StringField("Kullanıcı Adı",validators=[validators.length(min = 5,max = 35)])
    email = StringField("Email Adresi",validators=[validators.Email(message = "Lütfen geçerli bir Email adresi girin.")])
    password = PasswordField("Parola:",validators=[
        validators.DataRequired(message="Lütfen bir parola belirleyin"),
        validators.EqualTo(fieldname="confirm",message="Parolanız Uyuşmuyor..")
    ])
    confirm = PasswordField("Parola Doğrula")
    # confirm password karşılaştırır doğruysa işlem kabul olur

# WTForms ile Login Form yapmak
class LoginForm(Form):

    username = StringField("Kullanıcı Adı")
    password = PasswordField("Parola")




app = Flask(__name__)

app.secret_key ="bdblog"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORDT"] = ""
app.config["MYSQL_DB"] = "bdblog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)



@app.route("/")
def index():

    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/articles")
def articles():
    
    cursor = mysql.connection.cursor()

    sorgu = "Select * From articles"

    result = cursor.execute(sorgu)# hiç makale yoksa 0 gelir

    if(result > 0):

        articles = cursor.fetchall()

        return render_template("articles.html",articles = articles)

    else:
        return render_template("articles.html") # veri göndermiyoruz makale yok





@app.route("/dashboard")
@login_required
def dashboard():

    cursor = mysql.connection.cursor()

    sorgu = "Select * From articles where author = %s"

    result = cursor.execute(sorgu,(session["username"],))

    if (result > 0):
        articles = cursor.fetchall()
        return render_template("dashboard.html",articles = articles)

    else:
        return render_template("dashboard.html")


    

#Kayıt Olma
@app.route("/register",methods = ["GET","POST"]) # hem getrequest hem post request alır
def register():

    form = RegisterForm(request.form)

    if(request.method == "POST" and form.validate()):

        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)

        cursor = mysql.connection.cursor()

        sorgu = "Insert into users(name,email,username,password) VALUES(%s,%s,%s,%s)"

        cursor.execute(sorgu,(name,email,username,password)) # name %s emnail %s öyle yerine geçer

        mysql.connection.commit() # bilgi çekerken yapmak zorunlu değil ama güncellenecekse commit yapılmak zorunda

        cursor.close()

        flash("Başarıyla Kayıt Oldunuz...","success")

        #cursor.execute(sorgu,(name,)) virgül koymanın sebebi programın gönderilen değeri demet olarak anlaması için

        return redirect(url_for("login")) #ilişkili redirect anasayfa gider indexe

    else:
        return render_template("register.html",form = form)#direk register html gönderir



#Aşağıdaki örnek Flask Dinamik Url Yapısını yansıtır
# @app.route("/article/<string:id>") # article ın yanıa gelecek şeyin string olduğunu ve id adıyla tutulduğu bilgisi
# def detail(id):

#     return "Article Id : " + id

#Login İşlemi

@app.route("/login",methods = ["GET","POST"])
def login():
    form = LoginForm(request.form)

    if(request.method == "POST"):

        username = form.username.data
        password_entered = form.password.data


        cursor = mysql.connection.cursor()

        sorgu = ("Select * From users where username  = %s")

        result = cursor.execute(sorgu,(username,)) # yoksa 0 döner var ise farklı pozitif sayı

        if(result > 0):

            data = cursor.fetchone() # tüm bilgileri aldık

            real_password = data["password"]  

            if (sha256_crypt.verify(password_entered,real_password)):
                flash("Başarı ile giriş yaptınız.","success")  
                
                session["logged_in"] = True

                session["username"] = username

                return redirect(url_for("index"))        

            else:
                flash("Parolanızı yanlış girdiniz.","danger")
                return redirect(url_for("login"))

        else:
            flash("Böyle bir kullanıcı bulunmuyor..","danger")
            return redirect(url_for("login"))


    return render_template("login.html",form = form)


#Detay Sayfası

@app.route("/article/<string:id>")
def article(id):

    cursor = mysql.connection.cursor()

    sorgu = "Select * From articles where id = %s"

    result = cursor.execute(sorgu,(id,))

    if(result > 0):
        
        article = cursor.fetchone()
        return render_template("article.html",article = article)

    else:
        return render_template("article.html")




#Logout İşlemi
@app.route("/logout")
def logout():
    
    session.clear()
    return redirect(url_for("index"))


#Makale Ekleme
@app.route("/addarticle",methods = ["GET","POST"])
def addarticle():

    form = ArticleForm(request.form)

    if (request.method == "POST" and form.validate()):
        title = form.title.data
        content = form.content.data

        cursor = mysql.connection.cursor()

        sorgu = "Insert into articles(title,author,content) VALUES(%s,%s,%s)"

        cursor.execute(sorgu,(title,session["username"],content))

        mysql.connection.commit()

        cursor.close()

        flash("Makale başarıyla eklendi.","success")

        return redirect(url_for("dashboard"))
    
    return render_template("addarticle.html",form = form)


# Makale Silme

@app.route("/delete/<string:id>")
@login_required
def delete(id):

    cursor = mysql.connection.cursor()

    sorgu = "Select * from articles where author = %s and id = %s"

    result = cursor.execute(sorgu,(session["username"],id))

    if(result > 0):
        
        sorgu2 = "Delete from articles where id = %s"

        cursor.execute(sorgu2,(id,))

        mysql.connection.commit()

        return redirect(url_for("dashboard"))

    else:
        flash("Böyle bir makale yok veya bu işlemi yetkiniz yok.")
        return redirect(url_for("index"))


#Makale Güncelle
@app.route("/edit/<string:id>",methods = ["GET","POST"])
@login_required
def update(id):

    if(request.method == "GET"):
        cursor = mysql.connection.cursor()
        
        sorgu = "Select * from articles where id = %s and author = %s"

        result = cursor.execute(sorgu,(id,session["username"]))

        if(result == 0):
            flash("Böyle bir makale yok veya bu işleme yetkiniz yok","danger")
            return redirect(url_for("index"))
        else:
            
            article = cursor.fetchone()
            form = ArticleForm()
            # form wtf ile yapmadık kendi bilgilerimizi içine gönderdik
            # data ile çünkü önceki yazı vebaşlık gelsin onları güncellesin diye
            form.title.data = article["title"]
            form.content.data = article["content"]

            return render_template("update.html",form = form)

        
    else:
        #Post request kısmı

        form = ArticleForm(request.form)

        newTitle = form.title.data

        newContent = form.content.data

        sorgu2 = "Update articles Set title = %s,content = %s where id = %s"

        cursor = mysql.connection.cursor()

        cursor.execute(sorgu2,(newTitle,newContent,id))

        mysql.connection.commit()

        flash("Makale başarıyla güncellendi","success")

        return redirect(url_for("dashboard"))       

#Makale Form
class ArticleForm(Form):
    
    title = StringField("Makale Başlığı",validators=[validators.Length(min = 5,max=100)])
    content = TextAreaField("Makale İçeriği",validators=[validators.Length(min = 10)])


#Arama URL
@app.route("/search",methods = ["GET","POST"])
def search():

    if(request.method == "GET"): # eğer direk url çubuğuunda /search diye aratırsa get vermesin dedik
        return redirect(url_for("index"))

    else:
        keyword = request.form.get("keyword") #  articles içinde input keyword olan yeri alır
        
        cursor = mysql.connection.cursor()

        sorgu = "Select * from articles where title like '%" + keyword + "%' "

        result = cursor.execute(sorgu)

        if(result == 0):
            flash("Aranan kelimeye uygun makale bulunamadı.","warning")
            return redirect(url_for("articles"))

        else:
            articles = cursor.fetchall()

            return render_template("articles.html",articles = articles)


if(__name__ == "__main__"):
    app.run(debug=True)















