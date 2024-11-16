import requests
import pandas as pd


def line_count_in_csv(url):
    r = requests.get(url)
    with open("earthquake_data.csv", "wb") as f:
        f.write(r.content)

    data = pd.read_csv("earthquake_data.csv")
    return len(data)


def main():
    url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.csv"
    print(line_count_in_csv(url))


if __name__ == "__main__": 
    main()