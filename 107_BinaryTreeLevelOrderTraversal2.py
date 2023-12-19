# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # if not root:
        #     return []
        levels = []
        self.helper(root, 0, levels)
        i = 0
        j = len(levels) - 1
        while i <= j:
            k = levels[i]
            levels[i] = levels[j]
            levels[j] = k
            i += 1
            j -= 1
        return levels

    def helper(self, node, level, levels):
        if not node:
            return
        if len(levels) == level:
            levels.append([])

        levels[level].append(node.val)
        self.helper(node.left, level + 1, levels)
        self.helper(node.right, level + 1, levels)


