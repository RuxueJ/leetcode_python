# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy_head = ListNode()
        dummy_head.next = head

        slow, fast = dummy_head, dummy_head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        if slow.next:
            slow.next = slow.next.next

        return dummy_head.next

