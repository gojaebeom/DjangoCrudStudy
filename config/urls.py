"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from post import views

urlpatterns = [
    path('posts/', views.index),
    path('posts/<int:id>', views.show),
    path('posts/create', views.create),
    path('posts/store', views.store),
    path('posts/<int:id>/update', views.update),
    path('posts/<int:id>/edit', views.edit),
    path('posts/<int:id>/destroy', views.destroy),
]
