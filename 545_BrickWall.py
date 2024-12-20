from collections import defaultdict


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        n = len(wall)
        my_dic = defaultdict(int)
        for rows in wall:
            base = 0
            for i in range(len(rows) - 1):
                base += rows[i]
                my_dic[base] += 1

        if not my_dic:
            return len(wall)

        return n - max(my_dic.values())


