# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        small, big = min(p.val, q.val), max(p.val, q.val)

        def helper(node, small, big):

            if not node:
                return None

            if node.val == small or node.val == big or (node.val > small and node.val < big):
                return node

            if node.val < small:
                return helper(node.right, small, big)
            else:
                return helper(node.left, small, big)

        return helper(root, small, big)

