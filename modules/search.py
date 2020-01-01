import requests
from bs4 import BeautifulSoup as BS


class SearchAnime:
    def __init__(self, name):
        self.name = name

    # returns search page (response.text)
    def search_anime(self):
        anime = self.name
        query_link = f'https://www.animeout.xyz/?s={anime}'
        res = requests.get(query_link).text
        return res

    #  returns {1: {Title: 'One Punch Man', 'Link': 'https://.........'}, 2.....}
    def soup_extract(r):
        soup = BS(r, 'lxml')
        # .post-item > div > div[1] > .post-title > a
        a_loc = soup.select('.post-title a')
        lists = {}
        for resul in a_loc:
            # < a href="link to anime webpage"> Anime Title </a>
            link = resul.attrs['href']
            title = resul.getText()
            # dict[key] = value
            # lists[num] = {"Title": title, "Link": link}
            lists.update({title: link})
        return lists

