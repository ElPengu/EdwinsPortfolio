from collections import deque

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        '''
        - We have an mxn grid
        - You can move down or right at any point in time
        - How many UNIQUE paths can you take from grid[0][0]
        to grid[m-1][n-1]
        
        - Down: grid[i][j-1]->grid[i][j]
        - Right: grid[i-1][j]->grid[i][j]
        
        - Notice that from a spot on the grid you 
        can take a path through any other accessible
        spots
        -> From grid[0][0] you can take a path through
        ANY locations
        -> If you go from grid[1][0], you can take a 
        path through ANY locations EXCEPT from column=0
        
        - Notice that if we do this recursively, there
        are two ways to reach grid[1][1]
        -> grid[0][1] -> grid[1][1]
        -> grid[1][0] -> grid[1][1]

        - CACHE
        - We will store cache[i][j] to store the number 
        of paths to the target from i, j
        - How do we calculate cache[i][j]? By summing 
        the paths if we were to go right vs down
        - cache[i][j] = cache[i+1][j]+cache[i][j+1]
        - Okay, but how do we calculate these operands?
        - We need a base case!
        - At grid[m-1][n-1] we know there is exactly 1
        path. 
        - grid[m-1][n-1] = 1
        
        - Okay, but what if our down/right is out of 
        bounds?
        - EXAMPLE: grid[m-1][n-1] -> grid[m-1][n-2]
        - grid[m-1][n-2] = grid[m][n-2]+grid[m-1][n-1]
        - Well, there is no path from an out-of-bounds
        location to the target. I.e., there are 0 paths!
        - Hence... 
        - grid[m][n-2] = 0
        - grid[m-1][n-1] = 1
        - grid[m-1][n-2] = 0+1=1 

        - SEARCHING THE GRID
        - The right-most and bottom-most locations 
        will have exactly one path to the target
        - If you are on the bottom ROW you can only
        go right, if you are on the right-most 
        COLUMN you can only go down
        - With this in mind we start at the bottom 
        ROW and compute one row at a time
        
        - INTUITION FOR WHY WE CAN SEARCH THE GRID
        ROW-BY-ROW
        - BASE CASE 
        - At base case the entirety of the bottom 
        row is just 1's, as is the entirety of the 
        right row
        - INDUCTIVE STEP
        - We compute row i+1 and move to row i
        - At every location in i we strictly need 
        the number of paths by going DOWN and by 
        going RIGHT
        - We already have the DOWN paths at row i+1 
        as assumed
        - We already have the RIGHT path at (i+1,n-1)
        as defined by the base case
        - This enables us to calculate (i+1,n-2)
        - And so on until (i+1,0)
        - This implies that every time we move up a 
        row we MUST work from the right-most location 
        left-wards!
        - This completes the inductive step!

        '''

        # Set the BOTTOM row, the length of the number
        # of rows. There will be exactly one path 
        # from a position here to the target (down)
        row = [1]*n

        for i in range(m-1):
            # Go through all the rows EXCEPT the last one

            # Compute a new row above the old row
            newRow = [1]*n

            for j in range(n-2, -1, -1):
                # Avoid checking out of bounds by not checking
                # the last most value

                # newRow[j+1] holds the number of paths 
                # found from the right neighbour
                # row[j] holds the number of paths found from
                # the bottom neighbour
                newRow[j] = newRow[j+1]+row[j]
            
            # Update the row
            row = newRow

        # We want the number of paths at (0,0)
        return row[0]        

        pass

if __name__ == "__main__":
    sol = Solution()
    m,n = 3,6
    print(sol.uniquePaths(m,n)) #21
    m,n = 3,3
    print(sol.uniquePaths(m,n)) # 6