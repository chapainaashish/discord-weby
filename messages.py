import requests
import os
import urllib
from word_list import weby


def get_quote():
    quote_response = requests.get("https://zenquotes.io/api/random")
    quote = quote_response.json()[0]['q'] + " -" + \
        quote_response.json()[0]['a']
    return quote


def auto_search():
    """Searching news"""
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={os.environ.get("NEWSAPI")}'
    news_api = requests.get(url)
    searched_news = ["Today Headlines;\n"]
    for news in news_api.json()["articles"]:
        searched_news.append(f"--> {news['title']}\n")
    return searched_news


def query_find(query):
    """Searching General query in wolframalpha"""
    # Used to add '+' sign instead of ' ' in search query
    for word in weby:
        if word in query:
            query = query.replace(word, "")
    print(query)
    modified_query = urllib.parse.quote_plus(query)
    url = f'http://api.wolframalpha.com/v2/query?appid={os.environ.get("WOLFRAMAPI")}&input={modified_query}&format=plaintext&output=json'
    response = requests.get(url).json()
    try:
        data = response["queryresult"]["pods"][1]["subpods"][0]["plaintext"]
        return data
    except:
        return "Couldn't understand your language:("
