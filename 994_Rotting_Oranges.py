from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rotting = set()
        queue = deque()

        m, n = len(grid), len(grid[0])

        oranges_number = 0

        minutes = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotting.add((i, j))
                    queue.append((i, j))
                    oranges_number += 1
                elif grid[i][j] == 1:
                    oranges_number += 1

        if oranges_number == 0:
            return 0

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and (nx, ny) not in rotting:
                        queue.append((nx, ny))
                        rotting.add((nx, ny))
            minutes += 1

        if len(rotting) == oranges_number:
            return minutes - 1
        else:
            return -1





