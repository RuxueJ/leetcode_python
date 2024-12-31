class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if not matrix:
            return None

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        result = []

        while top <= bottom and left <= right:

            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result

# class Solution(object):
#     def spiralOrder(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[int]
#         """
#         rows = len(matrix)
#         cols = len(matrix[0])
#
#         returnList = []
#         startX = 0
#         startY = 0
#         offset = 1
#
#         n = min(rows, cols)
#         loop = n // 2
#
#         while (loop):
#             for j in range(startY, cols - offset):
#                 returnList.append(matrix[startX][j])
#             for i in range(startX, rows - offset):
#                 returnList.append(matrix[i][cols - offset])
#             for j in range(cols - offset, startY, -1):
#                 returnList.append(matrix[rows - offset][j])
#             for i in range(rows - offset, startX, -1):
#                 returnList.append(matrix[i][startY])
#             startX += 1
#             startY += 1
#             loop -= 1
#             offset += 1
#         if n % 2 == 1:
#             if rows < cols:
#                 for j in range(startY, cols - offset + 1):
#                     returnList.append(matrix[startX][j])
#             elif rows > cols:
#                 for i in range(startX, rows - offset + 1):
#                     returnList.append(matrix[i][startY])
#             else:
#                 returnList.append(matrix[startX][startY])
#         return returnList
