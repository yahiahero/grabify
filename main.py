# import sys, os
from modules.linkresolve import UrlCheck
from modules.search import SearchAnime
# script_path = os.path.dirname(sys.argv[0])
# for may be importing modules path can be necessary

url = "https://www.animeout.xyz/"
resp, st_code = UrlCheck(url).st_code()
if st_code == 200:
    print("exists")
    # inp_name = input("Type the anime name you want to search : ")
    inp_name = "boruto"
    res = SearchAnime(inp_name).search_anime()
    lists = SearchAnime.soup_extract(res)
    print(lists)