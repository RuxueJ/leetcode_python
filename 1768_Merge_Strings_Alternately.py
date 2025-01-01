class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        i = 0
        len_1 = len(word1)
        len_2 = len(word2)
        merge = []

        while i < len_1 and i < len_2:
            merge.append(word1[i])
            merge.append(word2[i])
            i += 1

        if i == len_1:
            merge.extend(word2[i:])
        else:
            merge.extend(word1[i:])

        return ''.join(merge)

