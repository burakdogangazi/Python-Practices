from django.db import models

# Create your models here.

class Article(models.Model):
    # user tablosu hazır gelir buna atıfta bulunmak için foreignkey bu alan user tablosunu işaret ediyor
    # auth.User tablosundan bir foreign key oluşturduk o tabloya yazarsak buraya gelir bu user silidniği zaman buna ait tablo vb silinsin anlamında ondelete yaptık.
    # auth.user işaret eden veritabanında eğer burakdogan2 yi silersek onun oluşturduğu articleları da sileriz
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar") # bu alan user tablosunu işaret eder ve delete models ile user silinince bu da silinsin dedik
    title = models.CharField(max_length=50,verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")# veri eklenince o anki tarihi ekler
    # modeli admin de kayıt ediyoruz.
    # id koymadık ama 0001 inital py altında otomatik oluşur

    def __str__(self):
        return self.title # adminde article de article object1 yerine title bilgisi gösterilecek.



