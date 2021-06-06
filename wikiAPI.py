"""
This file contains all the WikiMedia API request related functions. A sample call would look like:
https://en.wikipedia.org/w/api.php?action=query&titles=Albert%20Einstein&prop=links&pllimit=max
for the query Albert Eintein
"""
import requests

mockTitle = "Dog"
mockURL = "https://en.wikipedia.org/w/api.php?action=query&titles=Apple&prop=links&pllimit=max&format=json"


def get_links(title: str) -> str:
    """
    Given a query that can be assumed to be a Wikipedia Article Title, get the JSON for links back.
    """
    baseURL = "https://en.wikipedia.org/w/api.php?action=query&titles=TEMP&prop=links&pllimit=max&format=json"
    query = title.replace(" ", "%20")
    return baseURL.replace("TEMP", query)


def get_JSON(link: str) -> dict:
    """
    Given a query that can be assumed to be a valid Wikipedia API link to a JSON format, get the JSON data back.
    """
    s = requests.Session()
    r = s.get(link)
    return r.json()


def get_title(link: str) -> str:
    """
    Given a query that can be assumed to be a valid Wikipedia API link to a JSON format, get the title to the article.
    """
    file = get_JSON(link)
    id = list(file['query']['pages'])[0]
    return file['query']['pages'][id]['title']

def get_url(title: str) -> str:
    """
    Given a query that can be assumed to be a valid Wikipedia title, get the link to the article.
    """
    articleURL = "https://en.wikipedia.org/wiki/TEMP"
    query = title.replace(" ", "%20")
    return articleURL.replace("TEMP", query)

def get_intro(link: str) -> str:
    """
    Given a query that can be assumed to be a valid Wikipedia API link to a JSON format, get the intro to the article. 
    """
    file = get_JSON(link)
    id = list(file['query']['pages'])[0]
    return file['query']['pages'][id]['extract']

def clean_title(title: str) -> str:
    """
    Cleans a str such that it is appropriate to act as a Wikipedia title
    """
    title  = title.replace(" ", "%20")
    title = title.replace("&", "%26")
