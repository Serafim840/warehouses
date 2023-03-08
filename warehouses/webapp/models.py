from django.db import models
from django.forms import ModelForm, HiddenInput


class Item(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["brand", "model"], name="unique_model")
        ]

    def __str__(self):
        return f"{self.brand}, {self.model}, {self.country}"


class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    items = models.ManyToManyField(Item, through="Stock")

    def __str__(self) -> str:
        return self.name


class Stock(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    inventory_id = models.CharField(max_length=255)


class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = "__all__"
        labels = {"item": "Техника", "inventory_id": "Инв №"}
        widgets = {"warehouse": HiddenInput()}
