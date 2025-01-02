class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        zero_count = 0
        max_length = 0

        for j in range(len(nums)):
            if nums[j] == 0:
                zero_count += 1
                if zero_count > 1:
                    while nums[i] == 1:
                        i += 1
                    i += 1
                    zero_count -= 1
            max_length = max(max_length, j - i)

        return max_length

        # i = 0
        # hasZero = False
        # max_count = 0

        # for j in range(len(nums)):
        #     if nums[j] == 0 and not hasZero:
        #         hasZero = True

        #     elif nums[j] == 0 and hasZero:
        #         while nums[i] == 1:
        #             i += 1
        #         i += 1

        #     max_count = max(max_count, j - i)
        # return max_count





