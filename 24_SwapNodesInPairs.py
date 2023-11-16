# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # empty or one element
        if (head == None or head.next == None):
            return head

        # at least two elements
        else:
            dummyHead = ListNode(head)
            pre = dummyHead
            cur = head
            while (cur and cur.next):
                temp = cur.next

                pre.next = cur.next
                cur.next = temp.next
                temp.next = cur

                pre = cur
                cur = cur.next

        return dummyHead.next


