from typing import List

class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # How could a graph help us here?
        # Okay, we could store all possible coordinates
        # in a hash map
        # Next, we start from an arbitrary coordinate
        # Now we branch out to neighbours
        # If we have not VISITED this neighbour then we
        # add it to VISITED
        # Now we return min(1+dfs(neighbour1), 1+...)
        # What does this do?
        # Well we iterate through all coordinates 
        # manually, setting the distance in the 
        # hash map to be the minimum of what it is
        # and the distance returned by dfs  
        # Now within DFS we explore neighbours, 
        # and set w/e the minimum distance is
        # Idk, it makes sense to me since base case 
        # is that the neighbour to treasure will 
        # be min(...,0+1), and we recurse back
        # 
        # We want to modify distances IN PLACE
        # I guess we don't need the hash map, 
        # we can see if it has been visited with the 
        # set

        # Set of visited coordinates
        visited = set()

        # Store all rows and columns
        ROWS, COLS = len(grid), len(grid[0])


        # Backtracking function
        def dfs(r,c):
            # BASE CASES

            # If we are out of bounds then 
            # we want to end the call
            # We return INF
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS):
                return 2147483647

            # If we are on a water cell 
            # then we want to end the call
            # We may return INF
            if grid[r][c] == -1:
                return -1

            # Now we are either on land 
            # or on treasure!
            
            # If we have already visited this 
            # place, we can just return 
            # whatever distance it has 
            # so far
            if (r,c) in visited:
                return grid[r][c]

            # We see this coordinate, add it to 
            # our visited set
            visited.add((r,c))
            
            # If we are on a treasure chest, 
            # be sure to return 0!
            if grid[r][c] == 0:
                return 0
            
            # We go to its neighbours
            # Distances to go UP, DOWN, LEFT, RIGHT
            distances = [[0,1],[0,-1],[-1,0],[1,0]]
            for distance in distances:
                # Get distances in row,col format
                dr, dc = distance[0],distance[1]

                # Store the new row and new column
                # pair to explore
                newR, newC = r+dr, c+dc

                foundDistance = dfs(newR,newC)
                if foundDistance >= 0:

                    # We minimise distance
                    grid[r][c] = min(grid[r][c], 1+dfs(newR, newC))

            # We have exhausted all options, return whatever 
            # distance we have optimised to at this 
            # coordinate
            return grid[r][c]



        # Loop over all coordinates
        for r in range(ROWS):
            for c in range(COLS):
                foundDistance = dfs(r,c)
                if foundDistance >= 0:

                    # We minimise distance
                    grid[r][c] = min(grid[r][c], 1+dfs(r, c))

                # We clear visited nodes after the DFS call ends
                visited = set()

        # Return the grid
        return grid

        pass


if __name__ == "__main__":
    sol = Solution()

    grid = [
            [2147483647,-1,0,2147483647],
            [2147483647,2147483647,2147483647,-1],
            [2147483647,-1,2147483647,-1],
            [0,-1,2147483647,2147483647]
            ]

    print(sol.islandsAndTreasure(grid)) 
    '''
    [
    [3,-1,0,1],
    [2,2,1,-1],
    [1,-1,2,-1],
    [0,-1,3,4]
    ]
    '''

    grid = [
            [0,-1],
            [2147483647,2147483647]
            ]
    
    print(sol.islandsAndTreasure(grid))
    '''
    [
    [0,-1],
    [1,2]
    ]
    '''