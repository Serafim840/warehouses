from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Count
from django.urls import reverse
from .models import Item, Warehouse, Stock, StockForm
from django.forms import modelformset_factory


def index(request):
    warehouses = Warehouse.objects.all()
    items = Item.objects.raw(
        """
        SELECT it.id, it.brand, it.model, it.country, COUNT(iw.id) as item_count 
        FROM webapp_Item it 
        LEFT JOIN webapp_ItemInWarehouse iw 
        ON it.id = iw.item_id 
        GROUP BY it.id
        """
    )

    return render(request, "index.html", {"warehouses": warehouses, "items": items})


def item_all(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    results = Stock.objects.filter(item_id=item_id).select_related(
        "warehouse"
    )
    return render(
        request, "item.html", {"item": item, "results": results, "count": False}
    )


def item_count(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    results = Item.objects.get(id=item_id).warehouse_set.annotate(
        item_count=Count("id")
    )
    return render(
        request, "item.html", {"item": item, "results": results, "count": True}
    )

def create_item(request):
    if request.method == "GET":
        return render(request, "create_item.html")
    elif request.method == "POST":
        try:
            new_item = Item.objects.create(
                brand=request.POST["brand"],
                country=request.POST["country"],
                model=request.POST["model"],
            )
        except KeyError:
            return render(request, "create_item.html")
        else:
            new_item.save()
            return HttpResponseRedirect(reverse("item info", args=(new_item.pk,)))


def warehouse_all(request, warehouse_id):
    warehouse = get_object_or_404(Warehouse, pk=warehouse_id)
    results = Stock.objects.filter(warehouse=warehouse).select_related("item")
    return render(
        request,
        "warehouse.html",
        {"warehouse": warehouse, "results": results, "count": False},
    )


def warehouse_count(request, warehouse_id):
    warehouse = get_object_or_404(Warehouse, pk=warehouse_id)
    results = Warehouse.objects.get(id=warehouse_id).items.annotate(
        item_count=Count("id")
    )
    return render(
        request,
        "warehouse.html",
        {"warehouse": warehouse, "results": results, "count": True},
    )

def add_items(request, warehouse_id, amount=None):
    if amount is None:
        return render(request, 'add_items.html', {'warehouse': Warehouse.objects.get(id=warehouse_id), 'amount': amount})
    elif amount > 0:
        ItemInWareHouseFormSet = modelformset_factory(
            Stock, 
            form=StockForm,
            extra=amount,
        )
        if request.method == 'POST':
            formset = ItemInWareHouseFormSet(request.POST, initial=[{'warehouse': warehouse_id}]*amount)
            if formset.is_valid():
                formset.save()
                return HttpResponseRedirect(reverse("warehouse info", args=(warehouse_id,)))
        else:
            formset = ItemInWareHouseFormSet(queryset=Stock.objects.none(), initial=[{'warehouse': warehouse_id}]*amount)
            return render(request, 'add_items.html', {'formset': formset, 'warehouse': Warehouse.objects.get(id=warehouse_id), 'amount': amount})
    else:
        return HttpResponseRedirect(reverse("add items", args=(warehouse_id,)))
        