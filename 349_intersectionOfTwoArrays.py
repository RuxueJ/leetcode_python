# set: unique unordered collection of data
# list:  ordered collection of data(mutable: can be added removed or modified)
# tuple:  ordered collection of data(immutable)




class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # my_dic = {}
        # result = []
        # for num in nums1:
        #     if (not num in my_dic):
        #         my_dic[num] = 0
        # for num in nums2:
        #     if (num in my_dic):
        #         result.append(num)
        #         del my_dic[num]
        # return result
        return list(set(nums1) & set(nums2))

