class Solution(object):

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        N = 5

        while (1):
            if n < N:
                break
            res += n // N
            N *= 5
        return res

