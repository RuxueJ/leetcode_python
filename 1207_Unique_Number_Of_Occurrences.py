from collections import defaultdict


class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        my_dic = defaultdict(int)

        for num in arr:
            my_dic[num] += 1

        my_set = set(my_dic.values())

        return len(my_set) == len(my_dic)

