import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # here i need a mechanism to figure out which val is the minimum. 
        # I also need a scalable pointer system that allows me to increment pointers 

        # i could store a list of pointers and increment them by index
        # I just would then need to figure out which head of the each list is the smallest

        # To do this i can use a heap of tuples (val, i) when I pop a value off i can check my pointer list
        # for the location there and add the memory address to my output linked list. 
        # then iterate the pointer[i] to next.

        # The main piece missing now woudl be how I manage the None data. 

        dummy = ListNode()
        pointers = [listobject for listobject in lists]
        main_pointer = dummy

        current_vals = [(pointers[i].val, i) for i in range(len(lists)) if pointers[i] != None]
        heapq.heapify(current_vals)
        
        print(current_vals)

        while current_vals:
            val, idx = heapq.heappop(current_vals)
            main_pointer.next = pointers[idx]
            pointers[idx] = pointers[idx].next
            main_pointer = main_pointer.next

            if pointers[idx] != None:
                heapq.heappush(current_vals, (pointers[idx].val, idx))

            print(val, idx, current_vals)
        
        return dummy.next