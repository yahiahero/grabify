import sys, os
from modules.linkresolve import UrlCheck
from modules.search import SearchAnime
from modules.choose import Choose
from modules.episodes import AnimeName
from modules.downloader import Downloader

script_path = os.path.dirname(sys.argv[0])


# url = "https://www.animeout.xyz/"
# resp, st_code = UrlCheck(url).st_code()
# if st_code == 200:
#     print(" Link exists")
#     # inp_name = input("Type the anime name you want to search : ")
#     inp_name = "one punch man"
#     res = SearchAnime(inp_name).search_anime()
#     lists = SearchAnime.soup_extract(res)
#
#     # print(Choose(lists).anime())
#     print(lists)
#     # enumerate turns sequence to pair by numbering; from start=int
#     for k, v in enumerate(lists.keys(), start=1):
#         print(f'{k} ==> Title: {v} || Link: {lists[v]}')
#
#     # choice = int(input("Type the number of anime you want to watch"))
#     # # try:
#     #     # here i want the chooice option but i am stuck
#     #     # and this all choice will be later put on choice module  just foe testing purpose



# starting for ep list counter

# name = "boruto"
# link = "https://www.animeout.xyz/boruto/"
# print(AnimeName(name, link).episodes())

link = "https://up1.haylimoviez.info/Sereias/GOT/S08/WEB-DL%20480p%20HayliMoviez/game.of.thrones.s08e01.480p.web.x264-HayliMoviez.mkv"
resp, fl_size, fl_type = Downloader(link).size_calculate()
# chunk_size, chunk_list = Downloader.spit_size(fl_size)
chunk_size = Downloader.spit_size(fl_size)

print(fl_type)
file_name = input("Type the file name you want to save as : ")
print(Downloader.extension(fl_type))
file_ext = Downloader.extension(fl_type)
fl_path = f'{script_path}/{file_name}.{file_ext}'
print(f'Saving File as {fl_path}')
print(Downloader.download_chunks(chunk_size, fl_path, resp))

