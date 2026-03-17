from django.core.management.base import BaseCommand
from inventory.models import Stock
import random

class Command(BaseCommand):
    help = "Update stock randomly"

    def handle(self, *args, **kwargs):
        stocks = list(Stock.objects.all())

        if len(stocks) <= 10:
            selected = stocks
        else:
            selected = random.sample(stocks, 10)

        for stock in selected:
            stock.quantity = random.randint(10, 300)
            stock.save()
            self.stdout.write(f"Updated {stock.stock_id} → {stock.quantity}")

        self.stdout.write("✅ Stock update completed")