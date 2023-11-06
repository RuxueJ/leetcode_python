class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums)-1
        while(i<=j):
            middle = (i+j)/2
            if nums[middle] == target:
                return middle
            elif nums[(i+j)/2] > target:
                j = middle-1
            else:
                i = middle+1
        return -1
