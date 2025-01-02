class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i, j = 0, len(nums) - 1
        count = 0

        while i < j:
            current = nums[i] + nums[j]
            if current == k:
                count += 1
                i += 1
                j -= 1
            elif current > k:
                j -= 1
            else:
                i += 1

        return count
