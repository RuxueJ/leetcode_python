class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        current_sum = 0

        for i in range(k):
            current_sum += nums[i]

        max_sum = current_sum

        for i in range(k, len(nums)):
            current_sum = current_sum + nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)

        return max_sum / k
