import requests
from bs4 import BeautifulSoup as BS


class SearchAnime:
    def __init__(self, name):
        self.name = name

    def search_anime(self):
        anime = self.name
        query_link = f'https://www.animeout.xyz/?s={anime}'
        res = requests.get(query_link).text
        return res

    def soup_extract(r):
        soup = BS(r, 'lxml')
        li = soup.select(".post-item")
        num = 0
        lists = {}
        for articles in li:
            title = soup.select(".post-title a").getText()
            lists.update({num: title})
            num = num + 1
        return lists

    # // article[] / div / div / h3 / a xpath selector

