class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        cols = len(matrix[0])

        returnList = []
        startX = 0
        startY = 0
        offset = 1

        n = min(rows, cols)
        loop = n // 2

        while (loop):
            for j in range(startY, cols - offset):
                returnList.append(matrix[startX][j])
            for i in range(startX, rows - offset):
                returnList.append(matrix[i][cols - offset])
            for j in range(cols - offset, startY, -1):
                returnList.append(matrix[rows - offset][j])
            for i in range(rows - offset, startX, -1):
                returnList.append(matrix[i][startY])
            startX += 1
            startY += 1
            loop -= 1
            offset += 1
        if n % 2 == 1:
            if rows < cols:
                for j in range(startY, cols - offset + 1):
                    returnList.append(matrix[startX][j])
            elif rows > cols:
                for i in range(startX, rows - offset + 1):
                    returnList.append(matrix[i][startY])
            else:
                returnList.append(matrix[startX][startY])
        return returnList
