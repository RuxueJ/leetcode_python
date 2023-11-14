# how to create a 2D matrix in python [[0] * n for _ in range(n)]


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        startX = 0
        startY = 0
        offset = 1
        count = 1
        loop = n // 2
        mid = n // 2
        result = [[0] * n for _ in range(n)]

        while (loop):
            for j in range(startY, n - offset):
                result[startX][j] = count
                count += 1
            for i in range(startX, n - offset):
                result[i][n - offset] = count
                count += 1
            for j in range(n - offset, startY, -1):
                result[n - offset][j] = count
                count += 1
            for i in range(n - offset, startX, -1):
                result[i][startY] = count
                count += 1
            startX += 1
            startY += 1
            offset += 1

            loop -= 1
        if n % 2 == 1:
            result[mid][mid] = count
        return result

