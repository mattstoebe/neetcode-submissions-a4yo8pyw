# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # This is level-wise BFS. we need to add starting values to chck list, 
        # get its length, that is the length of the level, then add in the neighbors,
        # Then we pop from the queue n time swhere n = level size and put them in a list.
        # We dont even need to track visited because there is only one path to each node
        if not root: return []
        
        tocheck = deque()
        tocheck.append(root)
        out = []
        layer = 0
        while tocheck:
            layersize = len(tocheck)
            out.append([])
            print("layer", layer, "size", layersize)
            for i in range(layersize):
                proc = tocheck.popleft()
                out[layer].append(proc.val)

                
                if proc.left:
                    tocheck.append(proc.left)
                if proc.right:    
                    tocheck.append(proc.right)

            layer +=1
                
        return out

