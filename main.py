from app import app
import requests

def main():
    title = 'Apple'

    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "links"
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    PAGES = DATA["query"]["pages"]

    for k, v in PAGES.items():
        for l in v["links"]:
            print(l["title"])
