from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first, last = strs[0], strs[-1]

        result = []

        for i in range(len(first)):
            if first[i] != last[i]:
                break
            else:
                result.append(first[i])

        return ''.join(result)

        # target = strs[0]

        # result = []
        # end = False

        # for i in range(len(target)):

        #     char = target[i]

        #     for word in strs:
        #         if i > len(word)-1 or word[i] != char:
        #             end = True
        #             break
        #     else:
        #         result.append(word[i])

        #     if end:
        #         break

        # return ''.join(result)

