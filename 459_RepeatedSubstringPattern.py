class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        # i is the index of element of the repeated pattern, and the size of the pattern
        i = 1
        while (i <= length / 2):
            if s[i] != s[0]:
                i += 1
            elif length % i != 0:
                i += 1
            else:
                chunk_size = length // i
                for j in range(chunk_size):
                    if s[j * i:(j + 1) * i] != s[0:i]:
                        i += 1
                        break
                    if j == chunk_size - 1:
                        return True
        return False







