# define class
# or instead of ||
# add dummyHead before the real head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val;
        self.next = next;


class MyLinkedList(object):

    def __init__(self):
        self.dummyHead = ListNode()
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if (index < 0 or index >= self.size):
            return -1
        else:
            current = self.dummyHead.next
            for i in range(index):
                current = current.next
            return current.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        current = ListNode(val, self.dummyHead.next)
        self.dummyHead.next = current
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        current = self.dummyHead
        while (current.next != None):
            current = current.next
        current.next = ListNode(val, None)
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        current = self.dummyHead
        if (index < 0 or index > self.size):
            return None

        for i in range(index):
            current = current.next

        current.next = ListNode(val, current.next)
        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if (index < 0 or index >= self.size):
            return None
        else:
            current = self.dummyHead
            for i in range(index):
                current = current.next
            current.next = current.next.next
            self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)