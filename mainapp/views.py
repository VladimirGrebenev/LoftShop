from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.utils import timezone

from basketapp.models import Basket

from .models import Product, ProductCategory, Contact

import random


# Create your views here.
def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:4]
    return same_products


def main(request):
    title = "главная"
    links_menu = ProductCategory.objects.all()

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        # or you can use this
        # _basket = request.user.basket.all()
        # print(f'basket / _basket: {len(_basket)} / {len(basket)}')

    products = Product.objects.all()[:4]
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {"title": title, "products": products, "media_url": settings.MEDIA_URL, "basket": basket,
               "links_menu": links_menu, "hot_product": hot_product, "same_products": same_products,}
    return render(request, "mainapp/index.html", content)


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def products(request, pk=None):
    title = "товары"
    links_menu = ProductCategory.objects.all()

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        # or you can use this
        # _basket = request.user.basket.all()
        # print(f'basket / _basket: {len(_basket)} / {len(basket)}')

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by("price")
            category = {"name": 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by("price")
        content = {
            "title": title,
            "links_menu": links_menu,
            "category": category,
            "products": products,
            "media_url": settings.MEDIA_URL,
            "basket": basket,
        }
        return render(request, "mainapp/products_list.html", content)

    products = Product.objects.all()
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        "title": title,
        "links_menu": links_menu,
        "same_products": same_products,
        "products": products,
        "media_url": settings.MEDIA_URL,
        "basket": basket,
        "hot_product": hot_product,
    }

    if pk:
        print(f"User select category: {pk}")
    return render(request, "mainapp/shop-sidebar.html", content)


def contact(request):
    title = "о нас"
    links_menu = ProductCategory.objects.all()

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        # or you can use this
        # _basket = request.user.basket.all()
        # print(f'basket / _basket: {len(_basket)} / {len(basket)}')

    visit_date = timezone.now()
    locations = Contact.objects.all()
    content = {"title": title, "visit_date": visit_date, "locations": locations, "basket": basket,
               "links_menu": links_menu, }
    return render(request, "mainapp/contact.html", content)

def product(request, pk):
    title = "товары"
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    content = {
        "title": title,
        "links_menu": ProductCategory.objects.all(),
        "product": get_object_or_404(Product, pk=pk),
        "basket": get_basket(request.user),
        "media_url": settings.MEDIA_URL,
        "hot_product": hot_product,
        "same_products": same_products,
    }
    return render(request, "mainapp/product.html", content)