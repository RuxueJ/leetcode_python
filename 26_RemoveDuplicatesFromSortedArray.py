# the boundary
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        for i in range(len(nums)-1):
            if(nums[i] != nums[i+1]):
                nums[index] = nums[i]
                index += 1
        c
        index += 1
        return index

