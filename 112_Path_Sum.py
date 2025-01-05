# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right and root.val == targetSum:
            return True

        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

        # if not root:
        #     return False

        # def dfs(node,sum_so_far):
        #     if not node:
        #         return False

        #     if not node.left and not node.right:
        #         return node.val + sum_so_far == targetSum

        #     sum_so_far += node.val
        #     return dfs(node.left, sum_so_far) or dfs(node.right,sum_so_far)

        # return dfs(root, 0)



