# Kevin Yeung
# Scrolling stock ticker

# need to install yahoo_fin
# need to install requests_html (need to restart after)
# need to install tkinter

import tkinter as tk
import tkinter.font as tkFont
from tkinter import Frame, Entry
from yahoo_fin import stock_info as market
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

stock = "AAPL"
stockPrice = round(market.get_live_price(stock), 2) #formatted to 2 decimals by rounding

#live price of aapl stock
print("Current Price of: " + stock + " is $" + str(stockPrice))

#################################### SCROLL TEST ##############################


def setText():
    setText.msg = setText.msg[1:] + setText.msg[0]
    svar.set(setText.msg)
    root.after(delay, setText)
    
root = tk.Tk() # root is base of window
root.iconbitmap("stock.ico") #sets window icon
root.title("Live stock ticker")
root.geometry("750x30") #fixed window of tkinter root
#root.overrideredirect(1) #no border but also no exit

#root.attributes("-alpha", 0.0)
root.wm_attributes("-topmost", 1) #set to top most window (windows os)

delay = 200 # character delay in milliseconds
svar = tk.StringVar() # used to edit widget text

fontStyle = tkFont.Font(family="Lucida Grande", size=11)
label = tk.Label(root, textvariable = svar, height = 30, width=200, font=fontStyle, borderwidth=2, relief="groove") # creates label given params

setText.msg = "Example text here eeeeeeeeeeeeeeeeeeeeiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiieeeeeeee "
setText()
label.pack()
root.mainloop()
