import requests
import urllib3

global file_size


class Downloader():

    def __init__(self, link):
        self.link = link
        # self.header = header

    def size_calculate(self):
        link = self.link
        req = requests.get(link, stream=True, verify=False)
        content_length = req.headers['Content-Length']
        content_type = req.headers['content-type']
        return req, content_length, content_type

    def spit_size(leng):
        c = 8
        length = int(leng)
        diff = int(length / 8)
        ct_diff = diff
        # chunks = {}
        # st = 0
        # for i in range(1,8):
        #     diff = ct_diff * i
        #     chunks[i] = {st: diff}
        #     st = diff
        # chunks[8] = {diff: leng}
        # return ct_diff, chunks
        return ct_diff

    def download_chunks(chunk_size, fl_path, resp):
        handle = open(fl_path, "wb")
        c = 1
        for chunk in resp.iter_content(chunk_size=50000):
            print(f'Got chunk {c}')
            c = c + 1
            if chunk:  # filter out keep-alive new chunks
                handle.write(chunk)
        return f'Download Complete!!'
    def extension(fl_type):
        ext = {
            "video/mp4": "mp4",
            "video/mpeg": "mpeg",
            "video/ogg": "ogg",
            "video/MPV": "MPV",
            "video/x-matroska": "mkv",
            "application/octet-stream": "mkv",
            "audio/mp3": "mp3",
            "image/jpeg": "jpg"
        }
        try:
            ext = ext[fl_type]
        except KeyError:
            ext = "raw"
        return ext