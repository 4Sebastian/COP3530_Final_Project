from typing import Tuple, List

from solution import solution_handler, Node


class bfs_handler(solution_handler):
    def calculate_path(self, start: Tuple[int, int], end: Tuple[int, int], terrain: List[List[float]]) -> Node:
        return None