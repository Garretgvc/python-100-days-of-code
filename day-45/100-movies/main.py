from bs4 import BeautifulSoup
import requests

response = requests.get("http://web.archive.org/web/20201116063517/https://www.empireonline.com/movies/features/best"
                        "-movies-2/")
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")
movie_tags = soup.find_all(name="h3", class_="title")

movie_list = []

for each in movie_tags:
    text = each.getText()
    movie_list.append(text)

# ordered_movies = list(reversed(movie_list))
ordered_movies = movie_list[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for each in ordered_movies:
        file.write(f"{each}\n")
