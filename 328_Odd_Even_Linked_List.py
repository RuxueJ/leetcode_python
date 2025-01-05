# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head

        if odd_head.next and odd_head.next.next:
            odd_head.next = odd_head.next.next
            odd_head = odd_head.next

        if even_head.next and even_head.next.next:
            even_head.next = even_head.next.next
            even_head = even_head.next



