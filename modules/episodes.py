import requests
from bs4 import BeautifulSoup as BS


class AnimeName:
    def __init__(self, name, link):
        self.name = name
        self.link = link

    def episodes(self):
        name = self.name
        link = self.link
        req = requests.get(link).text
        soup = BS(req, 'lxml')
        article = soup.select("div .article-content p a")
        for a in article:
            if a.attrs['href'] is not None:
                ep = a.getText()
                li = a.attrs['href']
                if ep != "Openload.co":
                    if ep == "Direct Download":
                        print(f'{li}')
                    else:
                        print(f' {ep} --> {li}')
