from wikiAPI import *

def heuristic(a, b) -> int:
    """
    Returns predicted cost (distance) from a to b
    """
    pass

class article:
    """
    article class
    """

    def __init__(self, prev, target):
        """
        Initializes based on [urls/titles/nodes]
        """
        # initialize other stuff
        self.prev = prev
        self.g = prev.g + 1
        self.h = heuristic(self, target)
        self.f = self.g + self.h

    def get_next(self) -> list:
        """
        get list of connected [urls/titles/nodes]
        """
        pass

class PQ:
    """
    [Heap] implementation of priority queue
    """
    heap = []

    def __init__(self, root):
        heap = [0, root]

    def insert(self, new) -> None:
        """
        Insert new element in Priority queue
        """
        pass

    def pop(self, to_remove) -> article:
        """
        pops minimum element from priority queue
        """
        pass

def a_star(source: article, target: article) -> list:
    """
    Returns path from source to target using A* search algorithm
    """
    cur = source
    queue = PQ(cur)
    while (cur != target):
        nexts = cur.get_next()
        for next in nexts:
            queue.insert(next)
        cur = queue.pop()
    
    path = [cur]

    while path[0] != source:
        cur = cur.prev
        path.insert(0, cur)
    
    return path