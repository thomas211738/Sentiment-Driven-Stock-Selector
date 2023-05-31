import yfinance as yf
import pandas as pd
from test2 import Calc_Profit
data = yf.download("^GSPC", start = "2023-05-26", end = "2023-05-31")
print(data)
p = Calc_Profit("^GSPC","2023-05-26", "2023-05-31", 503)
print(p)
