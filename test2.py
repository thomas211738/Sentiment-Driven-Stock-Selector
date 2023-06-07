
import pandas as pd
import numpy as np
from nltk.sentiment import SentimentIntensityAnalyzer
from requests_html import HTMLSession
import yfinance as yf
import matplotlib.pyplot as plt
import csv
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


# Scores a Text and gives it a score between -1 and 1
def score_text(text):
    sid = SentimentIntensityAnalyzer()
    value = sid.polarity_scores(text)
    return value['compound']


# Returns List of all titles from google search first page
def Headlines(company_name):
    #url = f'https://news.google.com/rss/search?q={company_name}'
    url = f'https://news.google.com/rss/search?q={company_name}%20when%3A1d'

    s = HTMLSession()
    r = s.get(url)
    soup = BeautifulSoup(r.content, 'xml')
    titles = soup.find_all('title')
    titles.pop(0)
    
    tit = []
    for title in titles:
        split_list = title.text.split(" - ")
        full_text = split_list[0].replace('...', '')
        tit.append(full_text)
    
    
    return tit[:5]

# Calculates profit of an investment based on the company, inital time you invested
# and final time, and how much you invested
def Calc_Profit(Ticker, T_0, T_f, Investment):
    data = yf.download(Ticker, start= T_0, end= T_f)
    if (len(data['Close']) >= 1):
        new_investment = Investment * ( (data['Open'][-1]) / (data['Close'][0]))
        profit = new_investment - Investment
        return profit.round(3)
    else:
        return 0
    
#calculate the percentage difference from inital time invested and final time invested
def Calc_Percentage(Ticker, T_0, T_f):
    data = yf.download(Ticker, start= T_0, end= T_f)
    if (len(data['Close']) >= 1):
        new_investment = ( (data['Open'][-1]) / (data['Close'][0]))
        
        return ((new_investment-1)*100).round(3)
    else:
        return 0

#writer to a csv file
def demo_write_csv(filename, vals1):
    with open(filename, mode = 'a', newline='') as my_csv:
        writer = csv.writer(my_csv)
        writer.writerow(vals1)

#reading a csv file and converting to float numbers
def fdemo_read_csv(filename):
    lists = []
    with open(filename, mode='r') as my_csv:
        reader = csv.reader(my_csv)
        for record in reader:
            lists.append(float(record[0]))
    return lists


# Finds polarity scores for each company and returns an array of those scores
# Takes 10 mins to run   
def find_investment():
    df = pd.read_csv("S&P500.csv")
    name = df["Company"]
    Scores = []
    iterator = 1
    

    for i in range(len(name)):
        headlines = Headlines(name[i].strip().replace(" ", "%20"))
        print(iterator)
        iterator += 1
        score = []

        for headline in headlines:
            score.append(score_text(headline))
        
        if(len(score)!=0):

            avg = sum(score) / len(score)
            avg = round(avg,4)
            Scores.append(avg)
            array = [avg]
            demo_write_csv('scores_data.csv',array)
        else:
            demo_write_csv('scores_data.csv',[0])

    return Scores    


find_investment()