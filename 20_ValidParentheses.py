class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        open_bracket = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in open_bracket:
                stack.append(char)
            else:
                if not stack or char != open_bracket[stack[-1]]:
                    return False

                stack.pop()

        return not stack

# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         data = list(s)
#         stack = []
#         for parenthese in data:
#             if (parenthese == '(' or parenthese == '[' or parenthese == '{'):
#                 stack.append(parenthese)
#             elif len(stack) == 0:
#                 return False
#             elif parenthese == ')':
#                 if stack[-1] == '(':
#                     stack.pop()
#                 else:
#                     return False
#             elif parenthese == ']':
#                 if stack[-1] == '[':
#                     stack.pop()
#                 else:
#                     return False
#             else:
#                 if stack[-1] == '{':
#                     stack.pop()
#                 else:
#                     return False
#         if len(stack) == 0:
#             return True
#         else:
#             return False
#
