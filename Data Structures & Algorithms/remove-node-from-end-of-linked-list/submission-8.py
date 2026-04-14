# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # To remove the Nth Node, we can take two pointers. One is going to be ierated n times. 
        # Then we iterate first and second pointers until the faster pointer hits the end of the list. 
        # At that point, we will do last.next = last.next.next where last is the one before current. 
        dummy = ListNode(None, head)
        slow, fast = dummy, dummy
        
        for i in range(n):
            print('bump')
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        
        slow.next = slow.next.next
        

        return dummy.next
        
