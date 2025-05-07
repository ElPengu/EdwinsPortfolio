from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        - We have an NxM matrix
        - We want to return a list of the elements 
        in spiral order

        - Here is what spiral order looks like
        - [[1,2,3],
        -  [4,5,6],
        -  [7,8,9]]
        - It would read: 1,2,3,6,9,8,7,4,5

        - Let us design an algorithm to read the 
        matrix
        - From top left, we go all the way right, 
        then all the way down, then all the way 
        left, then up until just below the top left
        - That is for one layer
        - Now we move in a layer and repeat

        - How do we know top, left, right, bottom, 
        and the layer?
        - We can use pointers!
        - top, bottom = 0, len(matrix)
        -> Not len(matrix)-1 to make the code 
        easier 
        - left, right = 0, len(matrix[0])
        -> Not len(matrix[0])-1 to make the code 
        easier 
        
        - Let us look at an example
        - [[1,2,3,4],
        -  [5,6,7,8],
        -  [9,10,11,12]]
        - left, right = 0, 4 (not 3)
        - top = 0, bottom = 3 (not 2)
        - Set output array
        - Go from top left until we are about to 
        hit our right boundary
        - We read 1,2,3,4
        -> output = [1,2,3,4]
        - Now we don't need the top row, so we 
        set top = 1
        - Now we go down
        - 8,12 
        -> output = [1,2,3,4,8,12]
        - Now we hit our bottom boundary, so we go 
        left
        - We don't need our right column, so we 
        set right = 3
        - We read 11,10
        -> output = [1,2,3,4,8,12,11,10]
        - We DON'T read 9 because we go until we hit 
        the left boundary, just for consistency
        - Now we don't need our bottom row, so we 
        set bottom = 2
        - Now we start going up until we hit our 
        top boundary
        - We read 9, 5
        -> output = [1,2,3,4,8,12,11,10]
        - Now we don't need our left column, so we 
        set left = 1
        - Now we start going right until we hit our 
        right boundary
        - We read 6, 7
        -> output = [1,2,3,4,8,12,11,10]
        - Now we don't need our top row, so we 
        set top = 2
        - Now top > bottom, so we stop!

        - Our while condition: top<bottom and 
        left<right  
        - Note that we must check this half-way in 
        the code because we update top AND bottom 
        in one loop, ditto for left AND right

        - Here is the general solution
        - We set left, right = 0, len(matrix[0])
        - We set top, bottom = 0, len(matrix)
        - Hence the right and bottom pointers 
        are BOUNDARIES, as are left and top
        - We continue while left < right and top < 
        bottom
        - We start at top left
        - We read UNTIL we FINISH at top-right
        - We have finished reading the top row, so 
        we shift top pointer down
        - Now we are at top-right
        - We start at 1 step BELOW top-right and 
        read until we FINISH at bottom-right
        - We have finished reading right column, so 
        we shift right pointer in
        - WAIT
        - Now that we have updated top and right, 
        the condition may be broken
        - Break if the condition is broken 
        - Now we are at bottom-right
        - We start 1 step BEHIND bottom-right and 
        read until we FINISH at bottom-left
        - We have finished reading the bottom row, 
        so we shift bottom pointer up
        - Now we are at bottom-left
        - We start 1 step ABOVE bottom-left and we 
        read until we FINISH at NEW top-left, not 
        old top-left
        - Be careful about the pointers here, as you 
        shift the boundaries in you have to account 
        for this so that you start and finish EXACTLY 
        where you want
        - We have finished reading left column, so 
        we shift left pointer out

        - O(nm) time <- Read n rows, n columns
        - O(1) extra space <- we don't count the 
        output as extra memory
        '''

        res = []

        # Set pointers
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # Get every value in the top row
            for i in range(left, right):
                # We go from the left to the column 
                # BEHIND the right boundary
                # Hence we land on the top right
                res.append(matrix[top][i])
            # Shift down a row
            top+=1

            # Get every value in the right column
            for i in range(top, bottom):
                # We go from the top to the row 
                # ABOVE the bottom boundary
                # Hence we land on the bottom-right

                # Note that right and left are out 
                # of bounds!
                res.append(matrix[i][right-1])
            # Shift outer column inwards
            right-=1

            if not (left<right and top<bottom):
                # Why do we use this condition here?

                # Every loop we increment top and 
                # left, and decrement bottom and 
                # right
                # Therefore, they may cross over 
                # after we update top and right, 
                # and then cross over EVEN MORE 
                # after we update bottom and left
                
                # This essentially recognises that 
                # whilst the while condition could 
                # break at the end, it could also 
                # break halfway through!
                break

            # Get every value in the bottom row
            for i in range(right-1, left-1, -1):
                # We start at the bottom right
                # We don't want to read the 
                # bottom-right again
                # We start BEHIND the bottom right 
                # and read until the bottom left

                res.append(matrix[bottom-1][i])
            # Shift the bottom row upwards
            bottom-=1

            # Get every remaining value in the 
            # left column
            for i in range(bottom-1, top-1, -1):
                # We start at the bottom left
                # We don't want to read the 
                # bottom-left again
                # We start ABOVE the bottom 
                # boundary and read until top left
                # But don't worry! top-left is 
                # different now!
                # The top boundary is now 1 step 
                # below what it was, so we must 
                # finish exactly there 

                res.append(matrix[i][left])
            
            # Shift left column inwards
            left+=1

        return res

if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2],[3,4]]
    print(sol.spiralOrder(matrix)) #[1,2,4,3]
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(sol.spiralOrder(matrix)) #[1,2,3,6,9,8,7,4,5]
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(sol.spiralOrder(matrix)) #[1,2,3,4,8,12,11,10,9,5,6,7]