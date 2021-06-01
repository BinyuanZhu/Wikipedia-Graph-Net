from __future__ import annotations
import typing
import requests
import heapq
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from bs4 import BeautifulSoup
from wikiAPI import get_JSON
from typing import List, Type, Callable
import urllib.parse


def heuristic_0(a: str, b: str) -> float:
    return 0


def heuristic_1(a: str, b: str) -> float:
    """
    Returns predicted cost (distance) from two titles a to b, through the cosine similarity of two generated
    term-document matrices of the article. The heuristic in this case is purely semantic.

    The HTML enriched query for the JSON is:
    https://en.wikipedia.org/w/api.php?action=parse&page=TITLE&prop=text&formatversion=2&format=json
    """
    query = "https://en.wikipedia.org/w/api.php?action=parse&page=TEMP&prop=text&formatversion=2&format=json"
    startURL = (query.replace("TEMP", a.replace(" ", "%20"))).replace("&", "%26")
    endURL = (query.replace("TEMP", b.replace(" ", "%20"))).replace("&", "%26")
    # text processing using SOUP
    initialSoup = BeautifulSoup(get_JSON(startURL)['parse']['text'], 'html.parser')
    finalSoup = BeautifulSoup(get_JSON(endURL)['parse']['text'], 'html.parser')
    # generate term-document matrices
    corpus = [initialSoup.get_text().replace('\n', ' '), finalSoup.get_text().replace('\n', ' ')]
    vect = TfidfVectorizer()
    mat = vect.fit_transform(corpus)
    # return cosine similarity
    return cosine_similarity(mat[0:1], mat)[0][1]


def heuristic_2(a: str, b: str):
    """
    Returns predicted cost (distance) from two titles a to b, through the cosine similarity of two generated
    term-document matrices of the article. The heuristic in this case is purely semantic.

    The HTML enriched query for the JSON is:
    https://en.wikipedia.org/w/api.php?action=query&titles=TITLE&prop=extracts&format=json&exintro=1
    """
    query = "https://en.wikipedia.org/w/api.php?action=query&titles=TEMP&prop=extracts&format=json&exintro=1"
    startURL = query.replace("TEMP", a.replace(" ", "%20"))
    endURL = query.replace("TEMP", b.replace(" ", "%20"))
    # text processing using SOUP
    startText = get_JSON(startURL)['query']['pages']
    endText = get_JSON(endURL)['query']['pages']
    startId = list(startText)[0]
    endId = list(endText)[0]
    initialSoup = BeautifulSoup(startText[startId]['extract'], 'html.parser')
    finalSoup = BeautifulSoup(endText[endId]['extract'], 'html.parser')
    # generate term-document matrices
    corpus = [initialSoup.get_text().replace('\n', ' '), finalSoup.get_text().replace('\n', ' ')]
    vect = TfidfVectorizer()
    mat = vect.fit_transform(corpus)
    # return cosine similarity
    return cosine_similarity(mat[0:1], mat)[0][1]

def semantic_similarity(a: str, b: str) -> float:
    web_model = WebBertSimilarity(device='cpu', batch_size=10)
    return web_model.predict([(a, b)])

class Article:
    """
    This is the article class that represents each Wikipedia article.

    Instance Variables:
        - title: str that represents the title of the article
        - target: the final target given by the user
        - g:
        - f:
    """
    title: str
    target: str
    g: float
    f: float
    parent: typing.Union[Article, Type(None)]
    heuristic: Callable[[str, str], float] 

    def __init__(self, title: str, target: str, parent: typing.Union[Article, Type(None)], heuristic: Callable[[str, str], float] ):
        """
        Initializes based on [urls/titles/nodes]
        """
        self.title = title
        self.target = target
        self.heuristic = heuristic

        if parent:
            self.parent = parent
            self.g = parent.g + 1
        else:
            self.parent = None
            self.g = 0

        h = self.heuristic(title, target)
        self.f = self.g + h

    def get_children(self, cont: typing.Union[str, Type(None)]) -> List[str]:
        """
        Return list of connected (children) article object using the wikipedia API functions.
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
            if "links" not in v:
                return []

            for l in v["links"]:
                titles_so_far.append(l["title"])

        if "batchcomplete" in data:
            return titles_so_far
        else:
            contHolder = data["continue"]["plcontinue"]
            titles_so_far.extend(self.get_children(contHolder))
            return titles_so_far

        # return [Article(child, self.target, self.title) for child in titles_so_far]

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def __eq__(self, other):
        return self.title == other.title

    def __ne__(self, other):
        return self.title != other.title

    def __gt__(self, other):
        return self.f > other.f

    def __ge__(self, other):
        return self.f >= other.f


class PQ:
    """
    MinHeap implementation of a priority queue for A* search.
    """
    heap = []

    def __init__(self, root: Article):
        self.heap = [root]

    def insert(self, to_insert: Article) -> None:
        """
        Insert new element in Priority queue
        """
        heapq.heappush(self.heap, to_insert)

    def pop(self) -> Article:
        """
        pops minimum element from priority queue
        """
        return heapq.heappop(self.heap)


def a_star(source: str, target: str, heuristic: Callable[[str, str], float] ) -> list:
    """
    Returns path from source to target using A* search algorithm.
    """
    visited: set = set((source))
    cur: Article = Article(source, target, None, heuristic)
    queue: PQ = PQ(cur)
    while cur.title != target:
        nexts = cur.get_children(None)
        for next in nexts:
            if next not in visited:
                queue.insert(Article(next, target, cur, heuristic))
                visited.add(next)
        cur = queue.pop()
        print(cur.f, cur.title)

    path = [cur.title]

    while path[0] != source:
        cur = cur.parent
        path.insert(0, cur.title)

    return path


print(a_star("Nucleus", "Tehran", heuristic_2))
