class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        all_sum = sum(nums)
        for i in range(len(nums)):
            if left * 2 + nums[i] == all_sum:
                return i
            left += nums[i]
        return -1
