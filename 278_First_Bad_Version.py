# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 1, n
        while i <= j:
            mid = (i + j) // 2
            if isBadVersion(mid):
                j = mid - 1
            else:
                i = mid + 1
        return i
