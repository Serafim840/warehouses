from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/<int:item_id>/', views.item, name="item info"),
    path('item/create/', views.create_item, name="create item"),
    path('warehouse/<int:warehouse_id>/', views.warehouse_all, name="warehouse info"),
    path('warehouse/<int:warehouse_id>/count', views.warehouse_count, name="warehouse count")

]