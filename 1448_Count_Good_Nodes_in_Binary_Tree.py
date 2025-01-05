# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node, max_so_far):
            if not node:
                return 0
            if node.val >= max_so_far:
                max_so_far = node.val
                return 1 + dfs(node.left, max_so_far) + dfs(node.right, max_so_far)

            else:
                return dfs(node.left, max_so_far) + dfs(node.right, max_so_far)

        count = dfs(root, float('-inf'))
        return count

