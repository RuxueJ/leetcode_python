class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        the difference of s.split() and s.split(' ')
        """
        word_list = s.split()
        word_list.reverse()
        return ' '.join(word_list)

# class Solution(object):
#     def reverseWords(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         i, j = 0, len(s) - 1
#
#         while i <= j and s[i] == ' ':
#             i += 1
#         while i <= j and s[j] == ' ':
#             j -= 1
#         s = s[i:j + 1]
#         words = s.split()
#         out = []
#         for k in range(len(words) - 1, -1, -1):
#             out.append(words[k])
#         return ' '.join(out)
#
