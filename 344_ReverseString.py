# // is integer operation
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # i = 0
        # j = len(s)-1
        # while i < j:
        #     temp = s[i]
        #     s[i] = s[j]
        #     s[j] = temp
        #     i += 1
        #     j -= 1

        n = len(s)
        for i in range(n//2):
            # temp = s[i]
            # s[i] = s[n-i-1]
            # s[n-i-1] = temp
            s[i], s[n-i-1] = s[n-i-1],s[i]