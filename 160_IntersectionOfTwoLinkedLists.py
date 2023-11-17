# Definition for singly-linked list.
# two pointer fast and slow

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA = headA
        curB = headB
        while (curA.next and curB.next):
            curA = curA.next
            curB = curB.next
        if ((not curA.next) and (not curB.next)):
            curA = headB
            curB = headA
        elif (not curA.next):
            curA = headB
            while (curB.next):
                curA = curA.next
                curB = curB.next
            curB = headA
        else:
            curB = headA
            while (curA.next):
                curA = curA.next
                curB = curB.next
            curA = headB
        while (curA != curB and curA and curB):
            curA = curA.next
            curB = curB.next
        if ((not curA) or (not curB)):
            return None
        else:
            return curA


