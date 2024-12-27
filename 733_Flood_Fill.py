from collections import deque


class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        original_color = image[sr][sc]
        m, n = len(image), len(image[0])
        visited = set([(sr, sc)])
        image[sr][sc] = color

        queue = deque([(sr, sc)])

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited and image[new_x][
                    new_y] == original_color:
                    image[new_x][new_y] = color
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y))
        return image



