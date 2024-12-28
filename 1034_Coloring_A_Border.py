class Solution(object):
    def colorBorder(self, grid, row, col, color):
        """
        :type grid: List[List[int]]
        :type row: int
        :type col: int
        :type color: int
        :rtype: List[List[int]]
        """

        original_color = grid[row][col]
        m, n = len(grid), len(grid[0])
        visited = set()
        boarder_cells = []

        def dfs(x, y):
            visited.add((x, y))
            is_boarder = False

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = dx + x, dy + y

                if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] != original_color:
                    is_boarder = True
                elif (nx, ny) not in visited:
                    dfs(nx, ny)
            if is_boarder:
                boarder_cells.append((x, y))

        dfs(row, col)

        for x, y in boarder_cells:
            grid[x][y] = color

        return grid




