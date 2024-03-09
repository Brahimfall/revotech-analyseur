from django.contrib import admin
from django.urls import path, include

from contact import views

urlpatterns = [
    path('',views.contact,name='contact'),


]