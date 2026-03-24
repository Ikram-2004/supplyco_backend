#from django.contrib import admin
#from .models import Store, Item, Stock

#admin.site.register(Store)
#admin.site.register(Item)
#admin.site.register(Stock)


from django.contrib import admin
from .models import Store, Item, Stock


# ===================== STORE ADMIN =====================
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = (
        'store_id',
        'name',
        'district',
        'latitude',
        'longitude'
    )


# ===================== ITEM ADMIN =====================
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'item_id',
        'name',
        'price_per_kg',
        'is_subsidized'
    )


# ===================== STOCK ADMIN =====================
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = (
        'stock_id',
        'store_id',   # shows FK ID
        'item_id',    # shows FK ID
        'quantity',
        'last_updated'
    )