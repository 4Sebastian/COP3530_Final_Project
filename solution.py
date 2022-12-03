from typing import Tuple, List, Optional


class Node:
    def __init__(self, pos: Tuple[int, int]):
        self.pos = pos
        self.next = None


class solution_handler:
    def calculate_path(self, start: Tuple[int, int], end: Tuple[int, int], terrain: List[List[float]]) -> Node | None:
        """calculates the path in terms of the inherited class and returns the head of a linked list, which contains nodes each with a position creating a connected path"""
        pass

    def break_down_linked_list(self, head: Node, terrain: List[List[float]]) -> Tuple[List[int], List[int], List[float]]:
        x_data = []
        y_data = []
        z_data = []
        while head:
            x, y = head.pos
            x_data.append(x)
            y_data.append(y)
            if x < len(terrain) and y < len(terrain):
                z_data.append(terrain[x][y])
            else:
                print(x,y)

            head = head.next

        return x_data, y_data, z_data

    def generate_list(self, prev: dict, end: Tuple[int, int]) -> Node:
        head = Node(end)
        while head.pos in prev:
            temp = head
            head = Node(prev[head.pos])
            head.next = temp
        return head