# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.serialized = []
        
        def preorder(root):
            
            if not root:
                self.serialized.append("None")
            else:
                self.serialized.append(str(root.val))
                preorder(root.left)
                preorder(root.right)


        preorder(root)
        out = ','.join(self.serialized)
        print(out)
        return out
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Add data to stack until I find a None. Then pop off the top of the stack and make the None the left child
        # then go to next value and keep going 
        data = data.split(",")
    
        self.curr = -1    
    
        def preorder(data: list):
            
            self.curr +=1
            
            if data[self.curr] == "None":
                return None
            else:
                root = TreeNode(val = data[self.curr])

                root.left = preorder(data)
                root.right = preorder(data)

            return root

        out = preorder(data)
        print(out)
        return out