# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node, current):
            if not node:
                return 0
            if not node.left and not node.right:
                return current * 10 + node.val

            current = current * 10 + node.val

            return dfs(node.left, current) + dfs(node.right, current)

        return dfs(root, 0)


