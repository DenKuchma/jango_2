"""mydz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path
from dz.views import main, main1, main2, main3, main4, main5, main6, main7, main8, main9

urlpatterns = [
    path('', main),
    path('acricles/', main1),
    path('acrticles/archive/', main2),
    path('users', main3),
    path('article/<int:article_number>/', main4),
    path('article/<int:article_number>/archive', main5),
    path('article/<int:article_number>/<slug:slug_text>/', main6),
    path('users/<int:user_number>/', main7),
    re_path(r'^(?P<regular>[1-9a-f]{4}[-]{1}.{6}$)', main8),
    re_path(r'^(?P<regular2>[0]{1}[3-6]{1}[0-9]{1}\d{7}$)', main9)
]
