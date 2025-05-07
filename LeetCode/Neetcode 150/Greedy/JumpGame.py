from typing import List

class Solution:

    def canJump(self, nums: List[int]) -> bool:

        '''
        - This is a very popular problem
        - We can do this in a DP way, and we'll explain 
        such a solution, but we'll explain AND code a 
        greedy solution

        - nums[i] <- maximum jump length at that position
        - Return True if you can reach the last index from 
        0

        - GREEDY SOLUTION
        - Let us look at this in REVERSE order
        - If we can take x steps to a position, 
        could we not take x-1 steps to the 
        preceding position (possibly 0)?
        - Clearly yes!
        - Therefore, if we assume that we can 
        reach the goal, we want to find the FIRST 
        index that COULD jump to the goal
        - We work backwards until we find it (if we
        do) 
        - Then what?
        - We update the goal
        - If we assume that we can reach the goal, 
        we want to find the FIRST index that could 
        jump to the goal
        - And so on
        - When you have a goal that cannot be reached, 
        THAT is where you must start to reach the 
        final index
        - If the goal is now at the first index, you 
        are done!

        - Example
        - Look at [2,3,1,1,>4<]
        - goal = 4
        - The first index that you could use is 3
        -> 3+1>=4
        - goal = 3
        - The first index that you could use is 2
        -> 2+1>=3
        - goal = 2
        - The first index that you could use is 1
        -> 1+3>=2
        - goal = 2
        - The first index that you could use is 0
        -> 0+2>=1
        - goal = 0
        - Exit the loop
        - goal is now at the index that you must 
        start at!

        '''

        # Set goal to be final index
        goal = len(nums) -1

        # We loop from the final index backwards
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i]>=goal:
                # From the position we are in, could we jump 
                # at least to the goal?

                # If so, shift the goal down
                goal = i
        
        # The goal will be at the index that you must start at 
        # to reach the final index
        return True if goal == 0 else False

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,0,1,0]
    print(sol.canJump(nums)) # True
    nums = [1,2,1,0,1]
    print(sol.canJump(nums)) # False