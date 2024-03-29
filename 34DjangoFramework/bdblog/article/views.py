
import article
from article.models import Article,Comment
from django.shortcuts import redirect, render,HttpResponse,get_object_or_404
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.
#url gelince çalışacak fonksiyonlar


# django bölümünde 222. video yorumlarında Articel kullanırken from article.models import Article yapmalısın

def articles(request):

    keyword = request.GET.get("keyword") # name e göre "keyword"

    if (keyword):
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})
    
    articles = Article.objects.all()

    return render(request,"articles.html",{"articles":articles})


def index(request):
    context = {
        "numbers":[1,2,3,4,5,6]
    }
    return render(request,"index.html",context) # eğer template altında başka bir klasöründe altında ise article/index.html yazılmalı


def about(request):
    return render(request,"about.html")


# def detail(request,id):
#     return HttpResponse("Detail" + str(id))

@login_required(login_url="user:login")
def dashboard(request):

    articles = Article.objects.filter(author = request.user)
    context = {
        "articles" : articles
    }

    return render(request,"dashboard.html",context)
@login_required(login_url="user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if(form.is_valid()):
        
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        """
         article objesini oluşturur article.save() yapar ama user vermemiz lazım
        """
        messages.success(request,"Makale Başarıyla Oluşturuldu")
        return redirect("article:dashboard")


    return render(request,"addarticle.html",{"form":form})

def detail(request,id):
    # article = Article.objects.filter(id = id).first() # liste dönüyor tek obje dönmüyor tek obje almak için first() yazdık
    article = get_object_or_404(Article,id = id)
    comments = article.comments.all()

    return render(request,"detail.html",{"article":article,"comments":comments})
    

@login_required(login_url="user:login")
def updateArticle(request,id):

    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article) # instance içine objeyi gönderdik bilgiler article form içine yazılması için
    #instance sayesinde güncelleme sırasında önceki bilgileri aldık
    if(form.is_valid()):
        
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        """
         article objesini oluşturur article.save() yapar ama user vermemiz lazım
        """
        messages.success(request,"Makale Başarıyla Güncellendi.")
        return redirect("article:dashboard")

    return render(request,"update.html",{"form":form})

@login_required(login_url="user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)

    article.delete()

    messages.success(request,"Makale Başarıyla Silindi")

    return redirect("article:dashboard") # artilce uyg altındaki url dosyasına bakar dashboardı döner


def addComment(request,id):
    article = get_object_or_404(Article,id = id)

    if(request.method == "POST"):
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author = comment_author,comment_content = comment_content)
        newComment.article = article
        newComment.save()

    # return redirect("/articles/article/"+str(id))

    return redirect(reverse("article:detail",kwargs={"id" : id}))