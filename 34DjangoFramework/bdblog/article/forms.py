from django import forms
from .models import Article #input alanı için
class ArticleForm(forms.ModelForm):
    class Meta:# hazır input alanı için django doc bak
        model = Article
        fields = ["title","content","article_image"]

