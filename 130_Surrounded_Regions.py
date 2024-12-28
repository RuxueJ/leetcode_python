class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        visited = set()

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or (x, y) in visited or board[x][y] != "O":
                return
            visited.add((x, y))
            board[x][y] = "."
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx, ny = dx + x, dy + y
                dfs(nx, ny)

        for i in range(m):
            if board[i][0] == "O" and (i, 0) not in visited:
                dfs(i, 0)
            if board[i][n - 1] == "O" and (i, n - 1) not in visited:
                dfs(i, n - 1)

        for j in range(n):
            if board[0][j] == "O" and (0, j) not in visited:
                dfs(0, j)
            if board[m - 1][j] == "O" and (m - 1, j) not in visited:
                dfs(m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == ".":
                    board[i][j] = "O"


