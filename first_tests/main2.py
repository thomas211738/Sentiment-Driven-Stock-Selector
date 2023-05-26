
#from IPython.display import display
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def Calc_Profit(Ticker, T_0, T_f, Investment):
    data = yf.download(Ticker, start= T_0, end= T_f)
    if (len(data['Close']) >= 1):
        new_investment = Investment * ((data['Close'][-1]) / (data['Open'][0]))
        profit = new_investment - Investment
        return profit
    else:
        return 0
"""
#  UI
stock_Ticker = input("Stock Name: ")
initial_time = input("Start Time (yyyy-mm-dd): ")
investment_amount = int(input("Money Invested: "))
final_time = input("End Time (yyyy-mm-dd): ")

# DATA FRAME
apple_data = yf.download(stock_Ticker, start=initial_time, end=final_time)
df = pd.DataFrame(apple_data)[['Open', 'Close', 'High','Low']]

# CALCULATION
new_investment = investment_amount * ((apple_data['Close'][(len(df.index))-1])/(apple_data['Open'][0]))
profit = new_investment - investment_amount

# Printing
print("New Investment: " , new_investment)
print("Profit: " , profit , "\n\n")
display(df.head())


"""
print(Calc_Profit("AAPL", '2000-01-01', '2023-01-01', 100))