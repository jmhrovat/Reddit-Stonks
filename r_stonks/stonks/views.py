from django.http import HttpResponse
from modules.stonks import *
from modules.stonks_bot import *
from stonks.models import *
import yfinance as yf
import datetime


def index(request):

    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days = 1)

    # Create today's portfolio at 2:00pm
    # Set opening values equal to yesterday's portfolio
    open_portfolio = Portfolio.objects.get(date="2020-03-23")

    close_portfolio = Portfolio.objects.get(date="2020-03-24")

    request = UserRequest("$BUY COKE X30$")


    # close_portfolio.buy_stock(request)

    print("Open:")
    print(open_portfolio.holdings)
    print("Close:")
    print(close_portfolio.holdings)


    bot = get_stonks_bot()

    # Migrate url as attribute to Portfolio model
    post = bot.submission(url='https://www.reddit.com/r/test/comments/fl3jle/test_post/')



    # def get_formatted_holdings_table(holdings):
    #     #
    #     # holdings_substring = "Ticker | Price | Quantity | Value\n:--|--:|--:|--:\n"
    #     #
    #     # for stock in holdings:
    #     #     holdings_substring += ( stock
    #     #         + " | " + str(holdings[stock]["Price"])
    #     #         + " | " + str(holdings[stock]["Volume"])
    #     #         + " | " + str((holdings[stock]["Price"] * holdings[stock]["Volume"])) + "\n"
    #     #     )
    #     # return holdings_substring



    # print(portfolio.get_formatted_holdings_table())


    # today = str(date.today().strftime("%m/%d/%Y"))

    # post_text = ""
    # post_text += (
    #     "#" + " Portfolio\n" +
    #     "---\n"
    #     "View Chart\n\n" +
    #     "**Portfolio @ Open**\n" +
    #     portfolio.get_formatted_holdings_table() +
    #     "**Portfolio @ Close**\n" +
    #     portfolio.get_formatted_holdings_table() +
    #     "**End of Day Change:\n" +
    #     "View change to date by:" +
    #     "**Today's Transactions**" +
    #     "/u/**** sold 7 shares of stock" +
    #     "/u/******* bought 8 stock"
    #
    #     )

    # post.edit(post_text)
    # print(post_text)


    # user_requests = []

    # for top_level_comment in submission.comments:
    #     user_message = top_level_comment.body
    #     user_requests.append(UserRequest(user_message))
    #
    # for user_request in user_requests:
    #     try:
    #         if user_request.action == "$BUY":
    #             portfolio.buy_stock(user_request)
    #         elif user_request.action == "$SELL":
    #             portfolio.sell_stock(user_request)
    #     except AttributeError as err:
    #         pass

    # stock = yf.Ticker(ticker)
    # closing_price = stock.history(period="today")['Close'][0]


    # print("Cash balance: ", portfolio.cash)
    # print("--------------------------------")
    # if portfolio.holdings == {}:
    #     print("You have no holdings right now.")
    # else:
    #     print("Holdings:")
    #     print(portfolio.holdings)

    # print("You have the following stock:")
    # for key, value in portfolio.holdings:
    #     print('You own {} shares of {}, '.format(key, value))


    return HttpResponse("Check the terminal")
