# when the count of a char is 0, we need to del it
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        my_dic = {}
        for cha in s:
            my_dic[cha] = my_dic.get(cha, 0) + 1
        for char in t:
            if (not (char in my_dic)):
                return False
            else:
                my_dic[char] -= 1
                if (my_dic[char] == 0):
                    del my_dic[char]

        if (len(my_dic) == 0):
            return True
        else:
            return False
