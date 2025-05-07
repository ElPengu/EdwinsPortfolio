from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
        - Given a square nxn matrix of integers 
        matrix, rotate by 90 degrees clockwise
        - You must rotate the matrix in place

        - The first problem is to understand what 
        we mean by rotating 90 degrees clockwise
        - Look at the matrix and rotate your head 
        90 degrees. That is how you should be 
        able to read the matrix after rotation

        - The challenge is moving values and saving
        - Consider matrix...
        - [[1,2,3],
        -  [4,5,6],
        -  [7,8,9]]
        - We want the matrix
        - [[7,4,1],
        -  [8,5,2],
        -  [9,6,3]]
        - Notice what happens when we try to rotate 
        just the 1
        - 1->3, 3->9, 9->7, 7->1
        - There is a sort of chain
        - How about the 2?
        - 2->6, 6->8, 8->4, 4->2
        - Huh, okay but the 5 stays in place!
        - Yes, but that is not a helpful way of 
        understanding the problem, how about we say 
        that 5->5, 5->5, 5->5, 5->5
        - Do you notice how we can create a square 
        for the moving elements, where each element 
        is at a point and goes down an edge to the 
        adjacent point?

        - O(n^2) time <- to move each element
        - O(1) extra space <- we change the matrix 
        in place

        - Let's use an example with a 4x4 matrix
        - [[ 5, 1, 9,11],
        -  [ 2, 4, 8,10],
        -  [13, 3, 6, 7],
        -  [15,14,12,16]]
        - We will always rotate the outer most 
        square first
        - We use some pointers to define our square
        - Initialise L, R = 0, 3
        -> Left-most boundary, right-most boundary 
        - Initialise T, B = 0, 3
        -> Top-most boundary, bottom-most boundary
        - We start at the top-left, so we want 
        5->10, 10->16, 16->15, 15->5
        - We want to do this for the entire row 
        though
        - So we also want 1->10, 10->12, 12->13, 
        13->1
        - If you notice something, for this 
        adjacent element we are offset by 1
        -> From the left, top, right, and bottom 
        in that order
        - The same rule goes for the adjacent 
        element after that, and so forth
        - Okay, let's say we do this for the entire 
        square
        - How do you know that you have done the 
        entire square?
        - Well, in the example you only start from 
        5, 1, 9 in the outer layer. Not 11 because 
        that is where the 5 in the top-left goes
        - So we must start with an offset of i=0, 
        and then repeat the rotations until we have 
        an offset of r-l-1 rotations (start from left 
        to right, subtract 1 for the right)
        - We still may have the inner layer
        - Therefore, after evaluating a square you 
        shift each pointer inwards
        - L, R = L+1, R-1
        - T, B = T+1, B-1
        - Finally, how do we know when we have 
        stopped?
        - We can be certain that when L, R or T,B 
        cross over (L>R, T>B) then we have finished 
        evaluating our squares
        - But okay, let's go back to 5->11, 11->16, 
        16->15, 15->5
        - We move 5 to 11, and save the 11 in a 
        temporary variable. Then move the 11 to 
        the 16, and save the 16 in a temp variable, 
        and so on
        - This is fine, but what if I told you that 
        there is a slightly better way that makes 
        writing the code easier? With one temporary 
        variable instead of 4.
        - How about we do 15->5 first? And then 
        save the 5 in a temporary variable
        - We notice a space where 15 used to be, so 
        we can do 16->11
        - Now there is a space where the 16 used to 
        be, so 15->16
        - Finally, we fill where 15 used to be with 
        5, stored in our temporary variable 

        - Note that with i being the offset, we 
        must be careful about the value that we 
        apply i to
        - Top-left: Offset the left by +i
        - Top-right: Offset the bottom by +i
        - Bottom-right: Offset the right by -1
        - Bottom-left: Offset the bottom by -i
        '''

        # Set our left and right pointers
        l, r = 0, len(matrix[0])-1

        while l < r:
            # Run our rotation

            for i in range(r-l):
                # We rotate each element from top 
                # left up to JUST BEFORE the top 
                # right 

                # Note that i is the offset. We 
                # must be careful about the value 
                # that we apply the offset to
                # Top-left: Offset the left by i
                # Top-right: Offset the bottom by i
                # Bottom-right: Offset the right by 
                # -1
                # Bottom-left: Offset the bottom by 
                # -i

                # Set our top and bottom variables
                top, bottom = l, r

                # Save the top left
                topLeft = matrix[top][l+i]

                # Move the bottom left into top 
                # left
                matrix[top][l+i] = matrix[bottom-i][l]

                # Move the bottom right into bottom 
                # left
                matrix[bottom-i][l] = matrix[bottom][r-i] 

                # Move the top right into bottom 
                # right
                matrix[bottom][r-i] = matrix[top+i][r]

                # Move the ORIGINAL top left into 
                # top 
                matrix[top+i][r] = topLeft 
            
            # Update left and right pointers
            l, r = l+1, r-1
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