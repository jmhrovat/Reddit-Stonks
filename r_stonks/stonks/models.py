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

    # Combine buy and sell into a single conditional called 'ProcessOrder'
    def buy_stock(self, User_Request):
        valuation = 600
        closing_price = 100
        volume = User_Request.volume
        ticker = User_Request.ticker
        if self.cash >= valuation:
            if ticker in self.holdings:
                self.holdings[ticker]["Price"] = closing_price
                self.holdings[ticker]["Volume"] += volume
                self.cash -= valuation
            else:
                self.holdings[ticker] = {}
                self.holdings[ticker]["Price"] = closing_price
                self.holdings[ticker]["Volume"] = volume
                self.cash -= valuation
        else:
            print("You don't have enough cash for that purchase.")
        self.save()

    def sell_stock(self, User_Request):
        volume = User_Request.volume
        ticker = User_Request.ticker
        closing_price = 100
        valuation = closing_price * volume
        if ticker in self.holdings:
            print("Yes you have that stock")
            if self.holdings[ticker]["Volume"] >= volume:
                self.holdings[ticker]["Price"] = closing_price
                self.holdings[ticker]["Volume"] -= volume
                self.cash += valuation
            else:
                print("You don't have enough stock, sale failed")

            if self.holdings[ticker]["Volume"] <= 0:
                self.holdings.pop(ticker, None)
        else:
            print("You don't have that stock")
        self.save()

    def get_formatted_holdings_table(self):

        holdings_substring = "Ticker | Price | Quantity | Value\n:--|--:|--:|--:\n"
        total_valuation = 0
        for stock in self.holdings:

            valuation = self.holdings[stock]["Price"] * self.holdings[stock]["Volume"]

            holdings_substring += ( stock
                + " | " + str(self.holdings[stock]["Price"])
                + " | " + str(self.holdings[stock]["Volume"])
                + " | " + str(valuation) + "\n"
            )

            total_valuation += valuation

        holdings_substring += "**TOTAL** | | | **" + str(total_valuation) + "**\n"
        return holdings_substring
