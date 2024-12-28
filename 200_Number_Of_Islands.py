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

    # m, n = len(grid), len(grid[0])
    # visited = set()
    # island = 0
    #
    # def bfs(x, y):
    #     queue = deque([(x, y)])
    #     visited.add((x, y))
    #
    #     while queue:
    #         i, j = queue.popleft()
    #         for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    #             nx, ny = di + i, dj + j
    #             if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and grid[nx][ny] == "1":
    #                 visited.add((nx, ny))
    #                 queue.append((nx, ny))
    #
    # for i in range(m):
    #     for j in range(n):
    #         if grid[i][j] == "1" and (i, j) not in visited:
    #             island += 1
    #             bfs(i, j)
    #
    # return island




