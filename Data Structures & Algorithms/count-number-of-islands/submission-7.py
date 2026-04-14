class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # ok so im thinking we scan through the grid row by row. 
        # when we find land. we kick off a search where we  iterate outwards
        # up down right left from that location and flip 1 to zero to flag that
        # land is already associated with an island. once we finish, we keep moving
        # through the grid looking for any remianing land. 


        width, height = len(grid[0]), len(grid)
        islands = 0
        
        def find_nbrs(x,y):
            return [(x + dx, y + dy) for (dx, dy) in [(0,-1), (-1,0), (1,0), (0,1)]]

        def isValid(x,y):
            if 0 <= x <width and 0 <= y < height:
                return True
            return False

        def dfs(x,y):
            # mark as colonized
            grid[y][x] = "x"

            nbrs = find_nbrs(x,y)

            for xnew, ynew in nbrs:
                if isValid(xnew,ynew) and grid[ynew][xnew] == "1":
                    dfs(xnew,ynew)

        for x in range(0,width):
            for y in range(0, height):
                print(x,y)
                if grid[y][x] == "1":
                    islands +=1
                    dfs(x,y)

        return islands


