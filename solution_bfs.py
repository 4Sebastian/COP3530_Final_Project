from typing import Tuple, List
from collections import deque
from solution import solution_handler, Node


class BFS_Handler(solution_handler):
    def calculate_path(self, start: Tuple[int, int], end: Tuple[int, int], terrain: List[List[float]]) -> Node | None:

        visited = set()
        prev = dict()
        distance = 0
        nexts = deque()

        nexts.append(start)
        visited.add(start)

        while len(nexts) > 0:
            current = nexts.popleft()
            x, y = current

            if current == end:
                return self.generate_list(prev, end)

            up = (x - 1, y)
            if x > 0 and up not in visited:
                nexts.append(up)
                prev[up] = current
                visited.add(up)

            right = (x, y + 1)
            if y < len(terrain)-1 and right not in visited:
                nexts.append(right)
                prev[right] = current
                visited.add(right)

            down = (x + 1, y)
            if x < len(terrain)-1 and down not in visited:
                nexts.append(down)
                prev[down] = current
                visited.add(down)

            left = (x, y - 1)
            if y > 0 and left not in visited:
                nexts.append(left)
                prev[left] = current
                visited.add(left)

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
