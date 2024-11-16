import requests


def get_info(url):
    r = requests.get(url)

    response_info = {
        "Status Code": r.status_code,
        "Headers": r.headers,
        "Url": r.url,
        "History": r.history,
        "Encoding": r.encoding,
        "Reason": r.reason,
        "Cookies": r.cookies,
        "Elapsed": r.elapsed,
        "Request": r.request,
        "Content": r.content[:200]
    }
    return response_info


def main():
    url = input("URL: ")
    info = get_info(url)
    for key, value in info.items():
        print(f"{key}: {value}")
            
    return 0


if __name__ == "__main__":
    main()
