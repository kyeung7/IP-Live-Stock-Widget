# Kevin Yeung
# Scrolling stock ticker

# need to install yahoo_fin
# need to install requests_html (need to restart after)
# need to install tkinter
import tkinter as tk
import tkinter.font as tkFont
from tkinter import Frame, Entry
from yahoo_fin import stock_info as market

# Default list of stocks
watchlist = ["AAPL", "AMZN", "AMD", "BA", "DIS", "DFS", "INTC", "FB", "GOOG"]

# Updates the label text and animate
def setText():
    setText.msg = setText.msg[1:] + setText.msg[0]
    svar.set(setText.msg)
    root.after(delay, setText)

# Get live market prices
def updateText():
    tempStr=""
    for i in watchlist:
        stockPrice = round(market.get_live_price(i), 2)
        tempStr += " " + i + ": $" + str(stockPrice) + " "
    return tempStr

# Tkinter root and window options
root = tk.Tk()
root.iconbitmap("stock.ico")
root.title("Live stock ticker")
root.geometry("750x30")
root.wm_attributes("-topmost", 1) # Set to top most window (windows os)

delay = 200 # Character delay in milliseconds
svar = tk.StringVar() # Used to edit widget text

fontStyle = tkFont.Font(family="Lucida Grande", size=11)
label = tk.Label(root, textvariable = svar, height = 30, width=200, font=fontStyle, borderwidth=2, relief="groove") # creates label given params

## setText.msg = " AAPL: $318.89  AMZN: $2436.88  AMD: $55.17  BA: $137.53  DIS: $118.02  DFS: $40.47  INTC: $62.26  FB: $234.91  GOOG: $1410.42"
setText.msg = updateText()
setText()
label.pack()
root.mainloop()
