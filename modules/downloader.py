# import requests
import urllib3

global file_size


class Downloader():

    def __init__(self, link):
        self.link = link
        # self.header = header

    def size_calculate(self):
        link = self.link
        http = urllib3.PoolManager()
        # if want to use urllib3 instead of requests

        # req = requests.get(link)
        # request call takes a little longer
        # than urllib3 so request is replaced by urllib3

        req = http.request('GET', link)
        content_length = req.headers['Content-Length']
        content_type = req.headers['content-type']
        return content_length, content_type

    def spit_size(leng):
        c = 8
        leng = int(leng)
        diff = int(leng/8)
        return leng, diff

        # header = self.header

    def download_chunks(self):
        pas
