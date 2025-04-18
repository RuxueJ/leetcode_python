class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        path = []

        if not digits:
            return []

        dictionary = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': 'tuv',
            '9': "wxyz"
        }

        def backtracking(startIndex):
            if startIndex == len(digits):
                result.append(''.join(path))
                return

            characters = dictionary[digits[startIndex]]

            for char in characters:
                path.append(char)
                backtracking(startIndex + 1)
                path.pop()

        backtracking(0)
        return result

# class Solution(object):
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
#         map = {
#         '2':'abc',
#         '3':'def',
#         '4':'ghi',
#         '5':'jkl',
#         '6':'mno',
#         '7':'pqrs',
#         '8':'tuv',
#         '9':'wxyz',
#         }
#
#
#
#         if not digits:
#             return []
#
#
#         combinations = [""]
#         for digit in digits:
#             newCom = []
#             for combination in combinations:
#                 for letter in map[digit]:
#                     newCom.append(combination+letter)
#             combinations = newCom
#
#         return combinations
