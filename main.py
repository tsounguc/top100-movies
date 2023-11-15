import  requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

movies_page = response.text

soup = BeautifulSoup(movies_page, 'html.parser')

# print(soup.prettify())

movies = soup.find_all(name="div", class_="article-title-description__text")

movie_titles = [movie.find(name='h3').getText() for movie in movies]

movie_titles.reverse()

print(movie_titles)

for movie in movie_titles:
    with open("movie.txt", mode="a", encoding="utf-8") as file:
        file.write(f"{movie}\n")
