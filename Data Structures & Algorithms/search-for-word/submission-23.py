class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # so we iterate through the grid. We should look at all the starting nodes
        # Then for each starting node we get all the neighbors and step to them and see
        # if they contain the next letter in the string. If they do, we move to there and repeat
        # if not, we iterate to the next neighbor. If none of the neighbors have the vlaue
        # we iterate to the next start

        # so first lets do one pass over the string and get all the starting places
        # second lets make the function to get all the neighbors
        # Third lets do the backtracing


        width = len(board[0])
        height = len(board)
        starts = []

        for i in range(height):
            for j in range(width):
                if board[i][j] == word[0]:
                    starts.append((i,j))
        
        # edge case where the first letter is nowhere in the thing
        if not starts:
            return False
        
        def neighbors(i,j):
            return [(i + di, j + dj) for (di, dj) in [(-1,0), (0, -1), (1,0), (0,1)]]

        def isValid(i,j):
            if 0 <= i < height and 0<= j < width:
                return True
            else: 
                return False

        def backtrace(i,j,charindex):
            # here we take the character and the we run itself on all neighbors in a certain order
            # first we need to see if the index is valid
            if charindex == len(word):
                return True

            # out of bounds condition
            if not isValid(i,j):
                return False
            
            # now we do the backtracing pattern
            # First we see if current location is wher we need to be in the string
            
            if board[i][j] != word[charindex]:
                return False
            
            #Now for the we found it condition:
 

            # Now we know we are in bounds, we havent hit the end of the word, 
            # and the current character is on the right track
            # so we can confidently continue to the next step
            
            nbrs = neighbors(i,j)
            out = False
            for k,l in nbrs:
                temp = board[i][j]
                board[i][j] = "#"
                out = out or backtrace(k,l, charindex+1)
                board[i][j] = temp
            
            return out

        result = False
        while starts:
            
            proc = starts.pop()
            result = result or backtrace(proc[0],proc[1], 0)
            
        return result


