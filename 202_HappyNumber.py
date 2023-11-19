class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        record = set()
        while n != 1:
            sum = 0
            m = n
            while (n):
                a = n % 10
                sum += a * a
                n /= 10
            if sum in record:
                return False
            else:
                record.add(sum)
                n = sum
        return True


