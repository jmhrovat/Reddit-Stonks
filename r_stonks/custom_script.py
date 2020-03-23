import praw
import yfinance as yf

"""RULES: Welcome to Reddit buys Stonks. A social experiment on how well random
strangers can coordinate with eachother to grow a collective portfolio.

The game is simple. Starting on day one, Reddit will receive a starting fund
(For example let's assume it's 1 mil.) That money sits in the pool, and
will not earn interest.

The bot will create a new post, stating the current allocation of funds.

To buy stock, there must be enough capital available. If not, stocks must be
sold to raise money.

If there's enough money in the fund, any user can post a top level comment
and request a trade.

Assume the current market price for APPL is 250 per share. User_A replies
to the post requesting 40 shares. This would be a 10,000 dollar purchase.

Format: BUY APPL X40

The order will stand as is, as long as the votes remain above 0. A buy or sell order
must have positive karma to process.

At the end of trading, all top level comments are organized by top. Assuming
that 2 users posted the same ticker, the one with higher karma would go through.

Sell orders are completed first, followed by buy orders. There is a $15 fee per trade.

Orders are processed based off the closing trading values. Trades are closed on weekends.




Rules:

Only 1 share per top level comments. The same ticker can not appear twice in the
top level.

Edits lose participation privilge. this is to reduce shadow edit trolling.


"""


# stock = yf.Ticker("AAPL")
#
#
# closing_price = stock.history(period="today")['Close'][0]



# for top_level_comment in submission.comments:
#     comments.append(top_level_comment.body)

# tickers = validate_tickers(comments)

# print(tickers)

print("""
Today's Activity

Current Portfolio
MSFT: 88.80 USD −4.73 (5.06%)
4 Shares:

No Sells
------------------------------------

Buys
APPL: 40 Shares x $250.00 = $10,000

Broker Fee
1 Transaction * $15.00 = $15.00

Final Total

""")

# ticker = comments[1].body
#
# stock = yf.Ticker(ticker)
#
# print(stock.history(period="today")['Close'][0])
