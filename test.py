import requests
from bs4 import BeautifulSoup as BS


url = "https://www.animeout.xyz/?s=boruto"
r = requests.get(url).text
soup = BS(r, 'lxml')
list = soup.select(".post-item")
for item in list:
    print(item)
