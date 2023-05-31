
import pandas as pd
import numpy as np
from nltk.sentiment import SentimentIntensityAnalyzer
from requests_html import HTMLSession
import yfinance as yf
import matplotlib.pyplot as plt
import csv


# Scores a Text and gives it a score between -1 and 1
def score_text(text):
    sid = SentimentIntensityAnalyzer()
    value = sid.polarity_scores(text)
    return value['compound']


# Returns List of 100 Headlines Based on the company name
def Headlines(company_name):
    #url = f'https://news.google.com/rss/search?q={company_name}'
    url = f'https://news.google.com/rss/search?q={company_name}%20when%3A1d'

    s = HTMLSession()
    r = s.get(url)
    title = r.html.find('title')
    return title

# Calculates profit of an investment based on the company, inital time you invested
# and final time, and how much you invested
def Calc_Profit(Ticker, T_0, T_f, Investment):
    data = yf.download(Ticker, start= T_0, end= T_f)
    if (len(data['Close']) >= 1):
        new_investment = Investment * ( (data['Open'][-1]) / (data['Close'][0]))
        profit = new_investment - Investment
        return profit
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
    name = df['Company']
    Scores = []
    iterator = 1

    for i in range(len(name)):
        headlines = Headlines(name[i])
        print(iterator)
        iterator += 1
        score = []

        for headline in headlines:
            score.append(score_text(headline.text))

        avg = sum(score) / len(score)
        Scores.append(avg)
        array = [avg]
        demo_write_csv('scores_data.csv',array)

    return Scores    


scores = find_investment()