from operator import index, indexOf

from bs4 import BeautifulSoup
import requests


with open(file="website_sample.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.ul)
all_a_tags = soup.find_all("a")
for tag in all_a_tags:
    print(tag.getText())
    print("link is: ", tag.get("href"))

head_ing = soup.find(name="h1", id="name")
print(head_ing)
test_h3 = soup.find(name="h3", class_="heading")
print(test_h3)
css_selector_class = soup.select_one(selector=".heading")
print(css_selector_class)
css_selector_id = soup.select_one(selector="#name")
print(css_selector_id)
# from operator import length_hint

# college_years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
# print(list(enumerate(college_years, start=2016)))
# import math
# length = [1, 2, 3, 4]
# area = list(map(lambda x: x**2, length))
# print(area)
#
# bir = (1,1,1,1,0)
# print(all(bir))
# from collections import namedtuple
# Zek = namedtuple("Zek", ["x","y"])
# Zekai = Zek(44, 97)
# a,b = Zekai
# print(a,b)

web_resp = requests.get("https://news.ycombinator.com/news")
resp_text = web_resp.text
news_soup = BeautifulSoup(resp_text, "html.parser")

score_list = [int(row_new.getText().split(" ")[0]) for row_new in news_soup.find_all(name="span", class_="score")]
news_list = news_soup.select(selector=".titleline > a")
text_list, link_list = [], []
for row_new in news_list:
    text_list.append(row_new.getText())
    link_list.append(row_new.get("href"))

print(score_list)
print(text_list)
print(link_list)

max_upvote_index = score_list.index(max(score_list))
print(f"Most trending and upvoted title is: \"{text_list[max_upvote_index]}\", and can be accessed at: {link_list[max_upvote_index]}")


