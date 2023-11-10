# inner function, stack, string is immutable
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        def processing(input_str):
            result = []
            for char in input_str:
                if char != '#':
                    result.append(char)
                else:
                    if (result != []):
                        result.pop()
            return ''.join(result)

        return processing(s) == processing(t)

