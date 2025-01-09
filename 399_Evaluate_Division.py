from collections import defaultdict


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(list)

        for (A, B), value in zip(equations, values):
            graph[A].append((B, value))
            graph[B].append((A, 1 / value))

        def dfs(source, target, visited):
            if source not in graph or target not in graph:
                return -1.0
            if source == target:
                return 1.0

            visited.add(source)

            for neighbor, weight in graph[source]:
                if neighbor not in visited:
                    result = dfs(neighbor, target, visited)
                    if result != -1:
                        return result * weight

            return -1

        result = []

        for C, D in queries:
            result.append(dfs(C, D, set()))

        return result



