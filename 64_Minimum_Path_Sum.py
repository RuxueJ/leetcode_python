class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[m - 1][n - 1]

        # m, n = len(grid), len(grid[0])
        # self.min_sum = float('inf')

        # def dfs(i,j,current_sum):
        #     if i == m-1 and j == n - 1:
        #         self.min_sum = min(self.min_sum, current_sum + grid[i][j])
        #         return

        #     current_sum += grid[i][j]

        #     if i + 1 < m:
        #         dfs(i+1,j, current_sum)
        #     if j + 1 < n:
        #         dfs(i,j+1, current_sum)

        # dfs(0,0,0)
        # return self.min_sum

