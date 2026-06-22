
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}
        curr = head
        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        newHead = node_map[curr] if curr else None
        newCurr = newHead
        while curr: 
            newCurr.next = node_map[curr.next] if curr.next else None
            newCurr.random = node_map[curr.random] if curr.random else None
            newCurr = newCurr.next
            curr = curr.next
        return newHead