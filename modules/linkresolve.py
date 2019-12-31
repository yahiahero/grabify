import requests


class UrlCheck:
    def __init__(self, link):
        self.link = link

    def st_code(self):
        url = self.link
        r = requests.get(url)
        resp = r.text
        return r, r.status_code

