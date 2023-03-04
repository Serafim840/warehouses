from django.contrib import admin

from .models import Item, Warehouse

admin.site.register([Item, Warehouse])
