from django.contrib import admin
from django.urls import path, include

from acceuil import views

urlpatterns = [
    path('',views.acceuil,name='acceuil'),


]