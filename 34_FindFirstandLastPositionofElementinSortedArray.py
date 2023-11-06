class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(nums) - 1
        while (i <= j and nums[i] != target and nums[j] != target):
            middle = (i + j) / 2
            if (nums[middle] > target):
                j = middle - 1
            elif (nums[middle] < target):
                i = middle + 1
            else:
                i += 1
                j -= 1

        if (i > j):
            return [-1, -1]

        if nums[i] == target:
            while (nums[j] != target):
                j -= 1
        if nums[j] == target:
            while (nums[i] != target):
                i += 1

        return [i, j]


