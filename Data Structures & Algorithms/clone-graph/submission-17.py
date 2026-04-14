"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # So in this problem it is about return conditon, clone get neighbors repeat

        # We need to keep a dict of our created clones so that we can add it to the clone retroactively
        visited = {}

        def dfs(node):

            # if we reach the end of the graph we return empty
            if not node: 
                return None
            
            if node in visited:
                return visited[node] # This returns the node copy

            # now we create our clone and add it to our clone registry
            clone = Node(node.val)
            visited[node] = clone
        
            

            for nbr in node.neighbors:
                clone.neighbors.append(dfs(nbr))

            return clone

        out = dfs(node)
        return out


        
      