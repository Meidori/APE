from urllib.request import urlopen
from bs4 import BeautifulSoup


# Header Tags: <h1>-<h6>
def get_header_tags(url): 
    r = urlopen(url)
    soup = BeautifulSoup(r, "html.parser")
    headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    return headers


def main():
    url = "https://en.wikipedia.org/wiki/Main_Page"
    header_tags = get_header_tags(url)
    for x in header_tags:
        print(x)


if __name__ == "__main__":
    main()