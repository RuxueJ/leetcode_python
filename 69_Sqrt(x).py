

# O(sqrt(n))
# def mySqrt(self, x):
#     """
#     :type x: int
#     :rtype: int
#     """
#     i = 0
#     while (i * i <= x):
#         i += 1
#     return i - 1

# O(log(n))
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0
        j = x
        while (i <= j):
            middle = (i + j) / 2
            if (middle * middle > x):
                j = middle - 1
            elif (middle * middle < x):
                i = middle + 1
            else:
                return middle
        return j
