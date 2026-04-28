class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # So the solution here would be as follows
        # Get a list of every word in the board ( this is huge i wonder if there is a way to skip)
        # convert the list of words into a trie. (we should be able to skip the lsit step)

        # use the Trie to search for the words 
        
        
        # So the build trie step is interesting. At every letter we can either go up down righ tor left
        # We also cant go the way we came. Ive seen this algorithm before, its backtracing. So our iteration 
        # needs to apss in where we came from where we are at and then generate neighbors remove the where we came from 
        # neighbor and then go a step into it

        # at the same time we will be building the trie. At each recursive function we can pass the trie[child] and then
        # just keep iterating. In this case we CAN revisit letters but not in the current list. 
        # so we also will need to maintain a branch level set of letters that wea re visiting.

        # For initialization, we can start at every letter and then begin the recursive algorithm
        
        # First lets try to build a trie for one starting index

        def getNeighbors(col, row):
            return [(col + dy, row + dx) for dy, dx in[(-1,0), (0,-1), (1,0), (0,1)]]

        def isValid(col, row):
            if col < 0 or row < 0:
                return False
            
            if col >= len(board[0]) or row >= len(board):
                return False
            
            return True


        def buildTrie(words:list[str]) -> dict[str, str]:
            trie = {}
            for word in words:
                cur = trie
                for char in word:
                    if char not in cur:
                        cur[char] = {}
                    cur = cur[char]
                cur['End'] = True
        
            return trie

        def dfs(col, row, cur, prefix=""):
            
            char = board[row][col] # we know this is valid but not if its in the trie
            prefix += char
            if char not in cur: # here we prune the branch to see if its in the trie
                return
            cur = cur[char]

            # Here we check if we have reached the end of our word. 
            # We dont return here because we need to keep seearching for other potential words
            if cur.get('End', False):
                out.add(prefix)
            

            nbrs = getNeighbors(col, row)
            
            for colnew, rownew in nbrs:
                
                if isValid(colnew, rownew) and (colnew, rownew) not in visiting:
                    # now we have a valid neighbor and we can iterate
                    visiting.add((colnew, rownew))
                    dfs(colnew, rownew, cur, prefix)
                    visiting.discard((colnew,rownew))
            
        trie = buildTrie(words)
        cur = trie
        visiting = set()
        out = set()
        rows = len(board)
        cols = len(board[0])
        
        for row in range(rows):
            for col in range(cols):
                visiting.add((col,row))
                dfs(col, row, cur)
                visiting.remove((col,row))


        return list(out)
                 
        
        
    