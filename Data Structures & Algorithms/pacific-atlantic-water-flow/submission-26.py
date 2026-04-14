class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # For each cell we are searching for a path to the ocea. 
        # This path only survives if it goes flat or down. we can return False when it dies
        # and bubble up a true if not. we can do an false or result kind of situation. 

        # Lets start this from a single cell say 

        width,height = len(heights[0]), len(heights)

        def findNbrs(x,y):
            return [(x + dx, y + dy) for (dx, dy) in [(-1,0), (0,-1), (1,0), (0,1)]]

        def isValid(x,y):
            if 0 <= x < width and 0 <= y < height:
                return True
            return False

        def foundPacific(x,y):
            if x == 0 or y == 0:
                return True
            return False

        def foundAtlantic(x,y):
            if x == width-1 or y == height-1:
                return True
            return False

        # ok so i tried sarching from all the squares but what if instead I looked
        # At the water spreading and then tracked in an output what cells had been hit/

        # This could also be done as level wise BFS> I think i will do that. in other words
        # Take all the out of bounds starting locations and put them in the location. thats 
        # Phase one than iterate till you cant anymore
        out_grid = [[[False, False] for _ in range(width)] for _ in range(height)]

        pacific_starts = [(i, 0) for i in range(width)] + [(0, j) for j in range(height)]
        atlantic_starts = [(i, height-1) for i in range(width)] + [(width-1, j) for j in range(height)]
        print(pacific_starts)
        print(atlantic_starts)
        res = []
        def levelBfs(tocheck, ocean_pass):
            tocheck = deque(tocheck)
            while tocheck:
                # pop the item off the queue
                x,y = tocheck.popleft()
                val = heights[y][x]
                # mark it as visited
                out_grid[y][x][ocean_pass] = True


                nbrs = findNbrs(x,y)

                for xnew, ynew in nbrs:
                    if isValid(xnew, ynew) and not out_grid[ynew][xnew][ocean_pass] and val <= heights[ynew][xnew]:
                        tocheck.append((xnew, ynew))


        levelBfs(pacific_starts, 0)
        levelBfs(atlantic_starts, 1)
        res = []
        
        for y in range(height):
            for x in range(width):
                if out_grid[y][x][0] and out_grid[y][x][1]:
                    res.append([y, x])
        return res

            




