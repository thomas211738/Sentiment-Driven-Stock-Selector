import DateTime
from test2 import Calc_Profit
import pandas as pd

df = pd.read_csv("S&P500.csv")
ticker = df['Ticker']


def new_investment(Ticker_List, Investment_List):
    today = DateTime.date.today()
    tommorow = today + DateTime.timedelta(days=1)

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