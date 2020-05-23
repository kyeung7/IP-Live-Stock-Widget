# Kevin Yeung
# Scrolling stock ticker

#################################### HISTORICAL ##############################
##
### may need to install yfinance (via pip)
### also may need to install lxml
##
##import yfinance as yfinance
##
### ticker symbol
##stock = "AAPL"
##
### get data for AAPL
##stockData = yfinance.Ticker(stock)
##
### get AAPL price at specified range in time
##stockPrice = stockData.history(period="1d", start="2010-1-1", end="2010-1-7")
##
### market is not open some days due to holidays and weekends 
##print(stockPrice)
##
###stock summary
##print(stockData.info)

#################################### LIVE ##############################
# need to install yahoo_fin
# need to install requests_html (need to restart after)
from yahoo_fin import stock_info as market

stock = "AAPL"
stockPrice = round(market.get_live_price(stock), 2) #formatted to 2 decimals by rounding

#live price of aapl stock
print("Current Price of: " + stock + " is $" + str(stockPrice))
