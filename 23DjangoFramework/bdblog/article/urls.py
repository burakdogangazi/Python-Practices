from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path
from article import views


app_name = "article"
# bu url sayesinde ana dizinde sadece /articles yazarak ve include ederek burayı oraya katarız 

urlpatterns = [
    path('create/',views.index,name = "index"),
]


