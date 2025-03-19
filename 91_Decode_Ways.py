class Solution:
    def numDecodings(self, s: str) -> int:

        # each result[i] value only depends on result[i+1] and result[i+2]

        cur, prev = 1, 1
        n = len(s)
        for i in range(n-1,-1,-1):
            if s[i] == "0":
                cur, prev = 0, cur
            else:
                temp = cur
                if 10 <= int(s[i:i+2]) <= 26:
                    cur += prev
                prev = temp
        return cur
