# dictionary API
# edge condition
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        if len(nums) == 1:
            return nums[0]

        for num in nums:
            if num in dic:
                if dic[num] >= (len(nums) / 2):
                    return num
                else:
                    dic[num] += 1
            else:
                dic[num] = 1


