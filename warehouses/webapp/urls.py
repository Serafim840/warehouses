from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("item/<int:item_id>/", views.item_all, name="item info"),
    path("item/<int:item_id>/count", views.item_count, name="item count"),
    path("item/create/", views.create_item, name="create item"),
    path("warehouse/<int:warehouse_id>/", views.warehouse_all, name="warehouse info"),
    path(
        "warehouse/<int:warehouse_id>/count",
        views.warehouse_count,
        name="warehouse count",
    ),
    path("warehouse/<int:warehouse_id>/add_items", views.add_items, name="add items"),
    path(
        "warehouse/<int:warehouse_id>/add_items/<int:amount>",
        views.add_items,
        name="add items",
    ),
    path(
        "warehouse/<int:warehouse_id>/remove_items",
        views.remove_items,
        name="remove items",
    ),
    path(
        "warehouse/<int:warehouse_id>/remove_items/<int:amount>",
        views.remove_items,
        name="remove items",
    ),
]
