from django.contrib import admin
from .models import Store, Item, Stock

admin.site.register(Store)
admin.site.register(Item)
admin.site.register(Stock)