from django.contrib import admin
from .models import productTable

# Register your models here.
class Products(admin.ModelAdmin):
    list_view = ('prod_name', 'prod_price', 'image')

admin.site.register(productTable, Products)

# Superuser credentials
# username: Krisia
# password: grande123