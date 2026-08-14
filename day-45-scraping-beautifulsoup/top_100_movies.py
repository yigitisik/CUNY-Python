from traceback import print_tb

import requests
from bs4 import BeautifulSoup

#practice 1) archive scraping from html
with open(file="film_webpage_archive.html") as file:
    web_endpoint_archive_page = file.read()
web_soup_archive_page = BeautifulSoup(web_endpoint_archive_page, "html.parser")
titles = web_soup_archive_page.find_all(name="h3", class_="title")
# print(titles)

title_texts = []
for title in titles:
    movie_text = title.getText()
    title_texts.append(movie_text)
cleaned_ordered_list = title_texts[::-1] #can do reverse() as well
print(cleaned_ordered_list)
with open("top_100_movies_archive.txt", mode="w") as file:
    for movie in cleaned_ordered_list:
        file.write(f"{movie}\n")

#practice 2) current active scraping from html
with open(file="film_webpage_active_curr.html") as file:
    web_endpoint_curr_page = file.read()
web_soup_curr_page = BeautifulSoup(web_endpoint_curr_page, "html.parser")
titles_curr = web_soup_curr_page.select(selector="h2 > strong")
# print(titles_curr)

title_texts_curr = []
for title_curr in titles_curr:
    movie_text_curr = title_curr.getText()
    title_texts_curr.append(movie_text_curr)
cleaned_ordered_list_curr = title_texts_curr[::-1] #can do reverse() as well
print(cleaned_ordered_list_curr)
with open("top_100_movies_curr.txt", mode="w") as file:
    for movie in cleaned_ordered_list_curr:
        file.write(f"{movie}\n")

#practice 3) archive scraping from web with API
endpoint="https://www.empireonline.com/movies/features/best-movies-2/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml"
}
response = requests.get(url=endpoint, headers=headers)
web_soup_get_page = BeautifulSoup(response.text, "html.parser")
web_page_list = web_soup_get_page.select("h2 strong")
# can do the [::-1] or .reverse() or can do it another way in the file writing section below
# cleaned_ordered_list_web = web_page_list[::-1]
# print(cleaned_ordered_list_web)

with open("top_100_movies_web.txt", mode="w") as file:
    for i in range(len(web_page_list)-1, -1, -1):
        file.write(f"{web_page_list[i].text}\n")


