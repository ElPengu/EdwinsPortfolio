from typing import List

class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        '''
        - We have an array of POSITIVE integers
        - Can we PARTITION into TWO subsets where 
        both have the same sum

        - RECURSIVE APPROACH
        - Two branches for each num. Whether it is in 
        subset1 or subset2
        - Repeated work. Consider nums[N-1] will be 
        checked for being in subset2 for both nums[0]
        being in subset1 and not being in subset1

        - CACHE APPROACH
        - The base case is that both subsets are empty
        - Let's say DP[N] = TRUE to represent this
        - We move to N-1
        - Can we partition N-1? Never, because it is 
        defined to be never 0
        - Set DP[N-1] = FALSE
        - I think we need more information though
        - Let's set DP[N] = (0,0)
        - DP[N-1] = (nums[N-1],0)
        - Move to DP[N-2]
        - Do we greedily put nums[N-2] in a subset s.t. 
        we balance both subsets?
        - We'd run into an issue like 
        -> [5,2,1,6]->([6],[1,2,5])
        - When we want
        -> [5,2,1,6]->([6,1],[2,5])

        - Hmmm

        - You could blow up space complexity to N2
        - Set DP->[[SUBSET1,SUBSET2], [SUBSET1,SUBSET2]]
        - Start at final index
        - Add index to subset1 at 0, subset2 at 1
        - Continue all the way down
        - Check the sum of both when you get to 0

        
        - Pretty exhausted for writing this out, let's see if it 
        does what I want

        - EXAMPLE
        -> [5,2,1,6]
        -> i=3
        -> DP[3] = [[6],[]],[[],[6]]
        -> DP[2] = [[6,1],[]], [[1],[6]]
        -> DP[1] = [[6,1,2],[]], 

        - Wait no, FUCKKK
        
        '''



        pass

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4]
    print(sol.canPartition(nums)) # True
    nums = [1,2,3,4,5]
    print(sol.canPartition(nums)) # False
