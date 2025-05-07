from typing import List
from collections import deque

class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:

        # This is naturally a BFS pattern!
        # We can get the number of fresh fruits in O(m*n) time
        # We can also get the locations of the rotten fruits and
        # append them to a queue in O(m*n) time
        # Next we can set a timer starting at 0 minutes
        # Now we do BFS from the rotten locations one layer at a time,
        # ensuring that any in bounds fresh fruit is rotted and added
        # to the queue. Remember to decrement number of fresh fruits
        # After every layer we move to the next minute
        # 
        # Since we want to find out when all fruits are rotten, we 
        # do BFS until the queue is emptied OR when there are no
        # fresh fruits, which ever comes first
        # 
        # We only return time if we have no fresh fruits


        # Set a queue
        q = deque()

        # Keep time and number of fresh fruits
        time, fresh = 0, 0

        # Store the dimension of the grid
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    # Keep track of fresh oranges
                    fresh += 1
                if grid[r][c] == 2:
                    # Append coordinates of rotten
                    # to queue
                    q.append([r,c])

        # Four directions to move in
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh > 0:
            # We do BFS while the queue has elements
            # to be checked OR if there are no more
            # fresh fruits

            for i in range(len(q)):
                # Iterate over layer 1
                
                # Get row and column indices
                r,c = q.popleft()

                # Go in four directions
                for dr, dc in directions:
                    
                    row, col = dr+r, dc+c

                    
                    if (row < 0 or row == len(grid) or 
                        col < 0 or col == len(grid[0]) or
                        grid[row][col] != 1):
                        # We are out of bounds or
                        # at a non-fresh fruit
                        continue

                    # Go to in bounds and fresh
                    # fruit to rot it
                    grid[row][col] = 2
                    # Add the location of this
                    # newly rotted fruit to the
                    # queue
                    q.append([row,col])

                    # Decrement fresh
                    fresh -= 1
            # Time marches on to the next minute
            time+=1

        # Return time if there are no more fresh fruits
        return time if fresh == 0 else -1

if __name__ == "__main__":
    sol = Solution()
    grid = [[1,1,0],[0,1,1],[0,1,2]]
    print(sol.orangesRotting(grid)) # 4
    grid = [[1,0,1],[0,2,0],[1,0,1]]
    print(sol.orangesRotting(grid)) # -1
    pass