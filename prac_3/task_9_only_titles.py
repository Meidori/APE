import requests
from bs4 import BeautifulSoup as bs
import random


def get_random_top_10_movies():
    url = "https://www.imdb.com/chart/top/"
    # Чтобы не было 403 Forbidden
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = bs(response.text, "html.parser")
            # Неоптимальная работа с данными, поэтому не включает все 250 фильмов со страницы
            titles = [a.find('h3').get_text().strip() for a in soup.find_all('a', class_="ipc-title-link-wrapper") if a.find('h3')]

            recs = list()
            for i in range(10):
                index = random.randrange(len(titles))
                
                space = titles[index].find(" ")
                recs.append(titles[index][space + 1:]); del titles[index]

            return recs
                

        else:
            print("Ошибка при запросе страницы {page}: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка: {e}")


def main():
    # Программа берет только первые 25 фильмов, а не 250
    movies = get_random_top_10_movies()
    for x in movies:
        print(x, "\n")


if __name__ == "__main__":
    main()