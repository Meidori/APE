from urllib.request import urlopen
from urllib.error import HTTPError, URLError


def check_page(url):
    try:
        req = urlopen(url)
    except HTTPError as e:
        print(f"HTTP ошибка: {e.code} - {e.reason}")
    except URLError as e:
        print(f"URL ошибка: {e.reason}")
    else:
        print(f"Ответ запроса: {req.status}")


def main():
    url = input("Введите URL: ")
    check_page(url)


if __name__ == "__main__":
    main()
