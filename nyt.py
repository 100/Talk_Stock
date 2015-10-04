import requests
import private
from nytimesarticle import articleAPI

def getArticles(stocks):
    api = articleAPI(private.NYT)
    articles = {}
    for key, value in stocks.iteritems():
        stockRequest = api.search(fq = {'headline': value}, begin_date = 20150905)
        try:
            headline = stockRequest['response']['docs'][0]['headline']['main']
            url = stockRequest['response']['docs'][0]['web_url']
            if stockRequest['response']['docs'][0]['abstract'] is not None:
                abstract = stockRequest['response']['docs'][0]['abstract']
            else:
                abstract = "None"
        except Exception as e:
            pass
        articles[key] = {'headline': headline, 'url': url, 'abstract': abstract}
    return articles
