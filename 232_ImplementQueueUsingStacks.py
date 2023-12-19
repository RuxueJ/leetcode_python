class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        while (len(self.stack1) != 0):
            self.stack2.append(self.stack1.pop())
        pop_value = self.stack2.pop()
        while (len(self.stack2) != 0):
            self.stack1.append(self.stack2.pop())
        return pop_value

    def peek(self):
        """
        :rtype: int
        """
        while (len(self.stack1) != 0):
            self.stack2.append(self.stack1.pop())
        peek_value = self.stack2[len(self.stack2) - 1]
        while (len(self.stack2) != 0):
            self.stack1.append(self.stack2.pop())
        return peek_value

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack1) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()