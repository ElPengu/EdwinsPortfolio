from typing import List

class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        - We have an array of coins
        - coins[i] = value of coin at i
        - We have a target amount of money to make
        - We want to find out the fewest number of 
        coins to make EXACTLY the amount
        - If you cannot make the amount then return 0
        - NOTE: You have an unlimited number of coins 
        at an index

        - If you think of the backtracking brute force 
        solution, you'd start with amount. Then 
        you'd branch for each coin and reduce value 
        for each branch
        - EXAMPLE: amount = 7, coins = [1,3,4,5]
        - AFTER 1 branch: amounts = [6,4,3,2]
        - Now if you draw the branching out, you will 
        see that you will 
        repeat work for amounts. E.g. you can get to 
        amount of 2 by choosing 5,2 OR 2,2,1

        - We will store a cache DP
        - DP[i] stores minimum number of coins to get to 
        amount=i
        - FORALL i: DP[i]=amount+1 (as a ceiling)
        - FORALL i, j: DP[i] = min(1 + DP[i-coins[j]], DP[i])
        -> I.e., DP[i] holds coins, and we check what 
        happens when we add a SINGLE coin from coins 
        and minimise DP[i]. Do this for EVERY coin
        -> Note that DP[i-coins[j]] will always be 
        stored!
        
        - O(coins*amount) time <- For every possible 
        amount we consider every coin
        - O(amount) space <- We store every possible
        amount
        '''

        # Set cache
        # We go from 0 up to amount, hence DP is of this size
        # We initialise all values to amount+1 to make minimising it 
        # easy
        dp = [amount+1] * (amount+1) 

        # BASE CASE
        dp[0] = 0

        for a in range(1, amount+1):
            # This is the amount for this loop, that will be stored
            # in dp[a]

            for c in coins:
                # We consider adding this coin

                if a-c>=0:
                    # We do not immediately go over amount 
                    # a after adding this coin
                    
                    # Add the coin and see if the result is less 
                    # than what we calculated to be the number of 
                    # coins
                    dp[a] = min(dp[a], 1+dp[a-c])

        # Return the amount if not default, else -1
        return dp[amount] if dp[amount] != amount+1 else -1



        pass


if __name__ == "__main__":
    sol = Solution()
    coins = [1,5,10]
    amount = 12
    print(sol.coinChange(coins, amount)) # 3
    coins = [2]
    amount = 3
    print(sol.coinChange(coins, amount)) # -1
    coins = [1]
    amount = 0
    print(sol.coinChange(coins, amount)) # 0

