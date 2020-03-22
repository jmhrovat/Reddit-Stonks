from django.db import models
from django.contrib.postgres.fields import JSONField


# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    cash = models.IntegerField()
    holdings = JSONField(default=dict)

    def reset(self):
        self.cash = 100000
        self.holdings = {}

    def buy_stock(self, User_Request):
        valuation = 600
        closing_price = 35
        volume = 100
        ticker = User_Request.ticker
        if self.cash - valuation > 0:
            if User_Request.ticker in self.holdings:
                self.holdings[ticker]["Price"] = closing_price
                self.holdings[ticker]["Volume"] += volume
                self.cash -= valuation
            else:
                self.holdings[ticker] = {}
                self.holdings[ticker]["Price"] = closing_price
                self.holdings[ticker]["Volume"] = volume
                self.cash -= valuation
        else:
            print("You don't have enough cash for that purchase, moving on to the next order.")
        self.save()

        # TODO: Sell function
