from typing import List

class Solution:

    def exist(self, board: List[List[str]], word: str)->bool:

        # This is definitely a popular problem!
        # There is no super-efficient solution, we will rely
        # on back tracking
        # 
        # Intuitively: We start at every letter, until we find
        # the start of the word
        # Next we look at all the neighbours that we have NOT 
        # used already at this point until we find the second
        # letter of the word
        # Continue until you have found the word
        # 
        # We use a set to hold all the positions that we have 
        # seen
        # 
        # At any position we have four possible choices
        # > MOVE UP
        # > MOVE DOWN
        # > MOVE LEFT
        # > MOVE RIGHT
        # 
        # If we land on an out-of-bounds position, or we land 
        # on a SEEN position, or this letter is not the one 
        # that we are looking for (we can use a pointer for 
        # this) then we return false
        # Else, if we have evaluated the entire length of the 
        # word, we return true!
        # 
        # So really, we must return the OR for all possible 
        # choices. If we EVER get the word, True will dominate
        # 
        #
        # We will use recursive DFS
        # 
        # O(n*m*4^n) time
        # dfs <- 4^len(word) <- We make 4 choices at a time
        # 
        
        # Get the number of rows and columns
        ROWS, COLS = len(board), len(board[0])

        # We have a set of all positions that are currently 
        # within our path
        path = set()

        def dfs(r, c, i):
            # r <- row
            # c <- column
            # i <- index of the WORD that we are looking for

            if i == len(word):
                # We have found the word
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                word[i] != board[r][c] or
                (r,c) in path):
                # This is a FAT if statement, but it makes sense
                # CONDITION 1, 2
                # Row index < 0 or col index < 0, out of bounds
                # CONDITION 3, 4
                # Row index >= ROWS, col index >= ROWS, out 
                # of bounds
                # CONDITION 5
                # Word[i] != board[r][c], we are at a position 
                # with the letter that we are NOT looking for
                # CONDITION 6
                # (r,c) in path, we have already landed in this
                # position
                # 
                # ANY of these being the case means that we
                # are not happy
                return False
            
            # We add to the path the position that we are at
            path.add((r,c))

            # We look at ALL positions that we could move to
            # Move up
            res = dfs(r+1,c,i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            
            # We remove the position that we have considered from the 
            # path, just to clean up
            # Keep in mind that path is a global variable!
            path.remove((r,c))

        # Now we go through EVERY position in this grid
        for r in range(ROWS):
            for c in range(COLS):
                # We go from index 0
                if dfs(r,c,0):
                    return True
        # We have not found a word, so we return False
        return False

        pass

if __name__ == "__main__":
    sol = Solution()
    board = [["A","B","C","D"],  ["S","A","A","T"],  ["A","C","A","E"]]
    word = "BAT"
    print(sol.exist(board, word)) # false

