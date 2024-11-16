import requests


def check_ssl(url):
    try:
        r = requests.get(url, timeout=5)
        if r.url.startswith("https://"):
            return f"У сайта {url} есть SSL-сертификат."
        else:
            return f"У сайта {url} нет SSL-сертификат."
    except requests.exceptions.SSLError:
        return f"У сайта {url} нет SSL-сертификат."
    except Exception as e:
        return f"Не удалось проверить сайт {url}. Ошибка: {e}"


def main():
    url = input("URL: ")
    print(check_ssl(url))


if __name__ == "__main__":
    main()



