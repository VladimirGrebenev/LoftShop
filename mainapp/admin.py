from django.contrib import admin
from .models import ProductCategory, Product, Contact


# Register your models here.

# admin.site.register(ProductCategory)
# admin.site.register(Product)

# admin.site.register(Contact)

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_display_links = ("name",)

@admin.register(Product)
class ProductAdmin (admin.ModelAdmin):
    list_display = ("id", "name", "category", "price", "quantity")
    list_display_links = ("name",)
    list_filter = ("category", "name", "price", "quantity")
    search_fields = ("name",)
    save_on_top = True
    save_as = True

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("city", "phone", "email", "address")
    list_display_links = ("city", "phone", "email", "address")
    list_filter = ("city",)
    search_fields = ("city", "phone", "email", "address")
    save_on_top = True
    save_as = True


admin.site.site_title = 'LoftShop GeekBrains'
admin.site.site_header = 'LoftShop GeekBrains'
