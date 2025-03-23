# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(list1, list2):
            dummy_head = ListNode()
            cur = dummy_head

            while list1 and list2:
                if list1.val <= list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next

            cur.next = list1 if list1 else list2

            return dummy_head.next

        # def merge_sort(lists):

        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return merge(left, right)

        # min_heap = []

        # for i in range(len(lists)):

        #     if lists[i]:
        #         heapq.heappush(min_heap,(lists[i].val, i, lists[i]))

        # dummy_head = ListNode()
        # cur = dummy_head

        # while min_heap:
        #     val, index, node = heapq.heappop(min_heap)

        #     cur.next = node

        #     cur = cur.next

        #     if node.next:
        #         heapq.heappush(min_heap, (node.next.val, index, node.next))

        # return dummy_head.next

        # def merge(list1, list2):
        #     dummy_head = ListNode()
        #     cur = dummy_head

        #     pointer1 = list1
        #     pointer2 = list2

        #     while pointer1 and pointer2:
        #         if pointer1.val <= pointer2.val:
        #             cur.next = pointer1
        #             pointer1 = pointer1.next
        #         else:
        #             cur.next = pointer2
        #             pointer2 = pointer2.next
        #         cur = cur.next

        #     if not pointer1:
        #         cur.next = pointer2
        #     if not pointer2:
        #         cur.next = pointer1

        #     return dummy_head.next

        # if not lists:
        #     return None

        # result = lists[0]

        # for i in range(1,len(lists)):
        #     result = merge(result, lists[i])

        # return result



