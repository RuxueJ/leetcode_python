class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_amount = 0

        i, j = 0, len(height) - 1

        while i < j:
            current_amount = min(height[i], height[j]) * (j - i)
            max_amount = max(max_amount, current_amount)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return max_amount



