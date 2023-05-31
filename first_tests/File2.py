
import yfinance as yf
import datetime
import csv

def Calc_Profit(Ticker, T_0, T_f, Investment):
    data = yf.download(Ticker, start= T_0, end= T_f)
    if (len(data['Close']) >= 1):
        new_investment = Investment * ( (data['Open'][-1]) / (data['Close'][0]))
        profit = new_investment - Investment
        return profit
    else:
        return 0
    
"""data = yf.download("AAPL", start= '2023-05-26', end= "2023-05-28")
print(data)


print(Calc_Profit("AAPL",'2023-05-26',"2023-05-28", 100 ))"""


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
        except:
            print('Erorr Here')
            profts.append(Investment_List[i])

    return profts


def demo_read_csv(filename):
    scores = []
    with open(filename, mode='r') as my_csv:
        reader = csv.reader(my_csv)
        for record in reader:
            scores.append(float(record[0]))
    return scores

x = demo_read_csv("scores_data.csv")
print((x))