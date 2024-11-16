import requests


def get_text(url):
    try:
        r = requests.get(url)
        r.raise_for_status()  # Проверка на успешный ответ (код 200)
        print(r.text)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")


def main():
    url = "https://en.wikipedia.org/robots.txt"
    get_text(url)


if __name__ == "__main__":
    main()