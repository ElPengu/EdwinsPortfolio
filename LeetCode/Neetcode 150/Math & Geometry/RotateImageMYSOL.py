from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
        - Given a square nxn matrix of integers 
        matrix, rotate by 90 degrees clockwise
        - You must rotate the matrix in place

        - Yay, matrices
        - If only I remembered my FM and maths for 
        CS content
        - Hm
        - What exactly do we want to happen?
        - What does it mean to rotate a matrix by 
        90 degrees?
        - From the examples, every column read 
        from bottom to top is now read left to 
        right
        - Let's think...

        - To rotate a matrix 90 degrees, we could 
        read the matrix by turning our head 90 
        degrees anti-clockwise
        - Doing so results in reading each column 
        from bottom to top!

        - Let's break this problem of reading the 
        columns bottom to top into subproblems
        
        - We need to know the number of columns to 
        read
        - Subproblem: find the number of columns to 
        read
        - We need to know which column to read at 
        which time
        - Subproblem: have a way of distinguising 
        each column by its order
        - We need to be able to store a column
        - Subproblem: store a column
        - We need to be able to read each column 
        from bottom to top
        - Subproblem: read a column from bottom to 
        top
        - We need to be able to change the matrix 
        in place
        - Subproblem: change THAT matrix and return 
        it

        - Subproblem: find the number of columns to 
        read
        - rows, cols = len(matrix), len(matrix[0])
        
        - Subproblem: have a way of distinguishing 
        each column by its order
        - Iterate from i=0 to i=cols-1
        - read matrix[j][i]
        
        - Subproblem: store a column
        - Store the column in an array

        - Wait, but we need to rotate the matrix 
        IN PLACE, are we not just creating a new 
        matrix by setting each array
        - Whatever, don't let perfection be the 
        enemy of progress

        - Subproblem: read a column from bottom to 
        top
        - Read from j=rows to j=0

        - Subproblem: change THAT matrix and return 
        it
        - After getting all the rows, read them 
        into the matrix
        '''

        # Subproblem: find the number of columns to 
        # read
        ROWS, COLS = len(matrix), len(matrix[0])

        newMatrix = []

        # Subproblem: have a way of distinguishing 
        # each column by its order
        for i in range(COLS):

            # Subproblem: store a column
            col = []

            # Subproblem: read a column from bottom 
            # to top
            for j in range(ROWS-1, -1, -1):
                col.append(matrix[j][i])

            newMatrix.append(col)
        
        # Subproblem: change THAT matrix and return 
        # it
        for i in range(ROWS):
            for j in range(COLS):
                matrix[i][j] = newMatrix[i][j]
        return matrix   

if __name__ == "__main__":
    sol = Solution()
    matrix = [
    [1,2],
    [3,4]
    ]
    print(sol.rotate(matrix)) # [[3,1],[4,2]]
    matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
    print(sol.rotate(matrix)) # [[7,4,1],[8,5,2],[9,6,3]]