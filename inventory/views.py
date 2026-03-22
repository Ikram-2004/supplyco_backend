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




from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Stock
from django.utils.dateparse import parse_datetime

API_KEY = "MY_SUPPLYCO_SECRET_KEY"   # <-- NO SPACE BEFORE THIS

@api_view(['GET'])
def updated_stock(request):

    api_key = request.headers.get('X-API-KEY')

    if api_key != API_KEY:
        return Response({"error": "Unauthorized"}, status=401)

    last_sync_time = request.GET.get('last_sync_time')

    if last_sync_time:
        last_sync_time = parse_datetime(last_sync_time)
        stocks = Stock.objects.filter(
            last_updated__gt=last_sync_time
        ).order_by('last_updated')
    else:
        stocks = Stock.objects.all().order_by('last_updated')

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










