# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        pointer_1 = list1
        pointer_2 = list2
        dummy_head = ListNode()
        cur = dummy_head

        while pointer_1 and pointer_2:
            if pointer_1.val <= pointer_2.val:
                cur.next = pointer_1
                pointer_1 = pointer_1.next
            else:
                cur.next = pointer_2
                pointer_2 = pointer_2.next
            cur = cur.next

        cur.next = pointer_1 if pointer_1 else pointer_2

        return dummy_head.next


