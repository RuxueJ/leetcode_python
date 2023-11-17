# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        count = 0
        while (fast and slow and fast.next):
            fast = fast.next.next
            slow = slow.next
            if (fast == slow):
                slow = head
                while (slow != fast):
                    slow = slow.next
                    fast = fast.next
                    count += 1
                return slow

        return None
