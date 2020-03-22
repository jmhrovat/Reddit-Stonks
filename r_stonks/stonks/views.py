from django.http import HttpResponse
from modules.stonks import *
from stonks.models import *
import yfinance as yf


def index(request):

    portfolio = Portfolio.objects.get(pk=1)

    user_message = "$SELL COKE X200$"

    user_request = UserRequest(user_message)


    # stock = yf.Ticker(ticker)
    # closing_price = stock.history(period="today")['Close'][0]

    if user_request.action == "$BUY":
        portfolio.buy_stock(user_request)
    elif user_request.action == "$SELL":
        portfolio.sell_stock(user_request)

    print("Cash balance: ", portfolio.cash)
    print("--------------------------------")
    if portfolio.holdings == {}:
        print("You have no holdings right now.")
    else:
        print("Holdings:")
        print(portfolio.holdings)
    # else:
    # print("You have the following stock:")
    # for key, value in portfolio.holdings:
    #     print('You own {} shares of {}, '.format(key, value))


    return HttpResponse("Check the terminal")
