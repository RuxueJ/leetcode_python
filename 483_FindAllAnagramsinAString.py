class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        # sort method
        # length = len(p)
        # sorted_target = sorted(p)
        # for i in range(len(s) - length + 1):
        #     if(sorted(s[i:i+length]) == sorted_target):
        #         result.append(i)
        # return result

        # my_dict = {}
        # length = len(p)
        # start = 0
        # for char in p:
        #     my_dict[char] = my_dict.get(char,0) + 1

        # while start < len(s)-length+1:
        #     if(s[start] in my_dict):
        #         test = my_dict.copy()
        #         for end in range(length):
        #             if (not s[start+end] in test):
        #                 # start = start + end -1
        #                 break
        #             else:
        #                 test[s[start+end]] -= 1
        #                 if test[s[start+end]] == 0:
        #                     del test[s[start+end]]
        #         if not test:
        #             result.append(start)

        #     start += 1

        # return result

        record = [0] * 26
        window = [0] * 26
        lenS = len(s)
        lenP = len(p)
        result = []
        if lenS < lenP:
            return None
        else:
            for i in range(lenP):
                record[ord(p[i]) - ord('a')] += 1
                window[ord(s[i]) - ord('a')] += 1
            if record == window:
                result.append(0)

            # i is the index to be removed from the window
            for i in range(0, lenS - lenP):
                window[ord(s[i]) - ord('a')] -= 1
                window[ord(s[i + lenP]) - ord('a')] += 1
                if window == record:
                    result.append(i + 1)
            return result







