# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Iterateively check if every node is equal then use a boolean

        if not p and not q:
            return True
        
        if not p or not q:
            return False

        thisnode = p.val == q.val
    
    

        leftside = self.isSameTree(p.left, q.left)
        rightside = self.isSameTree(p.right, q.right)


        return (thisnode and leftside and rightside)
