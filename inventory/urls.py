from django.urls import path
from .views import updated_stock

urlpatterns = [
    path('updated-stock/', updated_stock),
]