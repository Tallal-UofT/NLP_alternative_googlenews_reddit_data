import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_sp500_details():
    wikiurl="https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    table_class="wikitable sortable jquery-tablesorter"
    response=requests.get(wikiurl)
    soup = BeautifulSoup(response.text, 'html.parser')
    sp500=soup.find('table',{'class':"wikitable"})
    df=pd.read_html(str(sp500))
    # convert list to dataframe
    df=pd.DataFrame(df[0])
    df = df[["Symbol", "Security"]]
    return df