# import sys, os
from modules.linkresolve import UrlCheck
from modules.search import SearchAnime
from modules.choose import Choose
from modules.episodes import AnimeName

# script_path = os.path.dirname(sys.argv[0])
# for may be importing modules path can be necessary

url = "https://www.animeout.xyz/"
resp, st_code = UrlCheck(url).st_code()
if st_code == 200:
    print(" Link exists")
    # inp_name = input("Type the anime name you want to search : ")
    inp_name = "boruto"
    res = SearchAnime(inp_name).search_anime()
    lists = SearchAnime.soup_extract(res)

    # print(Choose(lists).anime())
    print(lists)
    num = 1
    key2 = 0
    for key in lists:
        con = str(f'{lists[key]}')
        con.replace("{}''", '')
        print(f'{num}-->>{con}')
        num = num + 1

    # choice = int(input("Type the number of anime you want to watch"))
    # # try:
    #     # here i want the chooice option but i am stuck
    #     # and this all choice will be later put on choice module  just foe testing purpose



# starting for ep list counter

name = "boruto"
link = "https://www.animeout.xyz/boruto/"
print(AnimeName(name, link).episodes())
