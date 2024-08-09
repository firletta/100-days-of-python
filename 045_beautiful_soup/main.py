from bs4 import BeautifulSoup
import requests


def main():
    movies = scrape_movies()
    save_movies(movies)
    

def scrape_movies():
    response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
    yc_webpage = response.text

    soup = BeautifulSoup(yc_webpage, "html.parser")

    all_movies_soup = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
    return [movie.getText() for movie in all_movies_soup][::-1]


def save_movies(movies):
    with open("movies.txt", mode="w") as file:
        for movie in movies:
            file.write(f"{movie}\n")



if __name__ == "__main__":
    main()
