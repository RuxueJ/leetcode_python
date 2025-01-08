class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = {i: [] for i in range(n)}

        for u, v in connections:
            graph[u].append((v, True))
            graph[v].append((u, False))

        visited = set()

        self.edges_change = 0

        def dfs(city):

            visited.add(city)
            for neighbor, is_forward in graph[city]:
                if neighbor not in visited:
                    if is_forward:
                        self.edges_change += 1
                    dfs(neighbor)

        dfs(0)

        return self.edges_change




