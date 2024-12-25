class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        visited = set()
        max_area = 0

        def dfs(i, j):
            visited.add((i, j))

            area = 1
            visited.add((i, j))
            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]
                if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == 1 and (new_i, new_j) not in visited:
                    area += dfs(new_i, new_j)
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = dfs(i, j)
                    max_area = max(area, max_area)

        return max_area

