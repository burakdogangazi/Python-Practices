
#Django'nun Özellikleri
# Hızlı geliştirme ve hazır modüller
# flask kadar alışması kolay değil
# hazır admin paneli
# hazır kullanıcı modeli
# object relational mapping (orm) yapısı
# model - view - template

#Kurulum
# pip install Django==3.2.7
# django-admin --version

#Django Proje Oluşturma Ve Dosyaları

# cmd ile dosyayı oluşturacağımız bu klasöre geldik cd ile
# daha sonra 
# django-admin startproject bdblog dedik otomatik dosya oluşturdu


#Dosyalar Ve Anlamları

#manage.py dosyası terminalden çalışmamıza olanak sağlar

#__init__.py boş bir klasör bu projenin bir modul oldugunu göstermek için geliyor

#settings.py ayarların template dosyaların yolu sunucu ayarları veritabanı ayarları bulunmaktadır.
#database kısmında default sqlite3 kullandığını görüyoruz bu değiştirilebilir daha sonra

#urls.py url adreslerini verince çalışacak yerleri gösterir
#admin paneline ulaştırmak için default admin olduğunu gördük

#wsgi.py web sunucusu ayarları olan dosyadır.



#Projeye Başlamadan Önceki Ayarlar

#PS C:\Users\Burak\source\repos\Python\23DjangoFramework\bdblog> python manage.py runserver çalıştırdık 

#language code kısmından settings içinden en-us ibaresş yerine tr yazılarak server tr dilinde olur

#eğer proje bitince settings içinden DEBUG = FALSE yapılmalı ve öyle yüklenmeli

# TIME_ZONE = 'UTC' Europe yapılabilir ya da türkiye için Europe/Istanbul

#  python manage.py migrate yaptık

# python manage.py createsuperuser

# burakdogan
# ddoganbburak@gmail.com
# burak1q2w admin kurduk

#Admin paneline ulaşmak

# localhost:8000/admin diyerek ulaştık eski sürümlerde böyle bir tabel yok hatası alabiliriz
# django_session adında
# eğer hata verirse python manage.py migrate diyerek tabloları oluşturabiliriz.
#migrate kesinlikle yapılmalı ve admine girdik şifremizle


# python manage.py createsuperuser

# burakdogan
# ddoganbburak@gmail.com
# burak1q2w admin kurduk


# burakdogan2 adında 2. bir hesap kurduk django içinden bu admine erişemez
# burak1q2w admin kurduk

# ancak kullanıcın üzerine tıklayıp izinler kısmından buna izin verip süper kullanıcı yapabiliriz


# gruplar kısmından mesela editörleri etiketleyerek hepsine tek tek izin vermek yerine toplu izin verebiliriz.

# burda yazıdğımızı başka bir python projesine de entegre edebiliriz.


#Uygulama oluşturma
# python manage.py startapp article
