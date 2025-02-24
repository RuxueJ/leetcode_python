from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        current_max_sum = 0
        current_min_sum = 0
        total_sum = 0
        max_sum = max(nums)
        min_sum = min(nums)

        for num in nums:
            total_sum += num

            current_max_sum = max(current_max_sum + num, num)
            max_sum = max(max_sum, current_max_sum)

            current_min_sum = min(current_min_sum + num, num)
            min_sum = min(min_sum, current_min_sum)

        if max_sum < 0:
            return max_sum

        return max(max_sum, total_sum - min_sum)




