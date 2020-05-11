"""LoftShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
import mainapp.views as mainapp

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', mainapp.main, name='main'),
    path('products/', mainapp.products, name='products'),
    path('contact/', mainapp.contact, name='contact'),

    path("products/all", mainapp.products, name="products_all"),
    path("products/kitchen", mainapp.products, name="products_kitchen"),
    path("products/bedroom", mainapp.products, name="products_bedroom"),
    path("products/berloga", mainapp.products, name="products_berloga"),

]
