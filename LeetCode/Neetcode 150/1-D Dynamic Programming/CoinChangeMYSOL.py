from typing import List

class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        - We have an array of coins
        - coins[i] = value of coin at i
        - We have a target amount of money to make
        - We want to find out the fewest number of coins to make 
        EXACTLY the amount
        - If you cannot make the amount then return 0
        - NOTE: You have an unlimited number of coins at an index

        - What choice do we have?
        - At any point we can select ANY coin and see if we get to the 
        amount. If we go over then that coin does not work
        
        - What would the smallest subproblem be?
        - The value of ONE (1) coin

        - BASE CASE(s)
        - Select a single coin (loop over coins)

        - INDUCTIVE STEP 
        - Select a coin at some index

        - There is some repeated work in the inductive step though. 
        - Consider the case of selecting coins[i] 3 times at base cases 
        coins[i+1] and coins[i+2]
        - How could we reduce this

        - We can select coins[N-1] a number of times and be below or AT 
        the target amount
        - Ditto for every other index
        - Now the question becomes: what is the lowest number of ways to 
        combine values for different selections of coins across different
        indices that reach the exact amount. If none, return -1

        - This is very vague for coding purposes, I am sure that there is 
        a better way to express this idea

        - I have no idea!

        '''


        pass


if __name__ == "__main__":
    sol = Solution()
    coins = [1,5,10], amount = 12
    print(sol.coinChange(coins, amount)) # 3
    coins = [2], amount = 3
    print(sol.coinChange(coins, amount)) # -1
    coins = [1], amount = 0
    print(sol.coinChange(coins, amount)) # 0

