# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # this is where dfs pre order post order vs in order comes in. 
        # I need to figure out howt o do it in order so the ordering should be
        # First I pop left then i visit root then i pop right

        stk = [root]
        curr = root
        
        while curr or stk:
            print(stk)
            while curr:
                print("left")
                stk.append(curr)
                curr = curr.left

            proc = stk.pop()
            k -=1

            if k == 0: return proc.val
            curr = proc.right
            