from django.contrib import admin
from django.urls import path
from bookmark import views
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='index'),
]