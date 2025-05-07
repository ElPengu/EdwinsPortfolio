from typing import List

class Solution:

    def searchMatrix(self, matrix: List[List[int]], target:int) -> bool:
        # 
        # We get the specific row by checking both the 
        # first and final element in a list and doing 
        # binary search. 
        # We know that if the first element is greater 
        # than target then that row and all before it
        # do NOT have the solution.
        # If the final element is lesser than target then 
        # that row and all after it do NOT have the solution
        # Past these two preconditions, we know that the #
        # element must either be in this row, or not in 
        # the matrix
        # 
        # We use completely normal binary search on the 
        # target row

        # Let's store the dimensions of the matrix
        ROWS, COLS = len(matrix), len(matrix[0])

        #Set top and bottom rows to search
        top, bot = 0, ROWS - 1
        while top <= bot:
            #Compute middle row
            row = bot + ((top-bot)//2)

            if target > matrix[row][-1]:
                top = row+1
            elif target < matrix[row][0]:
                bot = row-1
            else:
                #If this is the case, we are in 
                # the correct row
                break
        
        # If the while condition is now false, 
        # we know that the target is not in here
        if not (top <= bot):
            return False

        row = (top+bot)//2
        l, r = 0, COLS-1
        while l<=r:
            m = l + ((r-l)//2)
            if target > matrix[row][m]:
                l = m+1
            elif target < matrix[row][m]:
                r = m-1
            else:
                return True
            
        #If we get here, not present!
        return False
            

        pass


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    target = 10
    print(sol.searchMatrix(matrix, target)) # true
    matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    target = 15
    print(sol.searchMatrix(matrix, target)) # false