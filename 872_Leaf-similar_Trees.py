# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """

        def postTraverse(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]

            return postTraverse(node.left) + postTraverse(node.right)

        leaf1 = postTraverse(root1)
        leaf2 = postTraverse(root2)

        return leaf1 == leaf2
