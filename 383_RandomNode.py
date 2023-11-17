class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        my_dic = {}
        for char in magazine:
            my_dic[char] = my_dic.get(char, 0) + 1

        for char in ransomNote:
            if (not (char in my_dic)):
                return False
            else:
                my_dic[char] -= 1
                if (my_dic[char] == 0):
                    del my_dic[char]

        return True
