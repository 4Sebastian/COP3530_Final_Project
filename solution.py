from typing import Tuple, List, Optional


class Node:
    def __init__(self, pos: Tuple[int, int]):
        self.pos = pos
        self.next = None


class solution_handler:
    def calculate_path(self, start: Tuple[int, int], end: Tuple[int, int], terrain: List[List[float]]) -> Node:
        """calculates the path in terms of the inherited class and returns the head of a linked list, which contains nodes each with a position creating a connected path"""
        pass