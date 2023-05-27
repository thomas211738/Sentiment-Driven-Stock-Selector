
import yfinance as yf
import datetime

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
    today = today - datetime.timedelta(days=5)
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
   
print(new_investment(["AAPL"], [100]))