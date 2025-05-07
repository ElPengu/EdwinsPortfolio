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

        - RECURSION
        - Okay, recursively we'd want to check every 
        possible sequence
        - Like, if we selected every element, then if 
        we ignored one element, then if we ignored two
        elements, etc.
        - Specifically, we'd go through every index and 
        consider the longest subsequence INCLUDING index i
        vs NOT INCLUDING index i
        - This involves repeated work as multiple branches
        would include or not include index i
        - Within the recursion we'd blindly check the length
        of the longest strictly increasing SUBSTRING

        - CACHE
        - What if at every index we knew the longest subsequence
        up to it? How could we use our recursion intuition here?
        - You'd only reduce to O(n2)
        - At index i you'd check every index AFTER i
        - BASE CASE: DP[N-1] = 1
        - DP[i] = MAX(DP[j]+1, DP[i]) s.t. i < j AND nums[i]<nums[j]
        
        - Done in under 20 minutes >:^)
        - URA!
        '''

        # BASE CASE
        # We create a cache LIS, assuming every LIS is 1
        LIS = [1]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            # We loop backwards

            for j in range(i+1,len(nums)):
                # We check every index j AFTER i

                if nums[i] < nums[j]:
                    # LIS starting at i through j can be formed

                    # Update LIS accordingly
                    LIS[i] = max(LIS[i],1+LIS[j])
        
        # Return the maximum
        return max(LIS)


if __name__ == "__main__":
    sol = Solution()
    nums = [9,1,4,2,3,3,7]
    print(sol.lengthOfLIS(nums)) # 4
    nums = [0,3,1,3,2,3]
    print(sol.lengthOfLIS(nums)) # 4