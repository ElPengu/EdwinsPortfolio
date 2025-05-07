from typing import List
from collections import defaultdict
import math
class Solution:

    def swimInWater(self, grid: List[List[int]]) -> int:
        '''
        - We start at square (0,0) on the top left
        - We want to end up at square (n-1,n-1) on the bottom right
        - The elevation of a square is grid[i][j]
        - At time t the water level across the grid is t
        -> So as I understand it, grid[0][0] = 0 and grid[0][1] = 2, you 
        must wait until time 2 so that you can "swim" onto the "shore" 
        of grid[0][1]
        
        - We are essentially asking for a path FROM grid[0][0] TO 
        grid[n-1][n-1]
        - We specifically want a path with minimal maximum elevation

        - STAGE 1: Create an adjacency list from the grid
        - STAGE 2: Perform BFS or DFS on the adjList
        - STAGE 3: Return the path found with minimum maximum elevation
        
        - WOOOOOOOOH, I got this HARD problem working in 35 minutes!!!!

        '''

        # STAGE 1: Create an adjacency list from the grid
        # CREATE adjList
        adjList = defaultdict(list)

        # Rows and columns
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                adjList[r].append((c, grid[r][c]))
                adjList[c].append((r, grid[r][c]))

        # STAGE 2: Perform BFS or DFS on the adjList
        # We hold a set of visited locations
        visit = set()
        def dfs(x, y):

            # We have our x and y

            # BASE CASES
            if (x,y) in visit:
                # Invalid location
                return math.inf
            if (x < 0 or y < 0 or x >= ROWS or y >= COLS):
                # We are out of bounds!
                return math.inf
            if (x == ROWS-1 and y == COLS-1):
                # We are at the location!
                return grid[x][y]
            
            # We are at a valid location, let's add it to visit
            visit.add((x,y))
            # Get the time here
            time = grid[x][y]
            # We call DFS on all possible directions that we could
            # go
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            minTimeByPath = math.inf
            for dx, dy in directions:
                # The time we get out of DFS is the maximum time 
                # along that path
                # We try to find the minimum out of all directions 
                minTimeByPath = min(minTimeByPath, 
                                    dfs(x+dx, y+dy))

            # We have finished visiting this location
            visit.remove((x,y))

            # We return the maximum out of the time along the path and 
            # the time here
            return max(time, minTimeByPath)
            

        # STAGE 3: Return the path found with minimum maximum elevation
        # We call DFS on the first row and first column
        # We need only return the time
        return dfs(0, 0)



if __name__ == "__main__":
    sol = Solution()
    grid = [[0,1],[2,3]]
    print(sol.swimInWater(grid)) #3

    grid = [
            [0,1,2,10],
            [9,14,4,13],
            [12,3,8,15],
            [11,5,7,6]]
    print(sol.swimInWater(grid)) #8