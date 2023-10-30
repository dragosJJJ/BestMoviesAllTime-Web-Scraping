import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
data = response.text

soup = BeautifulSoup(data, "html.parser")
titles = [title.text for title in soup.find_all(name="h3", class_="title")]
titles.reverse()
with open("top_movies_of_all_time", "w", encoding="utf-8") as file:
    for title in titles:
        file.write(f"{title}\n")

