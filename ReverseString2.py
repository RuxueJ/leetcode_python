'''
in python string is immutable
we cannot modify the string once it has been created
we need to convert it to list, modify,and convert back to string
res = list(s)
return ''.join(res)
'''
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        def reserveSession(strr):
            left, right = 0, len(strr) - 1
            while left < right:
                strr[left], strr[right] = strr[right], strr[left]
                left += 1
                right -= 1

            return strr

        res = list(s)
        for i in range(0, len(s), 2 * k):
            res[i:i + k] = reserveSession(res[i:i + k])
        return ''.join(res)






