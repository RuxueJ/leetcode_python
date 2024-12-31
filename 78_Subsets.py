class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)

        result = []

        path = []

        def backtracking(startIndex):
            if startIndex == n:
                result.append(path[:])
                return

            path.append(nums[startIndex])
            backtracking(startIndex + 1)
            path.pop()

            backtracking(startIndex + 1)

        backtracking(0)

        return result

