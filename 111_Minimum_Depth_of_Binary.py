# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # if not root:
        #     return 0
        # if not root.right:
        #     return 1 + self.minDepth(root.left)
        # if not root.left:
        #     return 1 + self.minDepth(root.right)
        # return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

        if not root:
            return 0

        my_queue = deque([(root, 1)])

        while my_queue:
            node, depth = my_queue.popleft()
            if (not node.left) and (not node.right):
                return depth
            if node.left:
                my_queue.append((node.left, depth + 1))
            if node.right:
                my_queue.append((node.right, depth + 1))

