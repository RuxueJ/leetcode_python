# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        visited = {}

        if not head:
            return None

        current = head

        while current:
            visited[current] = Node(current.val)
            current = current.next

        current = head

        while current:
            if current.next:
                visited[current].next = visited[current.next]
            if current.random:
                visited[current].random = visited[current.random]

            current = current.next

        return visited[head]

        # memory limit exceed
        # def dfs(original_node):
        #     if not original_node:
        #         return None

        #     if original_node in visited:
        #         return visited[original_node]

        #     clone = Node(original_node.val)
        #     clone.next = dfs(original_node.next)
        #     clone.random = dfs(original_node.random)
        #     visited[original_node] = clone

        #     return clone

        # return dfs(head)

        # cur = head
        # dummy_head = Node(0)
        # new = dummy_head

        # while cur:
        #     newNode = Node(cur.val)
        #     new.next = newNode
        #     visited[cur] = newNode
        #     cur = cur.next
        #     new = new.next

        # cur = head
        # new = visited[cur]
        # while cur:
        #     if not cur.random:
        #         new.random = None
        #     else:
        #         new.random = visited[cur.random]
        #     cur = cur.next
        #     new = new.next

        # return  dummy_head.next



