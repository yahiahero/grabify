import requests


class UrlCheck:
    def __init__(self, link):
        self.link = link

    def st_code(self):
        url = self.link
        r = requests.get(url)
        # this isn't used yet
        # resp = r.text
        return r, r.status_code

