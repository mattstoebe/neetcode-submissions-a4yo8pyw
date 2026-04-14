class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # So we could have a sort of visited set that manages what courses we have taken
        # this is only 1 level deep. Ie a course only has one prerequsite. so if i grab the 
        # in the list i can check if that top value is in any of the other lists

        # Its lilke i need to build a graph first then I need to try to find the root node
        # So i need to build a graph and then do cycle detection. I can do fast and slow cycle
        # detection where we move pointers along at differnet speeds until they meet. 

        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visiting = set()

        def dfs(node):
            # if we reach the bottom of the grpah then this part is legit
            
            if node in visiting:
                return False
            
            if not graph.get(node, None):
                return True

            # How do we detect a cycle
            # Ok i cheated but we coudl do a backtracing approach.

            visiting.add(node)
            ret = True
            for prereq in graph[node]:
                ret = ret and dfs(prereq)

            visiting.remove(node)
            
            return ret

        out = True
        verified = set()

        for _, course in prerequisites:
            if course not in verified:
                out = out and dfs(course) # need to find root
                verified.add(course)

            

        return out


