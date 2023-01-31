
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
print(response.status_code)

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "lxml")
articles = soup.find_all(class_="titleline")

article_texts = []
article_links = []

for article_tag in articles:
    a_text = article_tag.find(name="a").getText()
    article_texts.append(a_text)
    a_link = article_tag.find(name="a").get("href")
    article_links.append(a_link)

article_upvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

highest_upvote = 0
index = 0

for each in article_upvotes:
    if each > highest_upvote:
        highest_upvote = each
        index = article_upvotes.index(each)

print(article_texts[index])
print(article_links[index])
print(highest_upvote)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])

