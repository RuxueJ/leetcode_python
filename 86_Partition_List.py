# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        slow_head = ListNode()
        fast_head = ListNode()

        slow_pointer, fast_pointer = slow_head, fast_head

        cur = head
        while cur:
            if cur.val < x:
                slow_pointer.next = cur
                slow_pointer = cur
            else:
                fast_pointer.next = cur
                fast_pointer = cur
            cur = cur.next

        slow_pointer.next = fast_head.next
        fast_pointer.next = None

        return slow_head.next

