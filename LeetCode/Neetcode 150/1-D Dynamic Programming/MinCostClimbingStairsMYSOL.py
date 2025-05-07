from typing import List

class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        - cost[i] is cost of taking step from the ith floor
        - After paying cost[i] we can step to either (i+1)th
        or (i+2)th floor
        - We can start at index 0 or index 1 floor
        - Minimum cost to reach the top of the staircase
        - Top of stair case: just past the last index in cost
        
        - So we could start at index 0 or index 1, pay, 
        then move one or two steps, until we get past the final
        index

        - At every step we want to know the LOWEST cost of 
        reaching the top
        - BASE CASE: 
        -> floor n-1: cost[n-1]
        -> floor n-2: cost[n-2]
        - INDUCTIVE STEP:
        - floor i: cost[i]+min(cost[i+1],cost[i+2])

        - We use variables ONE and TWO
        - IF LEN(cost)==2: RETURN MIN(cost[0],cost[1])
        - INITIALISE ONE = cost[n-2]
        - INITIALISE TWO = cost[n-1]
        - Update ONE and TWO n-1 times

        -

        - O(n) time
        - O(1) space
        '''

        # Trivial case
        if len(cost) == 2: return min(cost[0],cost[1])

        # Set up variables
        n = len(cost)
        one = cost[n-2]
        two = cost[n-1]

        # We start calculating for the index 
        # before one and two
        i = n-3

        while i >= 0:
            # Store whatever one is
            temp = one

            # Calculate minimum cost starting 
            # at index i and going through 
            # i+1 vs i+2
            one = cost[i]+min(one,two)
            # Store in two what one was
            two = temp

            # Move to preceding index
            i-=1

        # Now one case the cost from the first floor
        # We start at floor 0 though, and choose 
        # between floor 0 and floor 1
        # So we calculate cost through floor 0 
        # vs floor 1
        one = min(one,two)
        
        # Minimum cost is stored in one
        return one


if __name__ == "__main__":
    sol = Solution()
    cost = [1,2,3]
    print(sol.minCostClimbingStairs(cost)) # 2
    cost = [1,2,1,2,1,1,1]
    print(sol.minCostClimbingStairs(cost)) # 4