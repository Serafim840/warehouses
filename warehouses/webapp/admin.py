from django.contrib import admin

from .models import Item, Warehouse, ItemInWarehouse

admin.site.register([Item, Warehouse, ItemInWarehouse])
