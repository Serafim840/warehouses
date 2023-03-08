from django.contrib import admin

from .models import Item, Warehouse, Stock

admin.site.register([Item, Warehouse, Stock])
