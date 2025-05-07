from typing import List

class Solution:

    def change(self, amount: int, coins: List[int]) -> int:
        '''
        - We have coins of different denominations
        - We have a target amount
        - Number of *distinct* combinations to total up 
        to the amount
        - You may assume an unlimited number of each coin

        - BRANCHING approach
        - At any one point you could choose a coin
        - If you remain below the amount you could choose another
        - We are looking for distinct combinations
        - How to represent a distinct combination?
        - We could use a hash map, initialised such that each coin 
        points to zero
        
        - BASE CASE
        - Amount = 0 -> RETURN coins mapped to zero
        - INDUCTIVE STEP
        - Amount = i -> IF amount-coins[i] >= 0: RETURN map for 
        amount-coins[i] INCREMENT coins[i] in map 
        - Wait a minute
        - We can have different maps though
        - What if for amount = 5 we could have 1x5/ or 5x1/?

        - How do we store every single map?
        - I know!
        - We have a 2D array
        - We have amount i at the ith entry
        - We have a SET of possible mappings for amount i at the ith 
        entry 

        - BASE CASE
        - Amount = 0 -> RETURN list of one mapping: coins mapped to zero
        - INDUCTIVE STEP
        - Amount = i -> IF amount-coins[i]>=0: 
        -> maps = maps for amount-coins[i]
        -> FOR map IN SET of maps: INCREMENT coins[i] 
        -> RETURN SET of maps

        
        - CACHING
        - Okay, this makes sense. But how do we cache this?
        - We can go backwards because I am used to doing it that way
        - Start at amount = 0
        - Store the default map of coins to zero in a set
        - Increment amount
        - For every coin that you can add and still have >=0 amount, 
        find the associated set of maps for THAT amount and store all 
        these maps for this amount
        - Finish when you are at the target amount 

        - I am pretty sure that this would work!


        '''

        pass

if __name__ == "__main__":
    sol = Solution()
    amount = 4
    coins = [1,2,3]
    print(sol.change(amount, coins)) # 4
    amount = 7
    coins = [2,4]
    print(sol.change(amount, coins)) # 0