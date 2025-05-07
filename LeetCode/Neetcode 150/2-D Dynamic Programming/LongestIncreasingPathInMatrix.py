from typing import List

class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
        - This is one of the more do-able HARD problems <- Neet

        - 2D grid of integers
        - Every integer >= 0
        - To form a path you may move horizontally or vertically
        - Return the length of the longest strictly increasing path

        - Note on the definition of a path: vertices nor edges may 
        repeat

        - Observation: At worst case, every position is of length 1 
        - Observation: Strictly increasing path means that values 
        cannot repeat
        - Observation: Let's say there is longest strictly increasing 
        path 1,2,6,9. This implies that from 2, the longest must be 
        2,6,9

        - LIP = longest strictly increasing path

        - BRUTE FORCE
        - We start from every position as if it is the start of the 
        LIP and search its neighbour, return the LIP found in a 
        position
        - We run DFS on every position
        - Let's say we run DFS on (i,j) and search (i+1,j) and the rest 
        of the neighbours recursively
        - Now we iterate to (i+1,j), and from here we run DFS on (i,j)
        - Do we need to re-run DFS on (i,j)? No. We already have the 
        LIP from (i,j)!
        - Return the largest LIP

        - CACHING
        - Instead of just running DFS on every position, we will cache 
        the LIP from every position after running DFS on it
        - Now whenever we want to run DFS on a position in a recursive 
        call, we return whatever is store in the cache for it IFF it 
        exists there 
        - Now return the largest LIP found
        - O(nm) space <- for the matrix and cache
        - O(nm) time <- Intuitively, you run DFS at most once from every 
        position
        -> If you start at the end position of the LIP whilst iterating, 
        you will have to iterate over every other position ANYWAY as 
        you iterate over the preceding position of the LIP using the 
        cache which takes O(1) time
        -> If you start at the start position of the LIP whilst 
        iterating, you will store all the positions of the LIP in the 
        cache so you will end up taking O(1) time as you use the cache 
        on the successive positions of the LIP
        '''

        # Store the rows and columns
        ROWS, COLS = len(matrix), len(matrix[0])

        # Create a cache for dp as a hash map
        # (row, column) -> LIP
        dp = {}

        def dfs(r,c, prevVal):
            # r,c -> position that we are evaluating

            # BASE CASES
            if (r < 0 or r == ROWS or 
                c < 0 or c == COLS or 
                matrix[r][c]<=prevVal):
                # Are we out of bounds
                # Are we at a position that is NOT larger than 
                # where we came from
                # In either case, the previous position cannot make 
                # a path to us, so we return 0

                return 0
            if ((r,c) in dp):
                # We have already computed the LIP starting from (r,c)
                # Return the length of the path that we may append
                return dp[(r,c)]

            # Default
            res = 1
            
            # INDUCTIVE STEP

            # We store every direction
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr, dc in directions:
                # We try to go in this direction, and maximise res
                res = max(res, 1+dfs(r+dr,c+dc,matrix[r][c]))
            
            # Store in dp
            dp[(r,c)] = res

            # Return the path in dp
            return res

        # Simple default: LIP is 0
        lip = 0
        for r in range(ROWS):
            for c in range(COLS):
                # Set the previous to -1 as matrix 
                # holds non-negative values
                lip = max(lip,dfs(r,c,-1))
        
        return lip


if __name__ == "__main__":
    sol = Solution()
    matrix = [[5,5,3],[2,3,6],[1,1,1]]
    print(sol.longestIncreasingPath(matrix)) # 4
    matrix = [[1,2,3],[2,1,4],[7,6,5]]
    print(sol.longestIncreasingPath(matrix)) # 7
