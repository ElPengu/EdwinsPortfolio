from typing import List

class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
        - Given an mxn matrix
        - If an element is 0, set its entire row 
        and column to 0s
        - You must update the matrix in-place

        - There are two interesting solutions, an 
        O(m+n) space solution and an O(1) space 
        solution. 
        - Both solutions are O(m*n) time for looping 
        over each element 

        - O(m+n) space solution
        - Problems
        - Find the locations of the zeroes
        - Store what the row or column index must 
        be for an element to be set to 0
        - Set all elements that must be 0 to be 0

        - Problem: Find the locations of the zeroes
        - Loop row,col over matrix
        - If matrix(row,col) == 0, then location 
        (row,col)

        - Problem: Store what the row or column 
        index must be for an element to be set 
        to 0
        - Array colArr with a mark if the column 
        must be zeroed
        - Array rowArr with a mark if the row 
        must be zeroed

        - Problem: Set all elements that must be 0 
        to be 0
        - Loop row, col over matrix
        - If row in rowArr or col in colArr, 
        matrix[row][col] = 0

        - O(m+n) space <- Every row and every column 
        may be marked
        - O(m*n) time <- Each row and column pair is 
        evaluated exactly twice


        - O(1) space solution
        - We modify the matrix in place
        
        - Problems
        - Find the locations of the zeroes
        - Storing which rows must be zeroed
        - Storing which columns must be zeroed
        - Ensuring that there is no overlap when 
        designating the rows and columns to be 
        zeroed
        - Updating the matrix by zeroing out the 
        relevant positions

        - Problem: Find the locations of the zeroes
        - Loop row,col over matrix
        - If matrix(row,col) == 0, then location 
        (row,col)
        
        - Problem: Storing which columns must be 
        zeroed
        - We modify the matrix so that every time 
        that we see a zero, we immediately go to 
        matrix[row][0]
        - matrix[row][0] = 0
        - Now matrix[row][0] points downwards to 
        the column that must be zeroed

        - Problem: Storing which rows must be 
        zeroed
        - We modify the matrix so that every time 
        that we see a zero, we immediately go to 
        matrix[0][col]
        - For all columns EXCEPT matrix[0][0] to 
        avoid overlapping with the column 
        designations   
        - matrix[0][col] = 0
        - Now matrix[0][col] points rightwards to 
        the row that must be zeroed 

        - Problem: Ensuring that there is no 
        overlap when designating the rows and 
        columns to be zeroed
        - We avoid this by NOT setting matrix[0][0] 
        when storing the rows that must be zeroed 
        - Instead, we have a separate variable
        - Let's call the separate variable FIRSTROW
        - When updating for row=0, set FIRSTROW=0


        - Problem: Updating the matrix by zeroing 
        out the relevant positions
        - Loop over row,col of the matrix EXCEPT 
        THE FIRST of each
        - When matrix[row][0] = 0 or matrix[0][col] 
        = 0, set matrix[row][col] = 0
        - matrix[0][0] points DOWNWARDS to the 
        column that must be zeroed, check this 
        condition
        - rowZero points RIGHTWARDS to the row that 
        must be zeroed, check this condition 

        - O(1) space <- Worst case you will use the 
        matrix and the extra FIRSTROW variable
        - O(n) time
        -> In the loop for designating columns to be 
        zeroed you make at most 1 update: 
        matrix[row][0] = 0
        -> In the loop for designating rows to be 
        zeroed you make at most 1 update: 
        matrix[0][col] = 0
        -> In the loop for updating the entire 
        matrix you make O(1) operations for each 
        row,col pair

        '''

        # O(1) memory solution

        # Get the rows and columns
        ROWS, COLS = len(matrix), len(matrix[0])

        # Extra variable for first row
        rowZero = False

        # Determine which rows/cols need to be 
        # zeroed
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # We have found a row and column 
                    # to be zero
                    
                    # Designate the COLUMN to be 
                    # zeroed
                    matrix[0][c] = 0

                    # Designate the ROW to be zeroed
                    if r > 0:
                        # Remember, we do NOT do 
                        # this for the first row!
                        matrix[r][0] = 0
                    else:
                        # r = 0
                        # Set the designated 
                        # variable to be True
                        rowZero = True

        # Update the matrix

        # Zero out all but the first row and first 
        # column
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if (matrix[0][c] == 0 or 
                    matrix[r][0] == 0 or
                    rowZero == True): 
                    # The row or column designates 
                    # this position to be zeroed!
                    matrix[r][c] = 0
        
        # Update the first column
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        # Update the first row
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

        
        
        return matrix

if __name__ == "__main__":
    sol = Solution()
    matrix = [
    [0,1],
    [1,0]
    ]
    print(sol.setZeroes(matrix)) # [[0,0],[0,0]]
    matrix = [
    [1,2,3],
    [4,0,5],
    [6,7,8]
    ]
    print(sol.setZeroes(matrix)) # [[1,0,3],[0,0,0],[6,0,8]]