# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Find min node in right subtree
            min_node = root.right
            while min_node.left:
                min_node = min_node.left

            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)

        return root
        # def helper(node, key):
        #     if not node:
        #         return None
        #     if node.val < key:
        #         node.right = helper(node.right, key)
        #     elif node.val > key:
        #         node.left = helper(node.left, key)

        #     else:
        #         # node to be deleted found
        #         # case 1: node is leaf
        #         if not node.left and not node.right:
        #             return None

        #         # case 2: node has one child
        #         elif not node.left:
        #             return node.right
        #         elif not node.right:
        #             return node.left

        #         # case 3: node has 2 children
        #         else:
        #             # find the smallest node in the right tree
        #             min_node = node.right
        #             while min_node.left:
        #                 min_node = min_node.left
        #             node.val = min_node.val
        #             node.right = helper(node.right, min_node.val)
        #     return node

        # return helper(root, key)




