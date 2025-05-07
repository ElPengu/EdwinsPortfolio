from typing import List
from collections import defaultdict
import heapq
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

        - We will use a modified form of Djikstra's algorithm
        - We will use a priority queue (heap) not a queue

        - We start at the top right
        - We push the cost of GETTING to the next possible new locations 
        along the path and the location to the minheap
        - This means that when we pop from the min heap we get the node 
        with the smallest cost of reaching it

        - Here is some pseudocode for what is going on
        - INITIALISE SET VISIT
        - INITIALISE MINHEAP
        - STEPS:
        - POP elevation, coordinate FROM MINHEAP
        - IF coordinate IS destination: RETURN elevation, elevation
        - FOR coordinate we can travel to: 
        -> IF coordinate IS OUTOFBOUNDS or coordinate IN VISIT: continue 
        -> PUSH (MAX(elevation, elevation_coordinate), coordinate) TO 
        MINHEAP 
        -> PUSH coordinate TO VISIT

        '''

        # Get the length of the square grid
        N = len(grid)
        # Create a visit hash set
        visit = set()
        # We also initialise a minimum heap for (time/height, r, c)
        minH = [[grid[0][0],0,0]]
        # A little helper variable for the four directions that we can 
        # travel to
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        while minH:
            # Pop from the minimum heap
            t,r,c = heapq.heappop(minH)

            # We now visit this location
            visit.add((r,c))

            if r == N-1 and c == N-1:
                # We are at the destination
                return t
            
            for dr,dc in directions:
                # Compute neighbour location
                neiR, neiC = r+dr, c+dc
                # We do NOT go to out of bounds locations, nor do we revisit nodes
                if (neiR < 0 or neiC < 0 or 
                    neiC == N or neiR == N or
                    (neiR,neiC) in visit): continue
                
                # We mark it as visited
                visit.add((neiR, neiC))

                # We push this location
                # NOTE: we add a value that is the max height along 
                # the PATH to reach this location
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])
            



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