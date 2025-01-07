# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        my_queue = deque([root])
        level = 0
        max_sum = float('-inf')
        max_level = 1

        while my_queue:
            level_sum = 0
            level += 1
            size = len(my_queue)
            for i in range(size):
                cur = my_queue.popleft()
                level_sum += cur.val
                if cur.left:
                    my_queue.append(cur.left)
                if cur.right:
                    my_queue.append(cur.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

        return max_level

