from collections import deque


class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        radiant_queue = deque()
        dire_queue = deque()

        for i in range(len(senate)):
            if senate[i] == 'R':
                radiant_queue.append(i)
            else:
                dire_queue.append(i)

        n = len(senate)

        while radiant_queue and dire_queue:
            if radiant_queue[0] > dire_queue[0]:
                radiant_queue.popleft()
                dire_queue.append(dire_queue.popleft() + n)
            else:
                dire_queue.popleft()
                radiant_queue.append(radiant_queue.popleft() + n)

        if radiant_queue:
            return "Radiant"
        else:
            return "Dire"


