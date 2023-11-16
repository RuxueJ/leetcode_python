# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if head == None:
        #     return None
        # else:
        #     current = head
        #     pre = None
        #     temp = head.next
        #     while temp != None:
        #         current.next = pre
        #         pre = current
        #         current = temp
        #         temp = temp.next
        #     current.next = pre
        #     head = current
        # return head

        pre = None
        current = head

        while (current):
            temp = current.next
            current.next = pre
            pre = current
            current = temp
        return pre
