

def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    i = 0
    j = len(nums) - 1
    while (i <= j):
        middle = (j + i) / 2
        if (nums[middle] == target):
            return middle
        elif (nums[middle] < target):
            i = middle + 1
        else:
            j = middle - 1

    return i
