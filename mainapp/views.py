from django.shortcuts import render
import datetime

# Create your views here.

def main(request):
    title = "главная"
    products = [
        {
            "name": "Диван Медведь",
            "desc": "Комплект Берлога Сибирская",
            "image_src": "image-300-400-1.jpg",
            "image_href": "/product/1/",
            "alt": "продукт 1",
            "price": "$ 25.00–$ 29.00",
        },
        {
            "name": "Барная стойка Дуб",
            "desc": "Идеальный вариант для вашей кухни",
            "image_src": "image-300-400-2.jpg",
            "image_href": "/product/2/",
            "alt": "продукт 2",
            "price": "$ 55.00–$ 69.00",
        },
        {
            "name": "Обеденный стол",
            "desc": "Коллекция В большой семье ...",
            "image_src": "image-300-400-3.jpg",
            "image_href": "/product/3/",
            "alt": "продукт 2",
            "price": "$ 75.00–$ 99.00",
        },
        {
            "name": "Полка что надо",
            "desc": "Не то что надо, а нужно!",
            "image_src": "image-300-400-4.jpg",
            "image_href": "/product/4/",
            "alt": "продукт 2",
            "price": "$ 15.00–$ 29.00",
        },
    ]
    content = {"title": title, "products": products}
    return render(request, 'mainapp/index.html', content)


def products(request):
    title = "продукты"
    links_menu = [
        {"href": "products_all", "name": "все"},
        {"href": "products_kitchen", "name": "кухни"},
        {"href": "products_bedroom", "name": "спальни"},
        {"href": "products_berloga", "name": "берлоги"},
    ]
    same_products = [
        {
            "name": "Диван Медведь",
            "desc": "Комплект Берлога Сибирская",
            "image_src": "image-300-400-1.jpg",
            "image_href": "/product/1/",
            "alt": "продукт 1",
            "price": "$ 25.00–$ 29.00",
        },
        {
            "name": "Барная стойка Дуб",
            "desc": "Идеальный вариант кухни",
            "image_src": "image-300-400-2.jpg",
            "image_href": "/product/2/",
            "alt": "продукт 2",
            "price": "$ 55.00–$ 69.00",
        },
        {
            "name": "Обеденный стол",
            "desc": "Коллекция В большой семье ...",
            "image_src": "image-300-400-3.jpg",
            "image_href": "/product/3/",
            "alt": "продукт 2",
            "price": "$ 75.00–$ 99.00",
        },
        {
            "name": "Полка что надо",
            "desc": "Не то что надо, а нужно!",
            "image_src": "image-300-400-4.jpg",
            "image_href": "/product/4/",
            "alt": "продукт 2",
            "price": "$ 15.00–$ 29.00",
        },
    ]
    content = {"title": title, "links_menu": links_menu, "same_products": same_products}
    return render(request, 'mainapp/shop-sidebar.html', content)


def contact(request):
    title = "о нас"
    visit_date = datetime.datetime.now()
    locations = [
        {"city": "Москва", "phone": "+7-888-888-8888", "email": "info@geekshop.ru", "address": "В пределах МКАД"},
        {
            "city": "Екатеринбург",
            "phone": "+7-777-777-7777",
            "email": "info_yekaterinburg@geekshop.ru",
            "address": "Близко к центру",
        },
        {
            "city": "Владивосток",
            "phone": "+7-999-999-9999",
            "email": "info_vladivostok@geekshop.ru",
            "address": "Близко к океану",
        },
    ]
    content = {"title": title, "visit_date": visit_date, "locations": locations}
    return render(request, 'mainapp/contact.html', content)
