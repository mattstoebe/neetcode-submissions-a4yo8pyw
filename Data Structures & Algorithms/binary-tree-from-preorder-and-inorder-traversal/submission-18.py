class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Ok so i kindo fremember this solution but lets try to thinka bout it from first 
        # Principles. The main thing I remember is one of the lists tells us where to split
        # The other list. and i also remember that i was doing a .index() call which made it 
        # n2 but if i change to a hasmap i should be able to reduce to O1

        # the first element if the pre order list tells us whats on the left and the right 
        # of the Tree. so if we can find that element in In order, we can reduce the problem to sub
        # problems. we can return from there the left tree and right tree and then build our tree from 
        # That


        # First i need to establish tree at current level
        
        if not preorder or not inorder:
            return None
        
        rootnode = preorder[0]
        result = TreeNode(val = rootnode)
        # print(preorder, inorder, rootnode)
        
        mid = inorder.index(rootnode)

        result.left = self.buildTree(preorder[1: mid+1], inorder[0:mid])
        result.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return result