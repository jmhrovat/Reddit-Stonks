from django.http import HttpResponse
from modules.stonks import *
from stonks.models import *
import yfinance as yf


def index(request):

    portfolio = Portfolio.objects.get(pk=1)

    user_message = "$BUY AAPL X20$"

    user_request = UserRequest(user_message)


    # stock = yf.Ticker(ticker)
    # closing_price = stock.history(period="today")['Close'][0]


    portfolio.buy_stock(user_request)

    print(portfolio.holdings)



    # if action.upper() == "$BUY":

    # elif action.upper() == "$SELL":
    #     if ticker in portfolio.holdings:
    #         print("Yes you have that stock")
    #         portfolio.holdings[ticker][1] -= volume
    #         portfolio.cash += valuation
    #     else:
    #         print("You don't have that stock")



            # if holdings_quanity >= volume:
            #     holdings_quanity -= volume
            #     cash_balance += valuation

    # portfolio.save()

    print("Cash balance: ", portfolio.cash)
    print("--------------------------------")
    if portfolio.holdings == {}:
        print("You have no holdings right now.")
    # else:
    # print("You have the following stock:")
    # for key, value in portfolio.holdings:
    #     print('You own {} shares of {}, '.format(key, value))


    return HttpResponse("Check the terminal")
