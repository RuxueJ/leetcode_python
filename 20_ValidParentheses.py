class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        data = list(s)
        stack = []
        for parenthese in data:
            if (parenthese == '(' or parenthese == '[' or parenthese == '{'):
                stack.append(parenthese)
            elif len(stack) == 0:
                return False
            elif parenthese == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif parenthese == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

