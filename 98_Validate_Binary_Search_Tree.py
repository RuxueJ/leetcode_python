# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.prev = float('-inf')
        self.result = True

        def dfs(node):

            if not node or self.result == False:
                return

            dfs(node.left)

            if node.val <= self.prev:
                self.result = False
            else:
                self.prev = node.val

            dfs(node.right)

        dfs(root)

        return self.result
