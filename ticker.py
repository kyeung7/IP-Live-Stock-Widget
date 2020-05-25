# Kevin Yeung
# Scrolling stock ticker

# need to install yahoo_fin
# need to install requests_html (need to restart after)
# need to install tkinter

import tkinter as tk
import tkinter.font as tkFont
from tkinter import Frame, Entry
from yahoo_fin import stock_info as market

watchlist = ["AAPL", "AMZN", "AMD", "BA", "DIS", "DFS", "INTC", "FB", "GOOG"]
listSize = len(watchlist)

def setText():
##    tempStr=""
##    for i in watchlist:
##        stockPrice = round(market.get_live_price(i), 2)
##        tempStr += " " + i + ": $" + str(stockPrice) + " "
##        print(tempStr) #for debugging
##    setText.msg = tempStr
    
    setText.msg = setText.msg[1:] + setText.msg[0]
    svar.set(setText.msg)
    root.after(delay, setText)

def updateText():
    tempStr=""
    for i in watchlist:
        stockPrice = round(market.get_live_price(i), 2)
        tempStr += " " + i + ": $" + str(stockPrice) + " "
##        print(tempStr) #for debugging
    return tempStr

root = tk.Tk() # root is base of window
root.iconbitmap("stock.ico") #sets window icon
root.title("Live stock ticker")
root.geometry("750x30") #fixed window of tkinter root
root.wm_attributes("-topmost", 1) #set to top most window (windows os)

delay = 200 # character delay in milliseconds
svar = tk.StringVar() # used to edit widget text

fontStyle = tkFont.Font(family="Lucida Grande", size=11)
label = tk.Label(root, textvariable = svar, height = 30, width=200, font=fontStyle, borderwidth=2, relief="groove") # creates label given params


##setText.msg = " AAPL: $318.89  AMZN: $2436.88  AMD: $55.17  BA: $137.53  DIS: $118.02  DFS: $40.47  INTC: $62.26  FB: $234.91  GOOG: $1410.42"
setText.msg = updateText()
setText() #this gets looped...
label.pack()
root.mainloop()

###################################### LIVE ##############################
##
##stock = "AAPL"
##stockPrice = round(market.get_live_price(stock), 2) #formatted to 2 decimals by rounding
##
###live price of aapl stock
##print("Current Price of: " + stock + " is $" + str(stockPrice))
##
###################################### SCROLL TEST ##############################
##
### formats text
##def setText():
##    setText.msg = setText.msg[1:] + setText.msg[0]
##    svar.set(setText.msg)
##    root.after(delay, setText)
##    
##root = tk.Tk() # root is base of window
##root.iconbitmap("stock.ico") #sets window icon
##root.title("Live stock ticker")
##root.geometry("750x30") #fixed window of tkinter root
###root.overrideredirect(1) #no border but also no exit
##
###root.attributes("-alpha", 0.0)
##root.wm_attributes("-topmost", 1) #set to top most window (windows os)
##
##delay = 200 # character delay in milliseconds
##svar = tk.StringVar() # used to edit widget text
##
##fontStyle = tkFont.Font(family="Lucida Grande", size=11)
##label = tk.Label(root, textvariable = svar, height = 30, width=200, font=fontStyle, borderwidth=2, relief="groove") # creates label given params
##
##setText.msg = "AAPL: $318.89  AMZN: $2436.88  AMD: $55.17  BA: $137.53  DIS: $118.02  DFS: $40.47  INTC: $62.26  FB: $234.91  GOOG: $1410.42"
##setText()
##label.pack()
##root.mainloop()
