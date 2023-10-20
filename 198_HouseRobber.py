class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # number = len(nums)
        # length = number + 1

        # result = [0] * length
        # result[0] = 0
        # if number == 0:
        #     return 0
        # else:
        #     result [1] = nums[0]

        #     for i in range(2,length):
        #         result[i] = max(result[i-1], result[i-2] + nums[i-1])

        #     return result[-1]

        if len(nums) < 2:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for house in range(2, len(nums)):
            dp[house] = max(dp[house - 1], dp[house - 2] + nums[house])
        return dp[-1]
