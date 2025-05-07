from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        - We have an NxN matrix
        - We want to return a list of the elements 
        in spiral order

        - From the examples, it seems that you read 
        from the top left to top right to bottom 
        bottom right to bottom left to JUST below 
        the top left, then you shift left and repeat

        - We can use some pointers to help 
        determine the boundaries of the current 
        square
        - top, bottom = 0, len(matrix)
        - left, right = 0, len(matrix[0])

        - How do we read a square in order?
        - We start at (top,left)
        - We increment until we get to (top,right)
        - We increment until we get to 
        (bottom,right)
        - We decrement until we get to (bottom,left)
        - We decrement until we get to (top-1,left)

        - What is a solution to read a square in 
        this order?
        - We read an element as matrix[i][j]
        - We set i=top, j=left
        - We increment j=left to j=right
        - We increment i=top to i=bottom
        - We decrement j=right to j=left
        - We decrement i=bottom to i=top+1

        - How do we shift to the inner square?
        - After all rotations...
        - top, bottom = top+1, bottom-1
        - left, right = left+1, right-1

        - How do you know when to stop shifting 
        squares?
        - top>bottom or left>right


        - ARG,SO CLOSE. Middle one doesn't work 
        though!
        '''

        cache = {}

        # Set left, right pointers
        left, right = 0, len(matrix[0])-1
        # Set top, bottom pointers
        top, bottom = 0, len(matrix)-1

        while (top<=bottom or left <= right):
            

            # Continue until we have evaluated 
            # the entire square

            # Read the square
            i=top
            j=left
            while j < right:
                cache[(i,j)] = matrix[i][j]
                print(matrix[i][j])
                j+=1
            while i < bottom:
                cache[(i,j)] = matrix[i][j]
                print(matrix[i][j])
                i+=1
            while j > left:
                cache[(i,j)] = matrix[i][j]
                print(matrix[i][j])
                j-=1
            while i > top:
                cache[(i,j)] = matrix[i][j]
                print(matrix[i][j])
                i-=1
            # Go to just below the top left
            i+=1
            if (i,j) not in cache:
                cache[(i,j)] = matrix[i][j] 
                print(matrix[i][j])
            top, bottom = top+1, bottom-1
            left, right = left+1, right-1

if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2],[3,4]]
    print(sol.spiralOrder(matrix)) #[1,2,4,3]
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(sol.spiralOrder(matrix)) #[1,2,3,6,9,8,7,4,5]
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(sol.spiralOrder(matrix)) #[1,2,3,4,8,12,11,10,9,5,6,7]