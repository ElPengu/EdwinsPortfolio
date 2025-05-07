from collections import deque

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        '''
        - We have an mxn grid
        - You can move down or right at any point in time
        - How many UNIQUE paths can you take from grid[0][0]
        to grid[m-1][n-1]

        - Intuitively we know that there is exactly 1 path 
        to grid[0][0]... 1
        - You can reach grid[i][j] by going down or right
        - Down: grid[i][j-1]->grid[i][j]
        - Right: grid[i-1][j]->grid[i][j]
        - Let us store paths to grid[i][j] in DP[i][j]
        - grid[i][j] = grid[i][j-1] + grid[i-1][j]

        - BASE CASE
        - FORALL i,j: DP[i][j] = 1
        - INDUCTIVE STEP
        - DP[i][j] = DP[i][j-1]+DP[i-1][j]
        - RETURN DP[m,n]

        - Arghhh, this is my first 2D DP problem, 
        but I am JUST missing the intuition for 
        searching!

        '''

        # BASE CASE
        dp = {}
        for i in range(m):
            dp[i] = []
            for j in range(n):
                dp[i].append(1)

        # INDUCTIVE STEP
        # We'll use BFS to branch out
        q = deque()
        q.append((0,0))
        while q:
            print(f"dp: {dp}")
            # Pop from queue
            loc = q.pop()

            x,y = loc[0],loc[1]
            if x == m-1 and y == n-1:
                # If we are at location then 
                # continue
                # This will result in us 
                # emptying the queue
                continue
            
            # Find the number of paths
            paths = dp[x][y]

            # Add the neighbours
            neighbours = [(x+1,y),(x,y+1)]
            for nei in neighbours:
                neiX, neiY = nei[0], nei[1]

                if not (neiX >= 0 and neiY>=0 and
                    neiX <m and neiY<m):
                    # Skip invalid neighbours
                    continue

                # Update DP for this neighbour
                dp[neiX][neiY]+=dp[x][y]

                # Push this onto the queue
                q.append((neiX,neiY))

        
        print(f"dp: {dp}")    

        return dp[m-1][n-1]

if __name__ == "__main__":
    sol = Solution()
    m,n = 3,6
    print(sol.uniquePaths(m,n)) #21
    m,n = 3,3
    print(sol.uniquePaths(m,n)) # 6