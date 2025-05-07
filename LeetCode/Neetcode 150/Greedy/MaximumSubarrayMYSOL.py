from typing import List
import math

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        '''
        - Array of integers nums
        - Find subarray with the largest sum
        - Subarray: contiguous non-empty sequency of elements
        
        - The subarray could start and end at any indices i,j 
        where j>=i
        - You could start at every i index, and loop up to every 
        possible j index and store i and j each time some sum 
        variable is maximised

        - To bring this down to two choices, given index i you 
        ask yourself: do you want to STOP at index j or not?
        - If you stop at index j, then you check the sum
        - Otherwise you shift index j up
        
        - Let N = size(nums)
        - If i and j point to index 0, we start and end at index 0
        - If i and j point to index N-1, we start and end at index 
        N-1
        
        - Let's take a step back
        - In a top-down memoization solution, we hold cache dp
        - dp[(i,j)] = sum starting at i and finishing at j
        - We can start at (0,0)
        - We iterate j until N-1, then we set i+=1, j=i
        - Once i=N-1, j=N-1, we have checked every possibility
        - We can hold globalI, globalJ which update when maximumSum 
        updates
        
        '''

        # Set up cache
        dp = {}

        # Size of nums
        N = len(nums)

        # Store the sum whenever i=j
        for i in range(N):
            dp[(i,i)] = nums[i]

        # We hold a global maximum sum
        # Initialise to value at start index
        maximumSum = nums[0]

        def dfs(i, maxSum):

            # i: Start index that we are investigating

            # BASE CASES
            if i == N:
                # No more indices to check!
                return maxSum

            # Check over every index from i to N-1
            for j in range(i, N):
                if (i,j) in dp:
                    # If we are at i=j then we have already stored it
                    maxSum = max(dp[(i,j)], maxSum)
                else:
                    # We use dp to compute the sum up to j and update 
                    # dp to store for i up to j
                    dp[(i,j)] = dp[(i,j-1)]+nums[j]

                    maxSum = max(dp[(i,j)], maxSum)

            return maxSum
        # Call dfs on every index in nums
        for i in range(N):
            maximumSum = max(dfs(i, maximumSum), maximumSum)

        # Return maximum sum
        return maximumSum

if __name__ == "__main__":
    sol = Solution()
    nums = [2,-3,4,-2,2,1,-1,4]
    print(sol.maxSubArray(nums)) # 8
    nums = [-1]
    print(sol.maxSubArray(nums)) # -1