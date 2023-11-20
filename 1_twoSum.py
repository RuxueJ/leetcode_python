class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dic = {}

        for i in range(len(nums)):
            if not (target - nums[i]) in my_dic:
                my_dic[nums[i]] = i
            else:
                return [my_dic[target - nums[i]], i]


