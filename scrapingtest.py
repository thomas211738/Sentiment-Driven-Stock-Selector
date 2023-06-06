from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl
import numpy as np
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

root = "https://www.google.com/"
link = "https://www.google.com/search?q=Apple&tbm=nws&tbs=qdr:d"


def news(link):
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html5lib')
    # print(soup.prettify())
    for item in soup.find_all('div', attrs={'class': 'Gx5Zad fP1Qef xpd EtOod pkphOe'}):
                
        title = (item.find('div', attrs={'class': 'BNeawe vvjwJb AP7Wnd'}).get_text())
       
        title = title.replace("...", "")
        print(title)
     
        

news(link)


def Headlines(companyname):
    link = f'https://www.google.com/search?q={companyname}&tbm=nws&tbs=qdr:d'
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html5lib')
    titles = []
    for item in soup.find_all('div', attrs={'class': 'Gx5Zad fP1Qef xpd EtOod pkphOe'}):
                
        title = (item.find('div', attrs={'class': 'BNeawe vvjwJb AP7Wnd'}).get_text())
        title = title.replace(",", "")
        title = title.replace("...", "")
        titles.append(title)
    return titles

# df = pd.read_csv("S&P500.csv")
# name = df["Company"]
# print(type(name[0]))
# print(type("Apple"))
# x = Headlines(name[0])
# print(x)

