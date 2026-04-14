class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: 
            return None

        # 1. The first element of preorder is always the root
        root_val = preorder[0]
        root = TreeNode(root_val)

        # 2. Find where the root is in the inorder list
        # This tells us how many nodes are in the left vs right subtree
        mid = inorder.index(root_val)

        # 3. Recursive calls with correct slicing:
        
        # Left subtree:
        # Preorder: skip the root, take 'mid' number of elements
        # Inorder: take everything before 'mid'
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[0 : mid])
        
        # Right subtree:
        # Preorder: take everything after the left subtree nodes
        # Inorder: take everything after 'mid'
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root