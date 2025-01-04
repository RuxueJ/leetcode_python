class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        current_number = 0
        current_string = ""
        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == '[':
                stack.append((current_number, current_string))
                current_number = 0
                current_string = ""
            elif char == ']':
                last_number, last_string = stack.pop()
                current_string = last_string + last_number * current_string
            else:
                current_string += char

        return current_string


