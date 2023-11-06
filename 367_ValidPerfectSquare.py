# True False
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 0
        j = num
        while(i <= j):
            middle = (i+j)/2
            if(middle * middle == num):
                return True
            elif(middle * middle > num):
                j = middle - 1
            else:
                i = middle + 1
        return False


