class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        data = list(s)
        stack = []
        for letter in data:
            if (len(stack) == 0):
                stack.append(letter)
            elif letter == stack[-1]:
                stack.pop()
            else:
                stack.append(letter)
        return ''.join(stack)
