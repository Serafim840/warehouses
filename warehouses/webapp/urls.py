from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/<int:item_id>/', views.item, name="item info"),
    path('warehouse/<int:warehouse_id>/', views.warehouse_all, name="warehouse info")
]