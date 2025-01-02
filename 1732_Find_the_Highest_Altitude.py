class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        height = 0
        max_height = 0

        for altitude in gain:
            height += altitude
            max_height = max(max_height, height)
        return max_height
