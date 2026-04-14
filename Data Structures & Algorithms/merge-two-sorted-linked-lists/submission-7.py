# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        outlist = ListNode(None, None)
        out = outlist
        c1, c2 = list1, list2
        

        while c1 and c2:
            print(out)
            if c1.val < c2.val:
                
                out.next = c1
                c1 = c1.next

            else:
                out.next = c2
                c2 = c2.next
            
            out = out.next

        if c1 == None:
            out.next = c2
        if c2 == None:
            out.next = c1

        return outlist.next

            


