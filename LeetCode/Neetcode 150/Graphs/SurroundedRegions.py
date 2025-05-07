from typing import List

class Solution:

    def solve(self, board: List[List[str]]):
        # Pretty interesting solution and it is well
        # worth your time
        # 
        # 'Os' that are 4-directionally surrounded 
        # by 'X's must be flipped to 'O's
        # Naturally, border regions cannot be 
        # surrounded
        # 
        # A clever way of doing this uses something 
        # that is called 'reverse thinking'
        # Original problem: capture surrounded 
        # regions
        # Reverse thinking problem: Capture everything
        # EXCEPT unsurrounded regions
        # How does this apply here?
        # If we are in a border region then we know
        # that we are unsurrounded
        # In the program
        # (DFS) PHASE 1: Capture unsurrounded regions
        # O->T
        # > We start by marking border 'O's and change 
        # it to a temporary variable T and do DFS 
        # to which turns every neighbouring 'O' to T
        # PHASE 2: Capture unsurrounded regions
        # O->X
        # > Now we'll have all unsorrounded regions
        # > The next portion is to search the board 
        # for O's. These O's are NOT UNSURROUNDED, 
        # i.e. surrounded, so we turn each one into 
        # 'X'.
        # PHASE 3: Uncapture unsurrounded regions
        # T->O
        # > Finally convert T's back to 'O's
        # O(n*m) time

        # Get the number of rows and columns
        ROWS, COLS = len(board), len(board[0])

        # DFS
        def capture(r,c):
            if (r<0 or c<0 or r == ROWS or c == COLS 
                or board[r][c]!="O"):
                # We are out of bounds or have not
                # found an 'O'
                return
            # We are at an 'O'
            
            # Change it to temp var T
            board[r][c] = "T"
            # Explore in four directions
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)

        # (DFS) PHASE 1: Capture unsurrounded regions
        # O->T
        for r in range(ROWS):
            for c in range(ROWS):
                # We only run dfs on border cells
                if (board[r][c] and
                    r in [0, ROWS-1] and
                    c in [0, COLS-1]):
                    # Capture this region
                    capture(r,c)
                

        # PHASE 2: Capture unsurrounded regions
        # O->X
        for r in range(ROWS):
            for c in range(COLS):
                # All remaining 'O's are unsurrounded
                # Convert to 'X's
                if board[r][c] == "O":
                    board[r][c] = "X"

        # PHASE 3: Uncapture unsurrounded regions
        # T->O
        for r in range(ROWS):
            for c in range(COLS):
                # All 'T's are unsurrounded 'O's
                # Convert to 'O's
                if board[r][c] == "T":
                    board[r][c] = "O"

        return board


if __name__ == "__main__":
    sol = Solution()

    board = [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","O","O","X"],
            ["X","X","X","O"]
            ]
    
    print(sol.solve(board)) 
    ''' 
    [
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","X","X","O"]
    ]
    '''