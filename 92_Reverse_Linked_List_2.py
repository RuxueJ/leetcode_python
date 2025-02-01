# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        dummy_head = ListNode()

        dummy_head.next = head

        first_node = dummy_head

        for i in range(left - 1):
            first_node = first_node.next

        second_node = first_node.next

        pre, cur, next_node = None, second_node, None

        for i in range(right - left + 1):
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node

        third_node = pre
        fourth_node = cur

        first_node.next = third_node
        second_node.next = fourth_node

        return dummy_head.next

