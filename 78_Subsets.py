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

    result = []

        # def backtrack(start, path):
        #     result.append(path[:])  # Add the current subset (copy to avoid mutation)
        #     for i in range(start, len(nums)):
        #         path.append(nums[i])  # Include nums[i]
        #         backtrack(i + 1, path)  # Recurse with next element
        #         path.pop()  # Exclude nums[i] (backtrack)
        #
        # backtrack(0, [])
        # return result

