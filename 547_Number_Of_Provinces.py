class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)

        visited = set()

        provinces = 0

        def dfs(i):
            visited.add(i)
            for neighbor in range(n):
                if neighbor not in visited and isConnected[i][neighbor] == 1:
                    dfs(neighbor)

        for i in range(n):
            if i not in visited:
                dfs(i)
                provinces += 1

        return provinces
