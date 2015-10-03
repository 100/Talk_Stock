import requests
import private
from nytimesarticle import articleAPI
from stockList import *

def getArticles(stocks):
    api = articleAPI(private.NYT)
    articles = {}
    for key, value in stocks.iteritems():
        stockRequest = api.search(fq = {'headline': value}, begin_date = 20150927)
        headline = stockRequest['response']['docs']['headline']['main']
        url = stockRequest['response']['docs']['web_url']
        if stockRequest['response']['docs']['abstract'] is not None:
            abstract = stockRequest['response']['docs']['abstract']
        else:
            abstract = "None"
        articles[key] = {'headline': headline, 'url': url, 'abstract': abstract}
