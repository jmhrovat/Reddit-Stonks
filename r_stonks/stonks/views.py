from django.http import HttpResponse
from stonks.models import *
import yfinance as yf


def index(request):

    portfolio = Portfolio.objects.get(pk=1)

    user_request_1 = "$BUY AAPL X4$"
    holdings_quanity = 0

    def is_valid_request(user_request):
        parameters = user_request.split()
        if (len(parameters) == 3
            and parameters[0][0] == "$"
            and parameters[2][0].upper() == "X"
            and parameters[2][-1] == "$"):
                return True
        else:
            return False

    def set_request_parameters(user_request):
        if is_valid_request(user_request):
            parameters = user_request.split()
            action = parameters[0]
            ticker = parameters[1]
            quantity = int(parameters[2][1:-1])
        return action, ticker, quantity

    try:
        action, ticker, volume = set_request_parameters(user_request_1)
    except:
        pass

    # stock = yf.Ticker(ticker)
    # closing_price = stock.history(period="today")['Close'][0]
    closing_price = 120
    valuation = volume * closing_price

    if action.upper() == "$BUY":
        if cash_balance - valuation > 0:
            holdings_quanity += volume
            cash_balance -= valuation
        else:
            print("You don't have enough cash for that purchase, moving on to the next order.")

    elif action.upper() == "$SELL":
        if holdings_quanity >= volume:
            holdings_quanity -= volume
            cash_balance += valuation

    print("Cash balance is now:", cash_balance)
    print("You own these many shares:", holdings_quanity)


    print("Cash balance: ", portfolio.cash)
    print("--------------------------------")
    if portfolio.holdings == {}:
        print("You have no holdings right now.")

    return HttpResponse("Check the terminal")
