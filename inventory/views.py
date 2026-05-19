# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Stock
# from django.utils.dateparse import parse_datetime

# @api_view(['GET'])
# def updated_stock(request):
#     last_sync_time = request.GET.get('last_sync_time')

#     if last_sync_time:
#         last_sync_time = parse_datetime(last_sync_time)
#         stocks = Stock.objects.filter(last_updated__gt=last_sync_time)
#     else:
#         stocks = Stock.objects.all().order_by('last_updated')

#     data = [
#         {
#             "store": stock.store.name,
#             "item": stock.item.name,
#             "quantity": stock.quantity,
#             "last_updated": stock.last_updated
#         }
#         for stock in stocks
#     ]

#     return Response(data)




from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Stock

API_KEY = "MY_SUPPLYCO_SECRET_KEY"


# Homepage route
def home(request):
    return JsonResponse({
        "message": "Supplyco Backend API Running",
        "api_endpoint": "/api/updated-stock/"
    })


# API route
@api_view(['GET'])
def updated_stock(request):

    # API KEY CHECK
    key = request.headers.get("X-API-KEY") or request.GET.get("api_key")

    if key != API_KEY:
        return Response({"error": "Unauthorized"}, status=401)

    # OPTIONAL SYNC FILTER
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

    # RESPONSE DATA
    data = [
        {
            "store": stock.store_id,
            "item": stock.item_id,
            "quantity": stock.quantity,
            "last_updated": stock.last_updated
        }
        for stock in stocks
    ]

    return Response(data)