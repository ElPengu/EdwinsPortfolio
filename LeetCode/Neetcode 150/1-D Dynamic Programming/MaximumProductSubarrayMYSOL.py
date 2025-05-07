from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        - Find subarray with the largest product within
        the array and return that product
        - Subarray: contiguous non-empty sequence of 
        elements within an array

        - As a base case, nums[N-1] is the largest product
        STARTING at N-1
        - Inductively, the largest from i may be 
        nums[i]*DP[i+1]
        - It should be
        
        - WHAT ABOUT NEGATIVES?!
        - [-1000,3,4,-1000] would return 7, but we want 7e6 as
        the answer

        - Hmmm
        - Okay, if we see a zero at i then we know that DP[i] is 0
        - We could have two running totals
        - DP[i] = (positives, negatives)
        
        - I FEEL SO CLOSE!
        
        - res = nums[0]
        - DP[N] = (1,1)
        - IF DP[i] == 0: DP[i] = (0,0)
        - ELSE: 
        -> IF DP[i] > 0: DP[i] = (nums[i]*DP[i+1][0], nums[i]*DP[i+1][1])
        -> ELSE: DP[i] = (MAX(DP[i+1][0],DP[i+1][1],nums[i]), nums[i]*DP[i+1][1])
        - res = MAX(res, DP[i][0], DP[i][1])
        - RETURN res

        - Close...

        '''

        # Get the number of items
        N = len(nums)

        # Initialise res
        res = nums[0]

        # Set DP
        dp = {}
        # 1 is multiplicative identity
        dp[N] = (1,1)

        for i in range(N-1,-1,-1):
            if nums[i] == 0:
                # Start new subarray!
                dp[i] = (0,0)
            else:
                if nums[i] > 0:
                    # POSITIVE CASE
                    dp[i] = (nums[i]*dp[i+1][0], nums[i]*dp[i+1][1])
                else:
                    # NEGATIVE CASE
                    dp[i] = (max(dp[i+1][0],dp[i+1][1],nums[i]), nums[i]*dp[i+1][1])
        
            res = max(res, dp[i][0],dp[i][1])
    
        return res
                             

        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,-3,4]
    print(sol.maxProduct(nums)) # 4
    nums = [-2,-1]
    print(sol.maxProduct(nums)) # 2