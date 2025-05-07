from typing import List
from collections import deque

class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:

        # We can get the number of fruits in O(m*n) time
        # Next we can set a timer starting at 0 minutes
        # We keep a set of rotten fruits, initialised to
        # 0
        # Now from every rotten fruit we branch out to 
        # a fresh fruit and rot it
        # Increase number of rotten fruits for each pop
        # This is naturally a BFS pattern!


        # Store the dimension of the grid
        ROWS, COLS = len(grid), len(grid[0])
        
        # Get number of fruits
        fruits = 0
        
        # Store the number of rotten fruits SEEN
        rottenFruits = 0

        # Keep a set of rotten fruits
        rottenLocations = set()

        for r in range(ROWS):
            for c in range(COLS):
                # If we see a rotten fruit, add its coordinates
                if grid[r][c] == 2:
                    rottenLocations.add((r,c))

                if grid[r][c] == 1 or grid[r][c] == 2:
                    fruits+=1
        # Create a queue for BFS
        q = deque()

        # Helper function to find valid neighbours  
        def addValidNeighbour(r,c,rottenFruit):
            # If it is not valid, do nothing
            if (r<0 or r >= ROWS or c < 0 or c >= COLS):
                # (r,c) is out of bounds or
                # (r,c is not a fresh fruit)
                return
            
            if grid[r][c] != 1:
                # We have a valid location, but it is not fresh!
                return

            # Okay, now we have a fresh fruit
            
            # We rot this fruit
            grid[r][c] = 2
            # We add it to our queue
            q.append((r,c))
            # We add it to our rotten locations set
            rottenLocations.add((r,c))

            return
            

        # BFS function
        def bfs():
            
            
            # Add locations of rotten fruits to the queue
            for location in rottenLocations:
                q.append(location)

            
            # Set minutes to None
            minutes = None

            # Run until the queue is empty
            while q:
                # Store the number of rotten fruits at this layer
                sizeOfLayer = len(q)
                # Pop elements at this layer
                for fruit in range(sizeOfLayer):
                    # Get the rotten fruit
                    rottenFruit = q.popleft()
                    # Get location
                    r, c = rottenFruit[0], rottenFruit[1]
                    # Add the locations of the left, right, up, and 
                    # down positions
                    addValidNeighbour(r+1, c, rottenFruit)
                    addValidNeighbour(r-1, c, rottenFruit)
                    addValidNeighbour(r, c+1, rottenFruit)
                    addValidNeighbour(r, c-1, rottenFruit)
                
                # We start at minute 0 when the first layer 
                # is covered
                # So we set minutes to 0, but we only start 
                # incrementing after the first layer is covered
                if minutes == None:
                    minutes = 0
                else:
                    minutes += 1
                
            # After BFS we return minutes
            return minutes
        # Call BFS and get minutes
        minutes = bfs()


        
        if len(rottenLocations) == fruits:
            # The size of the rotten fruit set is the same as fruits, 
            # so we return minutes
            return minutes
        else:
            # Not all fruits are rotten
            return -1

if __name__ == "__main__":
    sol = Solution()
    grid = [[1,1,0],[0,1,1],[0,1,2]]
    print(sol.orangesRotting(grid)) # 4
    grid = [[1,0,1],[0,2,0],[1,0,1]]
    print(sol.orangesRotting(grid)) # -1
    pass