# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def treeEqual(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if not a and not b:
            return True
        elif not a or not b:
            return False
        elif a.val != b.val:
            return False

        else:
            return(
                self.treeEqual(a.left, b.left) and
                self.treeEqual(a.right, b.right)
            )

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # This is very similar to checking if two trees are equal. 
        #First, we implement that functionality

        if not root:
            print("no root ending")
            return None

        if root.val == subRoot.val:
            print("checking equality on root", root.val)
            if self.treeEqual(root, subRoot):
                return True
        
        print("evaluating at root", root.val)
        lefteval = self.isSubtree(root.left, subRoot)
        righteval = self.isSubtree(root.right, subRoot)

        return lefteval or righteval or False
