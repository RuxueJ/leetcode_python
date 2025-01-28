class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            n = -n
            x = 1 / x

        result = 1

        while n > 0:
            if n % 2 == 1:
                result *= x
                n -= 1
            else:
                x *= x
                n //= 2
        return result

