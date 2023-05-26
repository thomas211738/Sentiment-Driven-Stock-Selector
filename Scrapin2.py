
from requests_html import HTMLSession

# Returns List of 100 Headlines Based on the company name
def Headlines(company_name):
    url = f'https://news.google.com/rss/search?q={company_name}'
    s = HTMLSession()
    r = s.get(url)
    title = r.html.find('title')
    return title



