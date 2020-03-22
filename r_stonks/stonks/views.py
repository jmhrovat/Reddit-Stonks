from django.http import HttpResponse
from modules.stonks import *
from modules.stonks_bot import *
from stonks.models import *
import yfinance as yf


def index(request):

    portfolio = Portfolio.objects.get(pk=1)

    portfolio.reset()

    bot = get_stonks_bot()

    submission = bot.submission(url='https://www.reddit.com/r/test/comments/fl3jle/test_post/')

    user_requests = []

    for top_level_comment in submission.comments:
        user_message = top_level_comment.body
        user_requests.append(UserRequest(user_message))

    for user_request in user_requests:
        try:
            if user_request.action == "$BUY":
                portfolio.buy_stock(user_request)
            elif user_request.action == "$SELL":
                portfolio.sell_stock(user_request)
        except AttributeError as err:
            pass

    # stock = yf.Ticker(ticker)
    # closing_price = stock.history(period="today")['Close'][0]


    print("Cash balance: ", portfolio.cash)
    print("--------------------------------")
    if portfolio.holdings == {}:
        print("You have no holdings right now.")
    else:
        print("Holdings:")
        print(portfolio.holdings)

    # print("You have the following stock:")
    # for key, value in portfolio.holdings:
    #     print('You own {} shares of {}, '.format(key, value))


    return HttpResponse("Check the terminal")
