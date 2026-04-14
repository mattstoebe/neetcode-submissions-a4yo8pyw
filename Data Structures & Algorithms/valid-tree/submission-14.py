class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # my understanding is that to be a valid tree there must be no cycles. 
        # This now reminds me of the previous two problems. 
        # In course schedule we looked for circularities and it seems we woudl do the same 
        # here. We would first map the edges into a dictionary that holds root - value
        # then we would move through that dictionary with some sort of DFS algorith where 
        # we track the branch we are "visiting" in a set. If we find something already
        # in the branch we are visiting we know we have found a cycle and surface a false
        
        # The other thing we needed in the course schedule was a all is visited set so we dont
        # do duplicate work.


        # first we build the graph
        graph = defaultdict(list)
        
        for key, value in edges:
            graph[key].append(value)
            graph[value].append(key)

        is_checked = set()
        visiting = set()
        
        def dfs(node, parent):
            if node in is_checked:
                return True

            if node in visiting:
                return False

            res = True
            visiting.add(node)
            for nbr in graph[node]:
                if nbr == parent: continue
                else:
                    res = res and dfs(nbr, node)

            visiting.remove(node)
            is_checked.add(node)

            return res

        if edges == []:
            return True
            
        out = dfs(edges[0][0], None)

        if len(is_checked) != n:
            return False
        
        return out
        
    