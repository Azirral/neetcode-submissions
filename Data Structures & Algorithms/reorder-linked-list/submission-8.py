# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Approach: 
        # 1. Get the number of nodes = total
        # 2. If total % 2 == 0 then lenA = total / 2 else lenA = total // 2 + 1
        # 3. iterate through the list until the lenA is met, then reverse the list
        # 4. To reverse the list first, I need 
        # 5. Link the nodes

        # 4. 

        # 1.
        total = 0
        curr = head

        while curr:
            total += 1
            curr = curr.next
        
        # 2.
        left_len = total // 2 + 1 if total % 2 else (total / 2)
        
        # 3.
        curr = head
        while left_len > 0:
            left_len -= 1
            temp = curr.next
            if (left_len == 0):
                curr.next = None
            curr = temp

        # 4. reverse
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head1 ,head2 = head, prev
        while head1 and head2:
            nxt1 = head1.next
            nxt2 = head2.next

            head1.next = head2
            head1 = nxt1

            head2.next = head1
            head2 = nxt2 
        return head2
