# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        my_queue = deque([root])
        result = []
        while my_queue:
            current_size = len(my_queue)
            max_num = float('-inf')
            for _ in range(current_size):
                current_node = my_queue.popleft()
                if current_node.val > max_num:
                    max_num = current_node.val
                if current_node.left:
                    my_queue.append(current_node.left)
                if current_node.right:
                    my_queue.append(current_node.right)
            result.append(max_num)

        return result

