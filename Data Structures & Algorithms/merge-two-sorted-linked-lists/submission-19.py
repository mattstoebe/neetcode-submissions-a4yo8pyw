# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode(0,None)
        op = out
        h1, h2 = list1, list2

        while h1 and h2:
            if h1.val < h2.val:
                op.next = h1
                # print(h1.val)
                h1 = h1.next

            else:
                op.next = h2
                # print(h2.val
                h2 = h2.next
            
            print(op.val)
            op = op.next

        
        op.next = h2 if h2 else h1 if h1 else None

        return out.next