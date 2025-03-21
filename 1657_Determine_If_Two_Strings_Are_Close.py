from collections import Counter


class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        if set(word1) != set(word2):
            return False

        freq_1 = Counter(word1)
        freq_2 = Counter(word2)

        return sorted(freq_1.values()) == sorted(freq_2.values())
