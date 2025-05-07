from typing import List

class Solution:

    def solveNQueens(self, n: int)-> List[List[str]]:
        # The only hard part is implementing the code
        # 
        # Let us start at the first row with an empty
        # 4x4 board
        # We could place a single queen on the first, 
        # second, third, or fourth position
        # On the second row, we can place the queen 
        # on a *different* column.
        # So we need to keep track of the columns used
        # We also cannot place the queen on any 
        # positive or negative diagonals that the first 
        # queen could be placed in
        # This all indicates that we must keep track of
        # columns = set
        # positive diagonals = set
        # negative diagonals = set
        #  
        # How do we keep track of positive and negative
        # diagonals?
        # 
        # Henceforth we will define a board as having (0,0)
        # at the top left, and rows increase DOWNWARDS and
        # columns increase RIGHTWARDS
        # 
        # Negative diagonals
        # Let us start at (0,0)
        # The negative diagonal goes [(0,0),(1,1),(2,2),...]
        # Notice something?
        # row-column is constant!
        # So if we see that position row-col in negative diagonals,
        # we have an invalid placement!
        # By nature of negative diagonals, you move down 1 and right
        # 1. 
        # I.e., you increment the row and column.  
        # This is why the property holds for negative diagonals
        #  
        # Positive diagonals
        # Let us start at (3,0)
        # The positive diagonal goes [(3,0),(2,1),(1,2),(3,0)]
        # The row decrements and the column increments
        # Therefore, the SUM of row and column remains the same
        # 
        # So our decision tree is to try the queen on all the 
        # positions for the first row, such that the position
        # is not in the column, positive diagonals, or negative
        # diagonals sets
        # We repeat this for subsequent rows
        
        # Define sets for columns, positive diagonals, and negative 
        # diagonals
        col = set()
        posDiag = set() # row+col
        negDiag = set() # row-col

        res = []

        # Initialise the board with an array of
        # arrays
        board = [["."]*n for i in range(n)]

        def backtrack(r):
            # We go row by row

            # Base case: All rows considered
            if r == n:
                # Make a "copy" of this board where each row is joined
                # together
                copy = ["".join(row) for row in board]
                res.append(copy)

            # Try every position, which ones can we add to?
            for c in range(n):
                #Try each column
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    # This column, positive diagona, or negative 
                    # diagonal is already being used
                    continue

                # Update the col, diagonal stuff
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                # Replace position with Queen
                board[r][c] = "Q"

                # Move to the next row
                backtrack(r+1)

                # Unroll the col, diagonal stuff
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                # Replace Queen with dot
                board[r][c] = "."
        
        # Call on the first row
        backtrack(0)

        return res

if __name__ == "__main__":
    sol = Solution()
    n = 4
    print(sol.solveNQueens(n)) # [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    n = 1
    print(sol.solveNQueens(n)) # [["Q"]]

