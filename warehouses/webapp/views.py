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
    results = ItemInWarehouse.objects.filter(warehouse_id=warehouse_id).select_related('item')
    return render(request, "warehouse.html", {'warehouse': warehouse, 'results': results, 'count': False})

def warehouse_count(request, warehouse_id):
    warehouse = Warehouse.objects.get(id=warehouse_id)
    results = ItemInWarehouse.objects.filter(warehouse_id=warehouse_id).values('item', 'item__country', 'item__brand', 'item__model').annotate(item_count=Count('item'))
    return render(request, "warehouse.html", {'warehouse': warehouse, 'results': results, 'count': True})

