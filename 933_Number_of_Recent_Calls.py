class RecentCounter(object):

    def __init__(self):
        self.deque = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.deque.append(t)
        while self.deque and self.deque[0] < t - 3000:
            self.deque.popleft()
        return len(self.deque)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)