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

    def __init__(self, prev, target) -> None:
        """
        Initializes based on [urls/titles/nodes]
        """
        # initialize other stuff
        self.g = prev.g + 1
        self.h = heuristic(self, target)
        self.f = self.g + self.h

    def get_next(self) -> None:
        """
        get list of connected [urls/titles/nodes]
        """
        pass

class PQ:
    """
    [Heap] implementation of priority queue
    """
    heap = []

    def __init__(self) -> None:
        heap = [0]

    def insert(self, new) -> None:
        """
        Insert new element in Priority queue
        """
        pass

    def remove(self, to_remove) -> None:
        """
        remove element from priority queue
        """
        pass

def a_star(source, target) -> list:
    """
    Returns path from source to target using A* search algorithm
    """
    pass