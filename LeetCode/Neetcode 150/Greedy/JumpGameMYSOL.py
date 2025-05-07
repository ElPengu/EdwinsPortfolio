from typing import List

class Solution:

    def canJump(self, nums: List[int]) -> bool:

        '''
        - nums[i] <- maximum jump length at that position
        - Return True if you can reach the last index from 
        0

        - At any index you can choose to jump up to the 
        maximum length
        - A different way of thinking: at every index there 
        are some spots that you can land at

        - Create a cache dp
        - From i, evaluate j=0,...,nums[j]
        - If i == N-1, return TRUE
        - If (i,j) in dp return dp[(i,j)]
        - Store dp[(i,j)] = dfs(i)
        '''

        # Cache dp
        # i: Start index
        # j: Jump value
        dp = {}

        # Store size of nums
        N = len(nums)

        def dfs(i):
            # BASE CASES

            if i == N-1:
                # We have reached the end!
                return True
            if i > N-1:
                # We have jumped beyond the final index!
                return False
            # Assume that this branch fails
            res = False
            for j in range(0, nums[i]+1):
                
                # We must check every possible jump value
                # From 0 to the maximum jump length

                if j==0:
                    # To avoid recursive problems, we manually
                    # compute for j=0
                    # We cannot be at i=N-1, so we know that 
                    # jumping this much would fail
                    dp[(i,j)] = False
                
                if (i,j) in dp:
                    # We have already tried to jump this far
                    # Update res
                    res = res or dp[(i,j)]
                else:
                    # We must see what happens when we land 
                    # on this new spot i+j and store the 
                    # result in our cache
                    dp[(i,j)] = dfs(i+j)

                    # Update res
                    res = res or dp[(i,j)]
                
            
            # res tells us if this branch is valid or not
            return res
        
        # Start at 0, this returns whether we reach N-1
        return dfs(0)

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,0,1,0]
    print(sol.canJump(nums)) # True
    nums = [1,2,1,0,1]
    print(sol.canJump(nums)) # False