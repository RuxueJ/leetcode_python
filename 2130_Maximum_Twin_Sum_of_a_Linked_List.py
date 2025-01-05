class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        # find the mid node in the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the right half part of the linked list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # iterate through the first and second half of the linked list
        max_sum = float('-inf')
        first = head
        second = prev
        while first:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next
        return max_sum
