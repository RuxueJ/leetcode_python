class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        i = 0
        number_0 = 0
        max_count = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                number_0 += 1
                if number_0 > k:
                    while nums[i] == 1:
                        i += 1
                    i += 1
                    number_0 -= 1

            max_count = max(max_count, j - i + 1)

        return max_count



