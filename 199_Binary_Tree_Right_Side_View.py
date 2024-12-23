# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        my_queue = deque([root])
        result = []
        while my_queue:
            cur_size = len(my_queue)
            for i in range(cur_size):
                cur_node = my_queue.popleft()
                if i == cur_size - 1:
                    result.append(cur_node.val)
                if cur_node.left:
                    my_queue.append(cur_node.left)
                if cur_node.right:
                    my_queue.append(cur_node.right)

        return result

