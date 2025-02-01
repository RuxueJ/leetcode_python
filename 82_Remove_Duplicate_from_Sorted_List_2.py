# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        dummy_head = ListNode()
        dummy_head.next = head

        pre, cur, temp = dummy_head, head, head.next

        while temp:
            if temp.val != cur.val:
                pre = cur
                cur = temp
                temp = temp.next


            else:
                while temp and temp.val == cur.val:
                    temp = temp.next

                pre.next = temp
                cur = temp
                if temp:
                    temp = temp.next

        return dummy_head.next



