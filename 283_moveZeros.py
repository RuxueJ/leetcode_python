class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slowIndex = 0
        for fastIndex in range(len(nums)):
            if (nums[fastIndex] != 0):
                nums[slowIndex] = nums[fastIndex]
                slowIndex += 1
        for i in range(slowIndex, fastIndex + 1):
            nums[i] = 0


