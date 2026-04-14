# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # So i was thinking about doing this from the bottom up, but neetcode poitns 
        # out I can just recursively call this function and iterate through. so:
        if not root:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp
        

        # Now we iterate down a level and reverse the following
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root