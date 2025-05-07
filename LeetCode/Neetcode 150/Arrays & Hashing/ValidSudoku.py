from typing import List
from collections import defaultdict

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Note: 9x9 Sudoku board
        # Loop over every column
        #For each column, add elements to a hash set
        #Return false if you try to add an element already 
        #in the hash set
        #Same idea for rows
        #Same idea for the nine sub-boxes

        #1. Loop over every column <- O(1)
        for i in range(9):
            #Create a hash set
            currColumnSet = set()
            #Add column entries <- O(1)
            for row in board:
                #Do not add a dot
                if row[i] != ".":
                    if row[i] in currColumnSet:
                        #Repeat found
                        return False
                    else:
                        #Add to set
                        currColumnSet.add(row[i])
        #2. Loop over every row
        for i in range(9):
            #Create a hash set
            currRowSet = set()
            #Select row to inspect
            row = board[i]
            #Iterate over entries in row
            for entry in row:
                if entry != ".":
                    #Do not add a dot
                    if entry in currRowSet:
                        #Repeat found
                        return False
                    else:
                        #Add to set
                        currRowSet.add(entry)
                    
        #3. Loop over each 3x3 box
        #Create a hash map (i,j)->set()
        #i->{0,1,2}, j->{0,1,2}
        #Loop over every entry of the grid
        #Due to how a box is defined, 
        #we can use floor division 3
        #Consider [2,5]->[0,1]
        #So each of the coordinates will map
        #to the same square!
        
        #Hash map as defined
        myMap = {}
        for i in range(3):
            for j in range(3):
                myMap[(i,j)] = set()

        #Now we check every entry
        for i in range(9):
            for j in range(9):
                print(myMap)
                #Use floor division to find the key
                key = (i//3,j//3)
                #Now check if this is a dot
                if board[i][j] != '.':
                    #Check if it has been checked or not!
                    if board[i][j] in myMap[key]:
                        #Duplicate found!
                        return False
                    else:
                        #Add to the set
                        myMap[key].add(board[i][j])
            

        return True


if __name__ == "__main__":
    sol = Solution()
    board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
    print(sol.isValidSudoku(board)) # True
    board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
    print(sol.isValidSudoku(board)) # False 