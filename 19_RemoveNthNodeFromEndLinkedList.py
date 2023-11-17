# Definition for singly-linked list.
# 快慢双指针

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if (head == None):
            return None

        dummyNode = ListNode(0, head)
        first = dummyNode
        slow = dummyNode

        for i in range(n):
            # if(first):
            first = first.next
        # else:
        # return None
        while (first.next):
            first = first.next
            slow = slow.next
        slow.next = slow.next.next

        return dummyNode.next



