class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        map = [0] * (n+1)
        map[1] = 1
        if n > 1:
            map[2] = 2
            for i in range(3,n+1):
                map[i] = map[i-1] + map[i-2]
            return map[n]
        else:
            return map[1]

