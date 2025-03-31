from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m, n = len(board), len(board[0])

        def dfs(i, j, startIndex):
            if startIndex == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[startIndex]:
                return False

            temp = board[i][j]
            board[i][j] = '*'

            directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

            for di, dj in directions:
                ni = di + i
                nj = dj + j
                if dfs(ni, nj, startIndex + 1):
                    return True
            board[i][j] = temp  # **Restore original character (Backtracking)**
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False
