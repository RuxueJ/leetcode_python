class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def backtracking(current, open_number, close_number):
            if len(current) == 2 * n:
                result.append(current)
                return

            if open_number < n:
                backtracking(current + '(', open_number + 1, close_number)

            if close_number < open_number:
                backtracking(current + ')', open_number, close_number + 1)

        backtracking("", 0, 0)

        return result



