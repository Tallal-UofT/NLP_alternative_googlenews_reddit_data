from gnews import GNews
import pandas as pd

def get_google_news(company):
    google_news = GNews()
    google_news = GNews(language='en', country='US', max_results=35)
    news = google_news.get_news(company)
    for i in range(len(news)):
        try:
            article = google_news.get_full_article(news[i]['url'])
            news[i]['text']= article.text
        except:
            pass
    news = pd.DataFrame(news)
    news['text'] = news['text'] + news['title']
    news = news.dropna()
    return news


def get_google_business_news():
    google_news = GNews()
    google_news = GNews(language='en', country='US', max_results=35)
    news = google_news.get_news_by_topic("BUSINESS")
    for i in range(len(news)):
        try:
            article = google_news.get_full_article(news[i]['url'])
            news[i]['text']= article.text
        except:
            pass
    news = pd.DataFrame(news)
    news['text'] = news['text'] + news['title']
    news = news.dropna()
    return news