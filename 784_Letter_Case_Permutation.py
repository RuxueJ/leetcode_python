class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        result = []
        path = []

        def backtracking(i):
            if i == n:
                result.append(''.join(path))
                return
            if s[i].isdigit():
                path.append(s[i])
                backtracking(i + 1)
                path.pop()
                return
            else:
                path.append(s[i].lower())
                backtracking(i + 1)
                path.pop()
                path.append(s[i].upper())
                backtracking(i + 1)
                path.pop()

        backtracking(0)
        return result


