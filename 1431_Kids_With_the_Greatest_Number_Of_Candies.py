class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candy = max(candies)
        result = []
        for candy in candies:
            if max_candy - candy > extraCandies:
                result.append(False)
            else:
                result.append(True)
        return result
