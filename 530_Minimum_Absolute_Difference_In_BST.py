# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def inorder(node):
            if node:
                inorder(node.left)

                process(node)

                inorder(node.right)

        def process(node):
            if self.previous_value:
                self.current_difference = node.val - self.previous_value

                self.min_difference = min(self.min_difference, self.current_difference)

            self.previous_value = node.val

            print(self.current_difference)
            print(self.min_difference)

        self.previous_value = None
        self.min_difference = float('inf')
        self.current_difference = 0

        inorder(root)

        return self.min_difference if self.min_difference != float('inf') else 0
