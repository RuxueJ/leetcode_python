class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flower = n
        length = len(flowerbed)

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (
                    i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                # Plant a flower
                flowerbed[i] = 1
                n -= 1
                # If we've placed all required flowers, return True
                if n == 0:
                    return True
            # if i == 0 and i + 1 < length and flowerbed[i] == 0 and flowerbed[i+1] == 0:
            #     flowerbed[i] = 1
            #     flower -= 1
            # elif i == len(flowerbed)-1 and i - 1 < length and flowerbed[i] == 0 and flowerbed[i-1] == 0:
            #     flowerbed[i] = 1
            #     flower -= 1
            # elif flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
            #     flowerbed[i] = 1
            #     flower -= 1
            # if flower == 0:
            #     return True

        return flower == 0




