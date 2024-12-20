class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        left, right = 0, 0
        record = set()
        max_length = 0
        while right < len(s):
            if s[right] not in record:
                record.add(s[right])
                right += 1
                current_length = right - left
                max_length = max(max_length, current_length)
            else:
                while s[left] != s[right]:
                    record.remove(s[left])
                    left += 1
                record.remove(s[left])
                left += 1
        return max_length


