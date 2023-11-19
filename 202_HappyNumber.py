class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # record = set()
        # while n != 1:
        #     sum = 0
        #     m = n
        #     while (n):
        #         a = n % 10
        #         sum += a * a
        #         n /= 10
        #     if sum in record:
        #         return False
        #     else:
        #         record.add(sum)
        #         n = sum
        # return True


        record = set()
        while True:
            n = self.getSum(n)
            if n == 1:
                return True
            else:
                if n in record:
                    return False
                else:
                    record.add(n)

    def getSum(self, n):
        sum = 0
        while (n):
            n, r = divmod(n, 10)
            sum += r * r
        return sum



