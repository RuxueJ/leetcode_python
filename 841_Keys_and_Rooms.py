class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set([0])

        def dfs(key):
            for room in rooms[key]:
                if room not in visited:
                    visited.add(room)
                    dfs(room)

        dfs(0)
        return len(rooms) == len(visited)
