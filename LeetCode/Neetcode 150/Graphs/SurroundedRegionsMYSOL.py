from typing import List

class Solution:

    def solve(self, board: List[List[str]]):
        # Four-directionally connected group of 'O's 
        # surrounded by 'X's is SURROUNDED
        # An 'O' on the border cannot be surrounded
        # Change SURROUNDED 'O's to X's
        # 
        # What is an intuitive way of understanding that
        # a group of 'O's is surrounded?
        # If from one 'O', you can explore in four directions
        # and EACH of those four directions finds an X, 
        # it is surrouded, as the example confirms
        # 
        # This can be solved with BFS
        # Loop through the board until you find an 'O'
        # From this 'O' we do BFS in four directions, if 
        # we see an 'O' in ...
        # Hold on
        # This seems to be better solved with DFS
        # The real question: From the current 'O' we are at, 
        # search as deep as you can UP, then DOWN, then LEFT, 
        # then RIGHT. If every search tree tells us "yeah, we 
        # found an 'X'" then change this current 'O' in place!
        # Easy!
        # We'll use recursive DFS

        # Find the number of rows and columns
        ROWS, COLS = len(board), len(board[0])

        # We need to maintain a set of locations 
        # that we have VISITED
        visited = set()

        # Our handy recursive DFS function
        def backtrack(row, col):
            # We take in the row and col of the character
            # in the matrix

            visited.add((row,col))

            if row < 0 or col < 0 or row >= ROWS or col >= COLS:
                # We are out of bounds and have not seen any 
                # 'X's so far
                # So we return false
                return False 
            

            if board[row][col] == 'X':
                # Now we are at an 'X' so we return True
                return True
            
            # We certainly are at an 'O' given the problem definition
            
            
            # We explore in every UNVISITED location

            surrounded = True

            possibleLocations = [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]
            searchableLocations = []
            for i in range(len(searchableLocations)):
                if searchableLocations[i] not in visited:
                    searchableLocations.append(possibleLocations[i])

            for searchableLocation in searchableLocations:
                row = searchableLocation[0]
                col = searchableLocation[1]
                surrounded = surrounded and backtrack(row,col)

            if surrounded:
                # We have seen an X in every direction, so we are surrounded
                # We change from O to X
                board[row][col] = 'X'
                # Now we are at an 'X' so we return True
                return True
        
        # We loop over the board
        for row in range(ROWS):
            for col in range(COLS):
                if backtrack(row,col) == 'O':
                    # We are at an O

                    # The backtrack function will change all surrounded
                    # 'O's it finds to 'X'
                    backtrack(row,col)
        print("her")
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