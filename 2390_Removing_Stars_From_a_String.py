class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for char in s:
            if char != '*':
                stack.append(char)
            elif stack:
                stack.pop()

        return ''.join(stack)
