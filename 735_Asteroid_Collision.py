class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(asteroid) > abs(stack[-1]):
                    stack.pop()
                    continue
                elif abs(asteroid) == abs(stack[-1]):
                    stack.pop()
                break
            else:
                stack.append(asteroid)

        return stack





