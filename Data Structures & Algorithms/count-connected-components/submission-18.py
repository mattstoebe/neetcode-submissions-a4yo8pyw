from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # ok so i know how to traverse a graph but then I need to mark certain edges as 
        # like traversed. i could use some sort of counter and then total edges - edges traversed maybe +1 
        # but no its not total edges it some sort of number from the graph itself. Like number of keys
        # and then when the process dies if there are more keys unreached we iterate and keep going

        # yea so we can loop through the starting nodes in the graph and do the traversal. As we do the 
        # traversal, we indicate which node has been visited. Once we reach then end, we go back to the 
        # list of all ndoes and we iterate through until we find a key that has not yet been searched on
        # we then iterate our counter and repeat. So we don tneed some funky subtraction. Its just explore,
        # track waht was explored and then when it ends see if there is more to explore against waht we already tracked


        # Step 1 would be to build the graph. 
        # We ned to look both ways (undirected) and then will neeed to handle the circularity issue
        graph = defaultdict(list)
        for key, value in edges:
            graph[key].append(value)
            graph[value].append(key)

        print(graph)
        # step 2 is to do the exploration. here we need a variable is visited to track that
        # We may also need something for the branch we are actively visiting. 

        visited = set()

        # We will also need to track the parent since we disregard the parent connection when we get the nbrs

        def dfs(node, parent):
            if node is None:
                return 
            if node in visited:
                return
            
            
            print(node, visited)
            visited.add(node)
            

            
            # I think this will also handle cycles. 
            

            for nbr in graph[node]:
                # skip self refferential issues
                if nbr == parent:
                    continue

                dfs(nbr, node)

        i=0
        for start in graph.keys():
            if start not in visited:
                dfs(start, None)
                i+=1
        
        return n - len(visited) + i

            
        



