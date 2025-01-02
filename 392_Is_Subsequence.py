class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        for j in range(len(t)):
            if i < len(s) and s[i] == t[j]:
                i += 1
        return i == len(s)


