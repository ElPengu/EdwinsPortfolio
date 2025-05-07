from typing import List

class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        - Array of numbers
        - Give length of the longest strictly 
        increasing subsequence
        - Subsequence: Sequence derived by deleting
        at least zero elements but not changing 
        the order

        - Assume that we have the longest increasing
        subsequence ENDING at index i
        - How about for index i+1?
        - Hm

        - Okay, recursively we'd want to check every 
        possible sequence
        - Like, if we selected every element, then if 
        we ignored one element, then if we ignored two
        elements
        - Specifically, we'd go through every index and 
        consider the longest subsequence INCLUDING index i
        vs NOT INCLUDING index i
        - This involves repeated work as multiple branches
        would include or not include index i
        - Within the recursion we'd blindly check the length
        of the longest strictly increasing SUBSTRING

        - What if at every index we knew the longest subsequence
        up to it? How could we use our recursion intuition here?
        - You'd only reduce to O(n2)
        - At index i you'd check every index UP TO i
        - DP[i] = MAX(DP[j]+1, DP[i]) s.t. j < i AND nums[j]<nums[i]
        
        - Done in under 20 minutes >:^)
        - URA!
        '''

        # Store our result
        res = 0

        # Set up our cache, assume all subseq. of 
        # max length 1
        dp = [1]*(len(nums))

        # BASE CASE: first element is subseq. of 
        # length 1

        # INDUCTIVE STEP
        for i in range(len(nums)):
            # Check every index in nums
            for j in range(i):
                # Check every index up to BUT NOT 
                # INCLUDING i
                if (nums[j]<nums[i]):
                    # We strictly increase from 
                    # index j

                    # Update dp to store at i the 
                    # maximum length of subseq if 
                    # we continue from index j
                    dp[i] = max(dp[j]+1, dp[i]) 
            
            # Update res
            res = max(res, dp[i])

        print(dp)
        return res

if __name__ == "__main__":
    sol = Solution()
    nums = [9,1,4,2,3,3,7]
    print(sol.lengthOfLIS(nums)) # 4
    nums = [0,3,1,3,2,3]
    print(sol.lengthOfLIS(nums)) # 4