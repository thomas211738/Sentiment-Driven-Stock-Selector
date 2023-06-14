

APIKEY = "2e63cc2cbf4208c632f1de1f72e2f442"

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests

api_key = '2e63cc2cbf4208c632f1de1f72e2f442'
url = 'https://www.google.com/search?q=Apple&tbm=nws&tbs=qdr:d'
proxy_url = f'http://api.scraperapi.com/?api_key={api_key}&url={url}&country_code=us'

response = requests.get(proxy_url)
soup = BeautifulSoup(response.text, 'lxml')
#print(soup.prettify())
titles = []
for item in soup.find_all('div', attrs={'class': 'SoaBEf'}):
    title = item.find('div', attrs={'class': 'n0jPhd ynAwRc MBeuO nDgy9d'}).get_text()
    title = title.replace("...", "")
    title = title.replace("\n","")
    titles.append(title)

print(titles)

