# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        pointer1, pointer2 = l1, l2

        carry = 0

        dummy_head = ListNode()
        cur = dummy_head

        while pointer1 or pointer2 or carry:
            number1 = pointer1.val if pointer1 else 0
            number2 = pointer2.val if pointer2 else 0

            newNumber = (number1 + number2 + carry) % 10
            carry = (number1 + number2 + carry) / 10

            newNode = ListNode(newNumber)
            cur.next = newNode
            cur = newNode

            pointer1 = pointer1.next if pointer1 else None
            pointer2 = pointer2.next if pointer2 else None

        return dummy_head.next






