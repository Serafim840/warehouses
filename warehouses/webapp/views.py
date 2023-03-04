from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from .models import Item, Warehouse, ItemInWarehouse

def index(request):
    warehouses = Warehouse.objects.all()
    items = Item.objects.all()
    return render(request, "index.html", {'warehouses': warehouses, 'items': items})

def item(request, item_id):
    return HttpResponse(str(Item.objects.get(id=item_id)))

def warehouse_all(request, warehouse_id):
    warehouse = Warehouse.objects.get(id=warehouse_id)
    items = ItemInWarehouse.objects.filter(warehouse_id=warehouse_id)
    return render(request, "warehouse.html", {'warehouse': warehouse, 'items': items})

def warehouse_count(request, warehouse_id):
    warehouse = Warehouse.objects.get(id=warehouse_id)
    items = ItemInWarehouse.objects.filter(warehouse_id=warehouse_id).annotate(item_count=Count('item'))
    return render(request, "warehouse.html", {'warehouse': warehouse, 'items': items, 'count': True})