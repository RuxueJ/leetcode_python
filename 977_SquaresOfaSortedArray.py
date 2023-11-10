# two pointer
# while loop and for loop
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # find the smallest absolute value
        result = [0] * len(nums)
        i = 0;
        j = len(nums) - 1;
        while (i <= j):
            for index in range(len(nums) - 1, -1, -1):
                if (abs(nums[i]) >= abs(nums[j])):
                    result[index] = nums[i] * nums[i];
                    i += 1;
                else:
                    result[index] = nums[j] * nums[j];
                    j -= 1;
        return result;




