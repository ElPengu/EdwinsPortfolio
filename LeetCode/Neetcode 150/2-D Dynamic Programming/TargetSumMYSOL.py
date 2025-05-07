from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        - We have integers in nums
        - We have an integer target
        - For each integer you may add OR subtract it to some total sum
        - Different ways that you can build the expression to reach 
        target?

        - IMMEDIATE APPROACH
        - All else being equal, you can add or subtract num at any point 
        of operations
        - We start at i = N with target t
        - You can choose to add or subtract at i = N-1
        - For either operation you update target t
        - At index i...
        - You see the number of different ways you can reach curTarget 
        through either choosing to add or subtract at index i, with 
        the remaining number of indices there

        - I kind of combined caching, DP, and DFS there

        - Let's tidy it up

        - What exactly are the subproblems
        - I know that we want to see what happens when we add or subtract 
        nums[i] to the sum of some operations on all indices after
        - I know this "happens" is the number of ways
        - What exactly is a way though?
        - Okay, at index i=0, the curTarget is target
        - Let's say we add nums[i]. Then what?
        - Well, if nums[i]+X=target, X=target-nums[i]
        - Hm...
        - At index i=1, GIVEN we added at i=0, curTarget=target-nums[i]
        - At index i=1, GIVEN we subtracted at i=0, 
        curTarget=target+nums[i]
        - What is the recurrence relation?
        - ways(i, OPERATION) = ways(i-1, NOT OPERATION)
        - FUCK, I am missing something here
        - My brain is fried 
        '''
        
        
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [2,2,2]
    target = 2
    print(sol.findTargetSumWays(nums, target)) # 3