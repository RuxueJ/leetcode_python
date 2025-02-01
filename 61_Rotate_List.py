# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]

        1 get the lenth of the linked list
        2 k % = length
        3 slow, fast pointer to locate the new head
        """

        # get the length of the linked list

        dummy_head = ListNode()
        dummy_head.next = head
        cur = dummy_head
        length = 0
        while cur.next:
            length += 1
            cur = cur.next

        if not head or k == 0:
            return head

        # update the new k
        k %= length

        # edge case
        if k == 0:
            return head

        # locate the new head
        slow, fast = dummy_head, dummy_head

        for _ in range(k):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        newHead = slow.next
        fast.next = head
        slow.next = None

        return newHead


