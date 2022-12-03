import random
from collections import deque
from typing import Tuple, List

from solution import solution_handler, Node


class DFS_Handler(solution_handler):
    def calculate_path(self, start: Tuple[int, int], end: Tuple[int, int], terrain: List[List[float]]) -> Node | None:

        visited = set()
        prev = dict()
        distance = 0
        nexts = deque()

        nexts.append(start)
        visited.add(start)

        while len(nexts) > 0:
            current = nexts.pop()
            x, y = current

            if current == end:
                return self.generate_list(prev, end)

            temp = []

            up = (x - 1, y)
            if x > 0 and up not in visited:
                temp.append(up)
                prev[up] = current
                visited.add(up)

            right = (x, y + 1)
            if y < len(terrain)-1 and right not in visited:
                temp.append(right)
                prev[right] = current
                visited.add(right)

            down = (x + 1, y)
            if x < len(terrain)-1 and down not in visited:
                temp.append(down)
                prev[down] = current
                visited.add(down)

            left = (x, y - 1)
            if y > 0 and left not in visited:
                temp.append(left)
                prev[left] = current
                visited.add(left)
            random.shuffle(temp)
            nexts.extend(temp)
            distance += 1

            # temp = nexts.copy()
            # neighbors = deque()
            # print()
            # while len(temp) > 0:
            #     current = temp.popleft()
            #     x, y = current
            #     visited.add(str(current))
            #
            #     if current == end:
            #         # Do something here
            #         return distance
            #
            #     if x > 0 and self.check_neighbor((x - 1, y), visited, terrain):
            #         neighbors.append((x - 1, y))
            #
            #     if y < len(terrain) and self.check_neighbor((x, y + 1), visited, terrain):
            #         neighbors.append((x, y + 1))
            #
            #     if x < len(terrain) and self.check_neighbor((x + 1, y), visited, terrain):
            #         neighbors.append((x + 1, y))
            #
            #     if y > 0 and self.check_neighbor((x, y - 1), visited, terrain):
            #         neighbors.append((x, y - 1))
            #
            # nexts = neighbors.copy()
            # distance += 1

        return None


