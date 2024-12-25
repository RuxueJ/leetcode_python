# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        my_dic = defaultdict(int)

        def postTraverse(root):
            if not root:
                return 0
            left_sum = postTraverse(root.left)
            right_sum = postTraverse(root.right)
            current_sum = left_sum + right_sum + root.val
            my_dic[current_sum] += 1
            return current_sum

        if not root:
            return []

        postTraverse(root)

        max_value = max(my_dic.values())

        return [k for k, v in my_dic.items() if v == max_value]

