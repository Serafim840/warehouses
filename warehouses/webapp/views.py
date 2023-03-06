from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count
from django.urls import reverse
from .models import Item, Warehouse, ItemInWarehouse

def index(request):
    warehouses = Warehouse.objects.all()
    items = Item.objects.all()
    return render(request, "index.html", {'warehouses': warehouses, 'items': items})

def item(request, item_id):
    result = get_object_or_404(Item, pk=item_id)
    return HttpResponse(str(result))

def create_item(request):
    if request.method == 'GET':
        return render(request, "create_item.html")
    elif request.method == 'POST':
        try:
            new_item = Item.objects.create(
                brand=request.POST['brand'],
                country=request.POST['country'],
                model=request.POST['model']
            )
        except KeyError:
            return render(request, "create_item.html")
        else:
            new_item.save()
            return HttpResponseRedirect(reverse('item info', args=(new_item.pk,)))

def warehouse_all(request, warehouse_id):
    warehouse = get_object_or_404(Warehouse, pk=warehouse_id)
    results = ItemInWarehouse.objects.filter(warehouse_id=warehouse_id).select_related('item')
    return render(request, "warehouse.html", {'warehouse': warehouse, 'results': results, 'count': False})

def warehouse_count(request, warehouse_id):
    warehouse = get_object_or_404(Warehouse, pk=warehouse_id)
    results = ItemInWarehouse.objects.filter(warehouse_id=warehouse_id).values('item', 'item__country', 'item__brand', 'item__model').annotate(item_count=Count('item'))
    return render(request, "warehouse.html", {'warehouse': warehouse, 'results': results, 'count': True})

