from bs4 import BeautifulSoup
import requests


def get_h1(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    h1 = soup.find("h1")
    return h1


def main():
    url = "http://www.example.com/"
    print(get_h1(url))


if __name__ == "__main__":
    main()