
from test2 import Calc_Profit
import pandas as pd

df = pd.read_excel('/Users/toto211738/Downloads/S&P500.xlsx')
ticker = df['Ticker']


def new_investment(Ticker_List, Investment_List):
    today = '2023-05-24'
    tommorow = "2023-05-25"

    profts = []
    iter = 1

    for i in range(len(Ticker_List)):
        print(iter)
        iter+=1
        investment = Investment_List[i]
        try:
            profit = Calc_Profit(Ticker_List[i],today,tommorow,investment)
            profts.append(profit)
            print(investment, profit)
        except:
            print('Erorr Here')
            profts.append(Investment_List[i])

    return profts