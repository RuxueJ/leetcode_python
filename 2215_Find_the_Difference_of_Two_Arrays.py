class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set_1 = set(nums1)
        set_2 = set(nums2)

        ans_1 = list(set_1 - set_2)
        ans_2 = list(set_2 - set_1)

        return [ans_1, ans_2]
