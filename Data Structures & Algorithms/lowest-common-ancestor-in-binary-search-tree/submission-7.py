# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Its like we need to search for these nodes, and then traverse back to the
        # most common point. But how woudl we track what the common point is? we could have 
        # one side be 5 deep and the other be 1 and so on traversing back it would get lost

        # We could hold a base node and then search until we find both and iteratively check base nodes: 
        # This is the least efficient solution so: 
        # root = 5: search left and right for the items. if they are both on th elft of both on the right
        # we iterate root to that side. If they are on opposite sides, we need to stop. This is worst case

        # Ok so i  need to think about how to pass information back up instead of repeativively searching down. 
        #So basically at each level, there are three options for L and R: either True False None
        # DFS will get us all this info at each level at the right time. We are waiting until L and R are both True 
        # indicating that on that branch we found the target

        # so i was on the right track. at each level, I need to check if 2/3 criteira are matched. That is how the function ends. 

        # Base Case: If we hit the end of a branch (None) 
        # or if we find one of the targets (p or q)
        if not root or root.val == p.val or root.val == q.val:


            return root
    
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both sides found a target, this root is the LCA
        if left and right:
            return root
            
        # Otherwise, return the one that isn't None (or None if both are None)
        return left or right