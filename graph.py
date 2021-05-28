from __future__ import annotations
import typing
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from bs4 import BeautifulSoup
from wikiAPI import get_JSON
from typing import List


def heuristic(a: str, b: str):
    """
    Returns predicted cost (distance) from two titles a to b, through the cosine similarity of two generated
    term-document matrices of the article. The heuristic in this case is purely semantic.

    The HTML enriched query for the JSON is:
    https://en.wikipedia.org/w/api.php?action=parse&page=TITLE&prop=text&formatversion=2&format=json
    """
    query = "https://en.wikipedia.org/w/api.php?action=parse&page=TEMP&prop=text&formatversion=2&format=json"
    startURL = query.replace("TEMP", a)
    endURL = query.replace("TEMP", b)
    # text processing using SOUP
    initialSoup = BeautifulSoup(get_JSON(startURL)['parse']['text'], 'html.parser')
    finalSoup = BeautifulSoup(get_JSON(endURL)['parse']['text'], 'html.parser')
    # generate term-document matrices
    corpus = [initialSoup.get_text().replace('\n', ' '), finalSoup.get_text().replace('\n', ' ')]
    vect = TfidfVectorizer()
    mat = vect.fit_transform(corpus)
    # return cosine similarity
    return cosine_similarity(mat[0:1], mat)


class Article:
    """
    article class
    """
    title: str
    target: str
    g: float
    f: float
    parent: typing.Union[Article, type(None)]

    def __init__(self, title: str, target: str, parent: typing.Union[Article, type(None)]):
        """
        Initializes based on [urls/titles/nodes]
        """
        self.title = title
        self.target = target

        if parent:
            self.parent = parent
            self.g = parent.g + 1
        else:
            self.parent = None
            self.g = 0

        h = heuristic(title, target)
        self.f = self.g + h

    def get_children(self, cont: typing.Union[str, type(None)]) -> List[str]:
        """
        return list of connected (children) article object using wikipedia API
        """
        s = requests.Session()

        url = "https://en.wikipedia.org/w/api.php"

        if cont is None:
            params = {
                "action": "query",
                "format": "json",
                "titles": self.title,
                "prop": "links",
                "pllimit": "max"
            }
        else:
            params = {
                "action": "query",
                "format": "json",
                "titles": self.title,
                "prop": "links",
                "pllimit": "max",
                "plcontinue": cont
            }

        titles_so_far = []

        r = s.get(url=url, params=params)
        data = r.json()

        pages = data["query"]["pages"]

        for k, v in pages.items():
            for l in v["links"]:
                titles_so_far.append(l["title"])

        if "batchcomplete" in data:
            return titles_so_far
        else:
            contHolder = data["continue"]["plcontinue"]
            titles_so_far.extend(self.get_children(contHolder))
            return titles_so_far

        # return [Article(child, self.target, self.title) for child in titles_so_far]


class PQ:
    """
    [Heap] implementation of priority queue
    """
    heap = []

    def __init__(self, root):
        heap = [0, root]

    def insert(self, new: Article) -> None:
        """
        Insert new element in Priority queue
        """
        pass

    def pop(self, to_remove: str) -> Article:
        """
        pops minimum element from priority queue
        """
        pass


def a_star(source: str, target: str) -> list:
    """
    Returns path from source to target using A* search algorithm
    """
    cur: Article = Article(source, target, None)
    queue: PQ = PQ(cur)
    while cur != target:
        nexts = cur.get_children()
        for curr in nexts:
            queue.insert(curr)
        cur = queue.pop()

    path = [cur]

    while path[0] != source:
        cur = cur.parent
        path.insert(0, cur.title)

    return path
