# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(root, low =  -float('inf'), high =  float('inf')):

            if root is None:
                # at the bottom, it doenst matter what the number is
                return True

            # I should actually be going top down instead of bottom up

            if low < root.val < high:
                # if this node is good then we go a step deeper
                return(
                    isValid(root.left, low, root.val) 
                    and 
                    isValid(root.right, root.val, high))

            else: return False

        
        return isValid(root)


            


            # now max comes from the right side - should be minimum observed on the right
            #min comes from the left side- Maximum observed on the left
