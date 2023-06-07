
import pandas as pd
import numpy as np
from nltk.sentiment import SentimentIntensityAnalyzer
from requests_html import HTMLSession
import yfinance as yf
import matplotlib.pyplot as plt
import csv
# Returns List of 100 Headlines Based on the company name
def Headlines(company_name):
    #url = f'https://news.google.com/rss/search?q={company_name}'
    url = f'https://news.google.com/rss/search?q={company_name}%20when%3A1d'

    s = HTMLSession()
    r = s.get(url)
    titles = r.html.find('title')
    titles.pop(0)
    
    tit = []
    for title in titles:
        split_list = title.text.split(" - ")
        full_text = split_list[0].replace('...', '')
        tit.append(full_text)
    
    
    return tit[:5]
print(Headlines("Apple"))
