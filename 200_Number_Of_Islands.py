class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set()

        m = len(grid)
        n = len(grid[0])
        island = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(i, j):
            visited.add((i, j))
            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]
                if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == "1" and (new_i, new_j) not in visited:
                    dfs(new_i, new_j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    island += 1
                    dfs(i, j)

        return island



