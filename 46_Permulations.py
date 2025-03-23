from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        result = []

        def dfs(index):
            if index == n:
                result.append(nums[:])
                return

            for i in range(index, n):
                nums[index], nums[i] = nums[i], nums[index]
                dfs(index + 1)
                nums[index], nums[i] = nums[i], nums[index]

        dfs(0)

        return result

        # n = len(nums)
        # path = []
        # result = []

        # def dfs():
        #     if len(path) == n:
        #         result.append(path[:])
        #         return

        #     for num in nums:
        #         if num not in path:
        #             path.append(num)
        #             dfs()
        #             path.pop()

        # dfs()

        # return result

