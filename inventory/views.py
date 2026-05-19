from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Stock, Item

API_KEY = "MY_SUPPLYCO_SECRET_KEY"


def home(request):
    return JsonResponse({
        "message": "Supplyco Backend API Running",
        "api_endpoint": "/api/updated-stock/"
    })


@api_view(['GET'])
def updated_stock(request):

    key = request.headers.get("X-API-KEY") or request.GET.get("api_key")

    if key != API_KEY:
        return Response({"error": "Unauthorized"}, status=401)

    last_sync_time = request.GET.get('last_sync_time')

    if last_sync_time:
        try:
            stocks = Stock.objects.filter(
                last_updated__gt=last_sync_time
            ).order_by('last_updated')

        except Exception:
            return Response({"error": "Invalid datetime"}, status=400)

    else:
        stocks = Stock.objects.all().order_by('last_updated')

    # LOAD ALL ITEM PRICES ONCE
    items = {
        item.item_id: float(item.price_per_kg)
        for item in Item.objects.all()
    }

    data = [
        {
            "store": stock.store_id,
            "item": stock.item_id,
            "quantity": stock.quantity,
            "price": items.get(stock.item_id),
            "last_updated": stock.last_updated
        }
        for stock in stocks
    ]

    return Response(data)