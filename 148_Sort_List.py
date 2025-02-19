# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        slow, fast = head, head.next

        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next

        mid, slow.next = slow.next, None

        l1 = self.sortList(head)
        l2 = self.sortList(mid)

        return self.merge(l1, l2)

    def merge(self, l1, l2):

        dummy = tail = ListNode(0)

        while l1 and l2:
            if l1.val > l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next

            tail = tail.next

        if not l1:
            tail.next = l2
        else:
            tail.next = l1

        return dummy.next


