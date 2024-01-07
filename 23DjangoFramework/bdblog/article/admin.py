from django.contrib import admin

# Register your models here.

from .models import Article

# admin.site.register(Article) ya da decorator ile
# siteyi kayıt ettik article içinde ama bdblog djangoya söylemedik settingse gidelim.
# settings installed apps kısmından gösterdik.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    #DjangoAdmin Dökümanından daha fazla özelliğe bakabiliriz.
    list_display = ["title","author","created_date"] # adminde sadece title değil author da gözükür

    list_display_links = ["title","created_date"] # tıklanabilir yaptık article ulaşmak için

    search_fields = ["title"] # title bilgisine göre arama

    list_filter = ["created_date"] # süzgeç koyduk tarihe göre


    #Terminal ORM Yapısı SHELL
    # Sıradaki adımda shell yapısı orm sorgular için yeni terminale python manage.py shell yazabiliriz.

    #In [2]: from django.contrib.auth.models import User   

    #In [3]: from article.models import Article

    # User Article yazarak yapıyı görebiliriz

    # bu satırlar sayesinde artık orm için objeler oluşturabilecez

    # 1. Yöntem
    #newUser = User(username = "denemekullanıcı",password = "123")

    # newUser

    # newUser.save() kullanıcı oluştu denemekullanici adında ama veritabanında şifrelemek lazım

    #2. Yöntem
    # In [9]: newUser2 = User(username = "denemekullanici2")

    # In [10]: newUser2.set_password("123")

    # In [11]: newUser2.save()

    #3.Yöntem

    # In [12]: newUser3 = User()

    # In [13]: newUser3.username = "denemekullanici3"

    # In [14]: newUser3.set_password("123")

    # In [15]: newUser3.first_name="Burak"

    # In [16]: newUser3.save()

    #Terminal Article oluşturmak

    #1.Yöntem
    # In [17]: article = Article(title = "Django Shell Deneme",content = "İçerik İçerik",author = newUser3)

    # In [18]: article.save()

    #2.Yöntem

    # In [19]: article2 = Article()

    # In [20]: article2.title = "Deneme15"

    # In [21]: article2.content = "contentiçerik"

    # In [22]: article2.author = newUser3

    # In [23]: article2.save()

    #3.yöntem

    # In [25]: Article.objects.create(title = "Deneme21",content = "icerik21",author = newUser2)
    # Out[25]: <Article: Deneme21> değerini döndü

    #4.yöntem

    # article = Article.objects.create(title = "Deneme31",content = "icerik31",author = newUser2)

    # In [27]: article.title
    # Out[27]: 'Deneme31'

    #In [28]: article.title = "Deneme 31 değişti"

    # In [29]: article.save()


    #Objeleri almak

    # In [30]: Article.objects.all()
    # Out[30]: <QuerySet [<Article: Deneme1>, <Article: Naber>, <Article: deneme2>, <Article: Django Shell Deneme>, <Article: Deneme15>, <Article: Deneme21>, <Article: Deneme 31 değişti>]>

    # In [33]: Article.objects.get(title = "Deneme21")
    # Out[33]: <Article: Deneme21>

    # In [34]: article = Article.objects.get(title = "Deneme21")      

    # In [35]: article.title
    # Out[35]: 'Deneme21'

    #Article Silmek Veritabanından

    # In [36]: article.delete()
    # Out[36]: (1, {'article.Article': 1})

    # In [40]: article = Article.objects.get(id = 7)

    # In [41]: article
    # Out[41]: <Article: Deneme15>

    # In [42]: article.delete()
    # Out[42]: (1, {'article.Article': 1})


    #Article Filtrelemek
    
    # In [43]: Article.objects.filter(title__contains = "Den")        
    # Out[43]: <QuerySet [<Article: Deneme1>, <Article: deneme2>, <Article: Django Shell Deneme>, <Article: Deneme 31 değişti>]>

    # In [44]: Article.objects.filter(title__contains = "She")        
    # Out[44]: <QuerySet [<Article: Django Shell Deneme>]>
    # Makale ekleyip silmede kullanılabilir

    #Daha fazla djangoproject.com/makingqueries

    # settings Templates dirs kısmına gidelim

    class Meta: # article admin ile article bağlamak için django sınıfı
        model = Article
