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
        less = ListNode()
        greater = ListNode()
        less_pointer = less
        greater_pointer = greater

        cur_pointer = head
        while cur_pointer:
            if cur_pointer.val < x:
                less_pointer.next = cur_pointer
                less_pointer = cur_pointer
            else:
                greater_pointer.next = cur_pointer
                greater_pointer = cur_pointer
            cur_pointer = cur_pointer.next

        greater_pointer.next = None
        less_pointer.next = greater.next
        return less.next

