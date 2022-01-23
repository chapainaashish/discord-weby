import urllib
import requests
from word_list import weby
from config import *

news_url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWSAPI}'
quotes_url = "https://zenquotes.io/api/random"
wolfram_url = 'http://api.wolframalpha.com/v2/query?appid={}&input={}&format=plaintext&output=json'


def get_quote():
    quote_response = requests.get(quotes_url)
    quote = quote_response.json()[0]['q'] + " -" + \
        quote_response.json()[0]['a']
    return quote


def news_search():
    news_api = requests.get(news_url)
    searched_news = ["Today Headlines;\n"]
    for news in news_api.json()["articles"]:
        searched_news.append(f"--> {news['title']}\n")
    return searched_news


def request_parser(query):
    """Used to add '+' sign instead of ' ' in search query"""
    for word in weby:
        if word in query:
            query = query.replace(word, "")
    modified_query = urllib.parse.quote_plus(query)
    return modified_query


def query_find(query):
    """Searching General query in wolframalpha"""
    modified_query = request_parser(query)
    response = requests.get(wolfram_url.format(
        WOLFRAMAPI, modified_query)).json()
    try:
        data = response["queryresult"]["pods"][1]["subpods"][0]["plaintext"]
        return data
    except:
        return "Weber didn't understand your language:(:("
