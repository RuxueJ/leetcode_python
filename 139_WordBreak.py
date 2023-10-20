class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # if not s:
        #     return True
        # for i in range(len(s)):
        #     if s[0:i+1] in wordDict:
        #         if self.wordBreak(s[i+1:],wordDict):
        #             return True
        # return False
        length = len(s)
        dp = [False] * (length + 1)

        dp[length] = True
        for i in range(length, -1, -1):
            for j in range(i, length):
                if s[i:j + 1] in wordDict and dp[j + 1]:
                    dp[i] = True
                    break

        return dp[0]
