class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(temperatures)

        stack = []

        for i, temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                prev_temperature = stack.pop()[1]
                answer[prev_temperature] = i - prev_temperature
            stack.append((temperature, i))

        return answer
