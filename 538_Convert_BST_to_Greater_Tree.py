# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        right, root, left
        pass the sum of the previous node to the next node
        '''

        def traverse(node, previous_sum):
            if not node:
                return previous_sum

            previous_sum = traverse(node.right, previous_sum)

            node.val += previous_sum

            return traverse(node.left, node.val)

        traverse(root, 0)

        return root

