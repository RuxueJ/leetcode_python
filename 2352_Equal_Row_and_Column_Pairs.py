from collections import defaultdict


class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        row_dic = defaultdict(int)
        col_dic = defaultdict(int)

        for i in range(n):
            row_dic[tuple(grid[i])] += 1

        for j in range(n):
            col_dic[tuple(grid[r][j] for r in range(n))] += 1

        count = 0

        for row in row_dic:
            if row in col_dic:
                count += row_dic[row] * col_dic[row]

        return count











