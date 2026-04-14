# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        # Find Mid point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        prev = None
        cur = slow.next
        slow.next = None
        
        #reverse second half
        while cur:
            nxt = cur.next
            cur.next = prev
            
            prev = cur
            cur = nxt

        # now we alternate between the main list and prev
        h, p = head, prev
        while h and p:
        
            hnxt = h.next
            pnxt = p.next

            h.next = p
            p.next = hnxt
            
            p = pnxt
            h = hnxt
        



