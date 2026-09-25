from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('home',views.index,name='homepage'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('services',views.services,name='services'),
]
