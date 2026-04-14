# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    result = None

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # So I watched the neetcode explainer here. My starting knowledge is as follows
        # First, we must have a bend in the tree. 
        # Second at each place we want to check the running totals of what is below it
        # and then see what the tree would produce if bent/ split at that node and then 
        # Use that to update our running max. Then we can move up a level and continue
        # When we move up a level we need to pass the greatest non-bent route. 

        # Because we need info from below, we will use psot-order. So we will do 
        # Left Right Process. 
        # The process step is two fold. First we need to update the global max
        # Second we need to return the greatest of left nad right
        def post_order(root):
            
            if not root:
                return 0 # At the base the sum is zero

            left = post_order(root.left)
            right = post_order(root.right)
            left = max(left, 0)
            right = max(right, 0)
            
            candidate = left + right + root.val
            
            if not self.result or candidate > self.result:
                self.result = candidate

            return max(left, right) + root.val


        post_order(root)
        return self.result