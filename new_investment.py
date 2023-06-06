import datetime
from test2 import Calc_Profit
import pandas as pd
import numpy as np
import yfinance as yf
from test2 import demo_write_csv
from test2 import fdemo_read_csv
from test2 import Calc_Percentage

df = pd.read_csv("S&P500.csv")
ticker = df['Ticker']

investment_list = fdemo_read_csv("scores_data.csv")


def new_investment(Ticker_List, Investment_List):
    
    today = datetime.date.today()
    
    yestrday =  today - datetime.timedelta(days=1)
    tommorow = today + datetime.timedelta(days=1)
    

    d = yf.download(Ticker_List[0], start= yestrday, end= tommorow)

    while(d.shape[0]==1):
        yestrday = yestrday - datetime.timedelta(days=1)
        d =  yf.download(Ticker_List[0], start= yestrday, end= tommorow)
    
        
        
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
            array = [profit]
            demo_write_csv('profits.csv',array)
            percentage = Calc_Percentage(Ticker_List[i],yestrday,tommorow)
            ar = [percentage]
            demo_write_csv('percentage.csv',ar)
        except:
            print('Erorr Here')
            profts.append(Investment_List[i])

    return profts

il = np.ones(503)*10
new_investment(ticker, il)

