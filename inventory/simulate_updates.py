import random
import time
from inventory.models import Stock

def auto_update():
    while True:
        stocks = list(Stock.objects.all())

        if len(stocks) <= 10:
            selected_stocks = stocks
        else:
            selected_stocks = random.sample(stocks, 10)

        for stock in selected_stocks:
            stock.quantity = random.randint(10, 300)
            stock.save()
            print(f"Updated stock ID: {stock.stock_id}")

        print("Sleeping for 5 minutes...\n")
        time.sleep(300)