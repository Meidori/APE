import requests
from bs4 import BeautifulSoup


def get_links(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links


def main():
    url = "https://en.wikipedia.org/wiki/Python"
    links = get_links(url)
    for x in links:
        print(x)
    

if __name__ == "__main__":
    main()