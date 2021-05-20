from _typeshed import NoneType
from typing import Union


def heuristic(a, b) -> int:
    """
    Returns predicted cost (distance) from a to b
    """
    pass

class Article:
    """
    article class
    """
    title: str
    target: str
    g: float
    f: float
    parent: Union[object, NoneType]

    def __init__(self, title: str, target: str, parent: Union[object, NoneType]):
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

    def get_children(self) -> list[Article]:
        """
        return list of connected (children) article object using wikipedia API
        """
        pass

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
    cur : Article = Article(source, target, None)
    queue : PQ = PQ(cur)
    while (cur != target):
        nexts = cur.get_children()
        for next in nexts:
            queue.insert(next)
        cur = queue.pop()
    
    path = [cur]

    while path[0] != source:
        cur = cur.parent
        path.insert(0, cur.title)
    
    return path