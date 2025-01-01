class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        slow, fast = 0, 0
        while fast < len(chars):
            current_char = chars[fast]
            current_number = 1
            while fast < len(chars) - 1 and chars[fast + 1] == chars[fast]:
                current_number += 1
                fast += 1
            chars[slow] = chars[fast]
            number = str(current_number)
            if current_number > 1:
                for i in range(len(number)):
                    slow += 1
                    chars[slow] = number[i]
            fast += 1
            slow += 1

        return slow




