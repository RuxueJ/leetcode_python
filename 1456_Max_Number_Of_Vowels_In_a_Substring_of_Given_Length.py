class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        my_set = set("aeiou")
        count = 0

        for i in range(k):
            if s[i] in my_set:
                count += 1
        max_count = count

        for i in range(k, len(s)):
            if s[i] in my_set:
                count += 1
            if s[i - k] in my_set:
                count -= 1
            max_count = max(max_count, count)

        return max_count

