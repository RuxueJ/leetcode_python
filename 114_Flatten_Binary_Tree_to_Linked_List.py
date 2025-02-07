# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def helper(node):
            if not node:
                return None

            left = node.left
            right = node.right

            if left:
                node.right = left
                node.left = None

                pointer = node.right

                while pointer.right:
                    pointer = pointer.right

                pointer.right = right

            helper(node.right)

        helper(root)
