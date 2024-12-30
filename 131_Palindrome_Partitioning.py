class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)

        result = []
        path = []

        def isPalindrome(s):
            return s == s[::-1]

        def backtracking(i):
            if i >= n:
                result.append(path[:])

            for j in range(i, n):
                if isPalindrome(s[i:j + 1]):
                    path.append(s[i:j + 1])
                    backtracking(j + 1)
                    path.pop()

        backtracking(0)
        return result



