from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        record = defaultdict(list)

        for words in strs:
            sorted_words = sorted(words)
            record[''.join(sorted_words)].append(words)
        return record.values()

