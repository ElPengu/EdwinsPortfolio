from typing import List
from collections import defaultdict

class Solution:
    '''
    - This is a very good problem to learn 2D DP

    - We have integers in nums
    - We have an integer target
    - For each integer you may add OR subtract it to some total sum
    - Different ways that you can build the expression to reach 
    target?

    
    - BRUTE FORCE
    - Let's draw it out to understand
    - EXAMPLE [1,1,1], target = 1
    - At i=1, you can add or subtract. Let's add
    - curSum = 1
    - At i=2, you can add or subtract. Let's subtract
    - curSum = 0
    - At i=3, you can add or subtract. Let's add
    - curSum = 1
    - At i=4, we have reached past the array
    - RETURN 1 if curSum == target, ELSE 0
    - Welp, curSum = 1 = target, so return 1
    - What does this return mean? It means that we 
    have found a way!
    - You will end up with a sum for each possible branch
    - If you think of a tree, we only care about the root-to-leaf 
    paths that add up to the target
    - O(2^n) <- every possible choice is enumerated

    - Memoisation
    - If you notice, we will repeat the same operations 
    on different branches
    - Consider [1,1,1], target=1 again
    - Let us explore two branches
    - BRANCH 1
    -> ADD at i = 0 -> curSum = 1
    -> SUBTRACT at i = 1 -> curSum = 0
    - BRANCH 2
    -> SUBTRACT at i = 0 -> curSum = -1
    -> ADD at i = 0 -> curSum = 0
    - In both BRANCH 1 and BRANCH 2 we land at 
    i=3, curSum = 0
    - Why not store this the first time that we 
    see it
    - This motivates the creation of DP
    - DP: {(i, curSum)->count}
    -> i <- The index which we are considering
    -> curSum <- The sum BEFORE adding or subtracting at index i
    -> count <- The number of ways to reach curSum
    - We add the result of our DFS call to DP, and 
    return that
    - Also we add another base case: if (i,curSum) is 
    already in DP, we return DP[(i,curSum)]
    - O(n*m) time and space
    -> n = size of nums
    -> m = sum(nums)... why not target? 
    be any number from sum(nums) to -sum(nums)
    ->> sum(nums) to -sum(nums) = 2sum(nums)+1 = O(sum(nums))
    

    - BOTTOM-UP APPROACH
    - We further optimise for space complexity
    - Currently we go all the way from i=0 to i=N, and then return back 
    to i=0
    -> This is because we branch down to i=N and then the leaf node 
    tells us whether we have reached the target
    - We will instead find our answer at i=N
    - Let's reimagine DP[i][curSum] = count and give a much tighter 
    definition to it
    -> i <- indices at and past which that we have NOT considered yet
    -> curSum <- the sum after operations on indices j<i
    -> count <- number of ways to reach curSum after operations on 
    nums[j] s.t. j<i
    - Now our base case lands at i=0, where we have done no operations 
    meaning our curSum is 0. There is exactly ONE (1) way to do no 
    operations on no elements
    - Hence: DP[0][0] = 1
    - Now our solution is found at DP[N][target]
    - Look closely
    -> N <- indices 0 to N-1 have been considered for all types of 
    operations
    -> target <- the sum of operations on indices j<N
    -> count <- number of ways to reach target after operations on 
    num[j] s.t. j<N
    
    - The code looks simple, but don't worry. If you see someone 
    coding it quickly that means that they have practised it A LOT! 
    - NeetCode

    '''

    def findTargetSumWaysBRUTEFORCE(self, nums: List[int], target: int) -> int:
        
        def backtrack(i, cur_sum):
            if i ==len(nums):
                return  1 if cur_sum == target else 0
            
            return (backtrack(i + 1, cur_sum + nums[i]) + 
                    backtrack(i + 1, cur_sum - nums[i]))
                
        return backtrack(0, 0)

    def findTargetSumWaysMEMOISATION(self, nums: List[int], target: int) -> int:
        
        
        # (index, cur_sum)->num of ways
        dp = {}

        def backtrack(i, cur_sum):
            
            # Base case
            if (i,cur_sum) in dp:
                return dp[(i,cur_sum)]

            if i == len(nums):
                # We have seen every element
                
                # We have 1 way if we are at the target!
                return 1 if cur_sum == target else 0
            
            dp[(i, cur_sum)] = backtrack(i+1, cur_sum+nums[i])+backtrack(i+1, cur_sum-nums[i])
            
            return dp[(i,cur_sum)]

        # Call on sum is 0, on index 0
        return backtrack(0,0)

    def findTargetSumWaysBOTTOMUPDP(self, nums: List[int], target: int) -> int:
        # By default we assume that there are no ways to curSum
        # This maps curSum->count for index i=0
        dp = defaultdict(int)

        # 1 way to sum to zero with the first zero elements
        dp[0] = 1

        for i in range(len(nums)):
            # We go through every index

            # We generate the DP for the next index
            # This maps curSum->count for index i+1
            next_dp = defaultdict(int)

            for cur_sum, count in dp.items():
                # dp maps curSum->count for index i

                # We now have the old current sum and old count after 
                # operating UP TO index i
                # We ask ourselves: if we were to add at index i, what 
                # would our curSum be? How about subtract?
                # We go to i+1 (i.e., we have computed at i) and the 
                # resulting curSum, and we add the number of ways we had 
                # to reach this old current sum up to i to the number of 
                # ways to reach the new current sum up to i+1  
                # We store this in next_dp which maps curSum->count for 
                # index i+1
                next_dp[cur_sum+nums[i]]+=count
                next_dp[cur_sum-nums[i]]+=count

            # Change next_dp to dp
            dp=next_dp
        # We are at i=N and want curSum = Target
        return dp[target]

if __name__ == "__main__":
    sol = Solution()
    nums = [2,2,2]
    target = 2
    #print(sol.findTargetSumWaysBRUTEFORCE(nums, target)) # 3
    print(sol.findTargetSumWaysMEMOISATION(nums, target)) # 3