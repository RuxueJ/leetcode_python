# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def inorder(node):
            if node:
                inorder(node.left)
                process(node)
                inorder(node.right)

        def process(node):
            if node.val == self.current_val:
                self.current_count += 1
            else:
                self.current_val = node.val
                self.current_count = 1

            if self.current_count > self.max_count:
                self.max_count = self.current_count
                self.modes = [node.val]
            elif self.current_count == self.max_count:
                self.modes.append(node.val)

        self.current_count = 0
        self.current_val = None
        self.modes = []
        self.max_count = 0

        inorder(root)

        return self.modes
