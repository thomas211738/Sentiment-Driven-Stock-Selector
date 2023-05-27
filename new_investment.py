import datetime
from test2 import Calc_Profit
import pandas as pd
import numpy as np

df = pd.read_csv("S&P500.csv")
ticker = df['Ticker']


def new_investment(Ticker_List, Investment_List):
    
    today = datetime.date.today()
    yestrday =  today - datetime.timedelta(days=1)
    tommorow = today + datetime.timedelta(days=1)
    
    today_dow = today.strftime("%A")
    
    
    if (today_dow == "Monday"):
        yestrday = today - datetime.timedelta(days=3)
        
        
    profts = []
    iter = 1

    for i in range(len(Ticker_List)):
        print(iter)
        iter+=1
        investment = Investment_List[i]
        try:
            profit = Calc_Profit(Ticker_List[i],yestrday,tommorow,investment)
            profts.append(profit)
            print(investment, profit)
        except:
            print('Erorr Here')
            profts.append(Investment_List[i])

    return profts



new_investment(["AAPL"], [100])
