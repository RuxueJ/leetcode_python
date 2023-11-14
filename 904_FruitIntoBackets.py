from collections import defaultdict


# dict 
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        basket = defaultdict(int)

        l = 0
        r = 0
        max_fruits = 0
        for r in range(0, len(fruits)):
            basket[fruits[r]] += 1

            while len(basket) > 2:

                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1
            max_fruits = max(max_fruits, r - l + 1)
        return max_fruits
