"""localcommunity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


from . import views
urlpatterns = [

    path('',views.index),
    path('search/', views.search, name='search'),
    path('add/',views.serviceadd,name="serviceadd"),
    path('contact/',views.contactView,name='contact'),
    path('success/', views.successView, name='success'),
    path('serviceHome', views.serviceHome, name="serviceHome"),
    path('postComment',views.postComment,name="postComment"),
    path('<str:slug>', views.servicePost, name="servicePost"),
    path('aboutUs/',views.aboutUs,name='aboutUs')

]

