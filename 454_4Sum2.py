from collections import defaultdict
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        # my_dic1 = {}
        # my_dic2 = {}

        # result = 0

        # for num1 in nums1:
        #     for num2 in nums2:
        #         sum1 = num1 + num2
        #         my_dic1[sum1] = my_dic1.get(sum1, 0) + 1
        # for num3 in nums3:
        #     for num4 in nums4:
        #         sum2 = num3 + num4
        #         my_dic2[sum2] = my_dic2.get(sum2, 0) + 1

        # for key in my_dic1:
        #     if (0-key) in my_dic2:
        #         result += my_dic1.get(key)*my_dic2.get(-key)
        # return result

        my_dict = defaultdict(lambda: 0)
        result = 0
        for num1 in nums1:
            for num2 in nums2:
                my_dict[num1 + num2] += 1
        for num3 in nums3:
            for num4 in nums4:
                result += my_dict[-num3 - num4]
        return result






