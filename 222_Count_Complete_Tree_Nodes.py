# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth, right_depth = 1, 1
        left, right = root, root

        while left.left:
            left_depth += 1
            left = left.left
        while right.right:
            right_depth += 1
            right = right.right

        if left_depth == right_depth:
            return pow(2, left_depth) - 1

        return self.countNodes(root.left) + self.countNodes(root.right) + 1

