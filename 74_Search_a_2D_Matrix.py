from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix:
            return False

        row, col = len(matrix), len(matrix[0])

        i, j = 0, row * col - 1

        while i <= j:
            mid = i + (j - i) // 2

            new_i = mid // col
            new_j = mid % col

            if matrix[new_i][new_j] == target:
                return True
            elif matrix[new_i][new_j] > target:
                j = mid - 1
            else:
                i = mid + 1

        return False

