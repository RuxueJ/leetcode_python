# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """

        def dfs(node, cumulativeSum):
            if not node:
                return 0

            cumulativeSum += node.val

            path = prefix_sum[cumulativeSum - targetSum]

            prefix_sum[cumulativeSum] += 1

            path += dfs(node.left, cumulativeSum)
            path += dfs(node.right, cumulativeSum)

            prefix_sum[cumulativeSum] -= 1

            return path

        prefix_sum = defaultdict(int)

        prefix_sum[0] = 1

        return dfs(root, 0)

        # def include(node, targetSum):
        #     if not node:
        #         return 0
        #     count = 1 if node.val == targetSum else 0

        #     return count + include(node.left,targetSum - node.val) + include(node.right,targetSum - node.val)

        # def exclude(node,targetSum):
        #     if not node:
        #         return 0
        #     return self.pathSum(node.left, targetSum) + self.pathSum(node.right, targetSum)

        # if not root:
        #     return 0
        # return exclude(root, targetSum) + include(root, targetSum)






