class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        index = 0
        n = len(pushed)
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[index]:
                index += 1
                stack.pop()

        return not stack


