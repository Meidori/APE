import requests
from bs4 import BeautifulSoup as bs
import random


def get_description(link):
    # делает отдельный запрос на каждую страницу фильма, чтобы получить описание
    # эта функция вызывается в цикле 10 раз
    # это 10 дополнительных запросов
    # Запросы занимают значительное время - поэтому программа выполняется максимально медленно
    base_url = "https://www.imdb.com"
    url = base_url + link
    # Чтобы не было 403 Forbidden
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = bs(response.text, "html.parser")
            description = soup.find('span', class_="sc-3ac15c8d-2 fXTzFP").get_text().strip()
            return(description)

        else:
            print("Ошибка при запросе страницы {page}: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка: {e}")


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
            # Неоптимальная работа с данными, поэтому не включает все 250 фильмов со странице
            links = [a["href"] for a in soup.find_all('a', class_="ipc-title-link-wrapper", href=True)]                                 
            titles = [a.find('h3').get_text().strip() for a in soup.find_all('a', class_="ipc-title-link-wrapper") if a.find('h3')]
            
            recs = dict()
            for i in range(10):
                index = random.randrange(len(titles))
                
                key = titles[index]; del titles[index]
                space = key.find(" ")
                key = key[space + 1:]

                link = links[index]; del links[index]
                value = get_description(link)

                recs[key] = value

            return recs
                

        else:
            print("Ошибка при запросе страницы {page}: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка: {e}")


def main():
    # Программа работает максимально медленно
    # + она берет только первые 25 фильмов, а не 250
    movies = get_random_top_10_movies()
    for k, v in movies.items():
        print("--------------------")
        print(k)
        print(f"\n{v}")


if __name__ == "__main__":
    main()