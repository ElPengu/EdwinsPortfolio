from typing import List
import math

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        '''
        - Array of integers nums
        - Find subarray with the largest sum
        - Subarray: contiguous non-empty sequency of elements

        - BRUTE FORCE
        - Iterate over every index of i, for each i 
        compute every index j>i, and for each j 
        compute the sum from i to j
        - O(n^3) time
        -> n^2 <- iterating every j for every i
        -> n <- O(1) for adding every value from 
        index i to j

        - QUADRATIC SOLUTION
        - Instead of manually computing the sum 
        from i to j, let's save the sum in a cache 
        dp
        - So we know that dp[(i,i)] = nums[i]
        - Within the j loop, check if we have stored 
        in the cache for (i,j)
        - If not, the sum is dp[(i,j-1)]+nums[j]
        - O(n^2) time
        -> n^2 <- iterating every j for every i
        -> 1 <- for adding a single value every 
        time you evaluate j 

        - LINEAR SOLUTION
        - Do we need to start at EVERY index i? 
        - Not really, we can use a sliding window 
        approach
        - You always are in two states
        - STATE 1: The prefix to the end index is 
        negative, so you should start a new subarray 
        by setting the end index to the start index
        - STATE 2: The prefix to the end index is 
        positive, so you should continue with this 
        subarray and shift the end index up
        - Consider [-2,1,-3,4,-1]
        - We start at -2, so curSum = -2
        -> Maximum subarray: [-2]
        - We consider 1, curSum=curSum+1
        - curSum=-1, but curEnd = 1
        - curEnd>curSum, so we can maximise curSum 
        by chopping off the prefix to curEnd
        - curSum = 1, curEnd = 1
        - We consider -3, curSum+=-3
        - curSum = -2, curEnd=-3
        - curEnd<=curSum, so we can maximise curSum 
        by NOT chopping off the prefix to curEnd
        - curSum = -2, curEnd = -3
        - We consider 4, curSum+=4
        - curSum=2, curEnd=4
        - curSum>curEnd, so we can maximise curSum 
        by chopping off the prefix to curEnd
        - curSum=4, curEnd=4
        - We consider -1, curSum+=-1
        - curSum=3, curEnd=-1
        - curEnd<=curSum, so we can maximise curSum 
        by NOT chopping off the prefix to curEnd
        - We ended up with curSum=3 though?!
        - No worries, we keep a global maxSum 
        variable that we set to max(maxSum,curSum) 
        every time we update curSum
        - O(n) time
        '''

        # Assume that maximum sum is the first 
        # element in nums
        maxSub = nums[0]

        # Initialise curSum to 0
        curSum = 0

        for n in nums:
            if curSum < 0:
                # We have a negative prefix, so 
                # we start counting again from this 
                # index
                curSum = 0
            # We add whatever num we are at to 
            # maximise the current sum
            curSum += n

            # Update the maximum sum of a subarray 
            # seen so far 
            maxSub = max(maxSub, curSum)
        
        return maxSub


if __name__ == "__main__":
    sol = Solution()
    nums = [2,-3,4,-2,2,1,-1,4]
    print(sol.maxSubArray(nums)) # 8
    nums = [-1]
    print(sol.maxSubArray(nums)) # -1