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
        lists = {}
        num = 0
        for articles in li:
            a_loc = articles.select('.post-title a')
            num = num + 1
            for resul in a_loc:
                links = resul.attrs['href']
                title = resul.getText()
                lists[num] = {"Title": title, "Link": links}
        return lists

