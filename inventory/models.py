from django.db import models

# Create your models here.
from django.db import models


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    district = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price_per_kg = models.FloatField()
    is_subsidized = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.FloatField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.store.name} - {self.item.name}"