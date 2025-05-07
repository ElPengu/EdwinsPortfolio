from typing import List

class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
        - Given an mxn matrix
        - If an element is 0, set its entire row 
        and column to 0s
        - You must update the matrix in-place

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
        - Hash map rowSet for rows
        - Hash map colSet for cols

        - Problem: Set all elements that must be 0 
        to be 0
        - Loop row, col over matrix
        - If row in rowSet or col in colSet, 
        matrix[row][col] = 0
        '''

        # Store what the row or column index must 
        # be for an element to be set to 0
        rowSet = set()
        colSet = set()


        # Find the locations of the zeroes

        # Store row and cols
        ROWS, COLS = len(matrix), len(matrix[0])



        for row in range(ROWS):
            # Loop over every row

            for col in range(COLS):
                # Loop over every column

                if matrix[row][col] == 0:
                    # We have found a zero!

                    # Save the row and column
                    rowSet.add(row)
                    colSet.add(col)

        

        # Set all elements that must be 0 to be 0
        for row in range(ROWS):
            # Loop over every row

            for col in range(COLS):
                # Loop over every column

                if row in rowSet or col in colSet:
                    # We are in a row or column 
                    # that must only hold zeros

                    # Set the element here to be 
                    # 0
                    matrix[row][col] = 0

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