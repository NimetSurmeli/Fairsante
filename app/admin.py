from django.contrib import admin
from app.models import Product, Ingredient


class ProductAdmin(admin.ModelAdmin):
    list_display = ['brand' , 'pname']
    list_display_links = ['pname']
    list_filter = ['brand']

    class Meta:
        model = Product

class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name' , 'rate']
    list_filter = ['rate']

admin.site.register(Product, ProductAdmin)
admin.site.register(Ingredient, IngredientAdmin)