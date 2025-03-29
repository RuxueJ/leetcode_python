from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []
        path = []

        def backtracking(startIndex):

            result.append(path[:])

            for i in range(startIndex, len(nums)):
                if i > startIndex and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                backtracking(i + 1)
                path.pop()

        backtracking(0)
        return result


