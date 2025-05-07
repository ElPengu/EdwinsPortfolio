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

        - We will use memoization. I.e. we will store
        all calculated paths in a bottom-up fashion 
        using the cost array
        - We COULD use variables one and two starting
        at the end and move up... but we'll use the
        array just to show you how it works

        - MEMOIZATION ON COST
        - On the final floor we'd pay cost[0] after 
        clearing the stairs. So we append a cost of 
        zero
        - BASE CASE: We use floor n-3 or floor n-2, 
        leave these values as it
        - INDUCTIVE STEP: Starting at floor i =  n-3 
        until you get to floor 0
        -> Calculate paying for floor i and using
        floor i+1 vs floor i+2
        -> Store minimum in floor i
        - Out of loop, return minimum cost of 
        jumping to floor 0 vs floor 1

        - O(n) extra memory
        - O(1) extra space (we write onto cost array)

        '''

        # We append an extra 0 for the final floor
        cost.append(0)

        for i in range(len(cost)-3,-1,-1):
            # We start at floor n-2 and go until 
            # we get to floor 0
            # We must use either floor n-2 or 
            # floor n-1!

            cost[i] = cost[i]+ min(cost[i+1],
                          cost[i+2])
            
        return min(cost[0], cost[1])



if __name__ == "__main__":
    sol = Solution()
    cost = [1,2,3]
    print(sol.minCostClimbingStairs(cost)) # 2
    cost = [1,2,1,2,1,1,1]
    print(sol.minCostClimbingStairs(cost)) # 4