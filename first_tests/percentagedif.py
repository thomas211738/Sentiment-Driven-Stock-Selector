import pandas as pd
import numpy as np
import datetime
import yfinance as yf
import matplotlib.pyplot as plt



today = datetime.date.today()
    
yestrday =  today - datetime.timedelta(days=1)
tommorow = today + datetime.timedelta(days=1)
def Calc_Percentage(Ticker, T_0, T_f):
    data = yf.download(Ticker, start= T_0, end= T_f)
    if (len(data['Close']) >= 1):
        new_investment = ( (data['Open'][-1]) / (data['Close'][0]))
        
        return ((new_investment-1)*100).round(3)
    else:
        return 0
print(Calc_Percentage("AAPL",yestrday,tommorow))
