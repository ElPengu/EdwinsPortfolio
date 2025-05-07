from typing import List
from collections import deque

class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]])->int:

        # This lends itself to BFS/DFS
        # We'll use recursive DFS to be different from 
        # the previous question
        # We have a visit set of coordinates
        # We do DFS from each coordinate
        # We DFS up, down, left or right to another land 
        # coordinate that we have not seen
        # Simples!

        # Get the rows and columns in the grid
        ROWS, COLS = len(grid), len(grid[0])
        # Store the visited coordinates
        visit = set()

        # DFS function that returns area
        def dfs(r,c):
            # Base case
            # > Out of bounds
            # > Non-land
            # > Already visited land
            if (r < 0 or r == ROWS or c < 0 or c == COLS or 
                grid[r][c] == 0 or (r,c) in visit):
                # We are returning 0 additional area
                return 0
            # We have landed on uncharted land!

            # Add this to our visit set
            visit.add((r,c))

            # Calculate the area that we are at and 
            # area found by exploring the other directions
            return (1 + dfs(r+1,c) + 
                    dfs(r-1,c) + 
                    dfs(r,c+1) + 
                    dfs(r,c-1))
        
        # Maintain area
        area = 0
        # Iterate over the entire grid
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r,c))

        return area

if __name__ == "__main__":
    sol = Solution()

    grid = [
    [0,1,1,0,1],
    [1,0,1,0,1],
    [0,1,1,0,1],
    [0,1,0,0,1]
    ]
    print(sol.maxAreaOfIsland(grid)) # 6