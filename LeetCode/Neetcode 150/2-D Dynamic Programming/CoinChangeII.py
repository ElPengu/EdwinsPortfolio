from typing import List

class Solution:

    '''
    - We have coins of different denominations
    - We have a target amount
    - Number of *distinct* combinations to total up 
    to the amount
    - You may assume an unlimited number of each coin

    - m^n time <- when we brute force it
    -> m: number of coins
    -> n: the target amount
    - mn <- When we use memoisation
    
    - BRUTE FORCE
    - EXAMPLE: amount = 5, coins = [1,2,5]
    - Consider we start with amount 0
    - We could choose coins in order: 1,2,2 
    -> This is branch 0-(1)->1-(2)->-(2)->5
    - But then we could choose coins in order 2,1,2
    -> This is branch 0-(2)->2-(1)->3-(2)->5
    - We do not want to repeat the coins in this way! These are 
    the same combination

    - How do we avoid duplicates?
    - Let us branch as usual for coin 1
    - But then for coin 2 we DON'T choose coin 1
    - Now that duplicate is eliminated
    - More generally...
    - GIVEN you have just chosen coin i, you are allowed to branch 
    to any coins EXCEPT coin i-1, i-2, ...

    - How do we know which coins that we are not allowed to choose?
    - We will use a POINTER i
    -> i = GIVEN we have just chosen coin i
    - We can only choose any coins that are at or to the right of i

    - MEMOIZATION
    - We avoid duplicate branches, but we have not avoided all 
    duplicate work
    - Whenever we choose a coin, we ask ourselves how many distinct 
    ways can we choose subsequent coins to reach the amount
    - Assume we have amount a left
    - Now suppose we can have amount a left after choosing coins c0 
    and coin c1
    - In both instances we'd calculate the ways to choose from coins 
    after selecting c0 and c1, and for each of THOSE coins you'd 
    repeat work

    - Let dfs(i,a) be a function
    -> i = index of coin we have JUST chosen
    - a = the amount that we have left after choosing coin i
    - Let dfs(i,a) return the number of unique combinations given 
    i and a
    - To avoid calling dfs(i,a) more than once we will store it in 
    a cache!
    - Now we are at O(mn) time, space
    
    - We can reduce to O(n) space through dynamic programming!

    - NAIVE DYNAMIC PROGRAMMING SOLUTION
    - Assume we have cache i, a
    - We have to revisit how exactly the cache functions
    - At exactly (i,a) is the number of ways that you can choose 
    from coins i to N-1 to reach amount a
    -> Look at how the pointer works to see why this is the case
    - BASE CASE
    - At amount 0, we have exactly 1 way for every i. We must choose 
    no coins to get an amount of 0
    
    - There is a specific order that we should do the calculations, 
    and it makes sense!
    - Naturally you'd calculate amount a, a+1,...
    - But there is also an order for calculating coins!
    - Consider arbitrary amount a
    - Consider coins i, i+1, i+2
    - When computing for coin i, you will calculate for coin i+1, 
    i+2
    - It would be ideal to have a solution for i+2 already
    - So you'd start at i+2 and compute for itself. Next move onto 
    i+1, which computes i+1 and then uses the stored value for i+2. 
    finally i computes for itself and then uses the stored values 
    for i+1 and i+2
    - Therefore, we work from the LOWEST amount, and for each amount 
    we work from the LAST coin!

    - How do we calculate the number of ways for (i,a)?
    - i = GIVEN we have just chosen coin i
    - a = amount we are targeting
    - For every coin we see what amount we have after making choice.
    - We see the number of ways that we can reach this new amount 
    for this coin choice and add 1 to it
    -> If the amount is less than 0 then there are no ways. Set to 0
    -> Otherwise we have found some more way. Add these ways

    - SPACE ISSUE
    - Computing (i,a) may necessitate us looking down to (i+i1, a) 
    or right to (i,a+a1), i1>0, a1>0
    - This means that every entry of the cache must be computed
    - Is there a better way? 
    
    - OPTIMAL DYNAMIC PROBLEM SOLUTION
    - You probably would not need this solution. But why not learn 
    it? 
    - Look back at how we made our decisions
    - We went amount a, a+1, ...
    - And then for amount a we computed coin i, i-1, ...
    - In fact, we can reverse this by doing the following
    - We go coin i, i-1, ...
    - And then for coin i we compute amount a, a+1, ...
    
    - How is this decision-making process more efficient?
    - Now we only need to store memory for two coins at a time
    -> coin i, i-1
    - As opposed to storing memory for every (i,a) combination
    
    - Why do we only store memory for two coins? Surely at coin i 
    we still need to know the number of ways for i+1 AND i+2?
    - Let's assume i+2 is the calculated for each amount, and that 
    there is no coin i+3
    - When we calculate for i+1 for each amount we add up the ways 
    if we chose coin i+1 OR coin i+2
    - Okay, now we move to i
    - For every amount a we want the number of ways if we chose 
    coin i OR i+1 OR i+2
    - So we'd calculate for choosing coin i, sure
    - But importantly, we'd ONLY also check what (i+1,a) maps to!
    - So we only need the row for coin i and the row for coin i+1
    - Let's look at what (i,a) is meant to map to
    - (i,a) -> number of ways if, for amount a, we chose coin i, 
    i+1,...
    
    - Why couldn't we just store amounts a, a+1 and all coins?
    - Okay, consider coin i
    - If we choose coin i or coin i+1, we may consider amounts a, 
    and a2
    - Since coin[i] could be 3 and coin[i+1] could be 7, we might 
    jump to ANY amount!
    - To summarise, when calculating the number of ways for 
    combination (i,a) you will strictly only need to calculate at most 
    for choosing coin i or coins i+1,...
    - Choosing coin i or i+1,... will result in any amount a, so 
    you must store this 
    - Calculating for coin i will be done manually
    - Coins i+1,... is already computed in (i,a), (i,a-1),..., (i,0)
    
    - O(n) space
    '''

    def changeRECURSION(self, amount: int, coins: List[int]) -> int:
        # O(n*m)

        cache = {}

        def dfs(i,a):
            # A lot of base cases!
            if a == amount:
                # We have reached the amount!
                # Return 1
                return 1
            if a > amount:
                # We have exceeded the amount, we 
                # cannot reach amount now. return 0
                return 0
            if i == len(coins):
                # We have no coins available to us, 
                # return 0
                return 0
            if (i,a) in cache:
                # We have already computed this, no need
                # to recalculate!
                return cache[(i,a)]
            
            # This is the inductive case
            # We ask ourselves
            # 1. How many distinct ways can we 
            # choose coins GIVEN we choose coin i?
            # 2. How many distinct ways can we 
            # choose the coins in indices >i
            # > dfs(i+1,a) will calculate for all 
            # indices >i as you would call dfs, 
            # let j=i+1 in this call of dfs, now 
            # you get to 
            # cache[(j,a)]=dfs(j,a+coins[j])+dfs(j+1,a)
            # See!
            cache[(i,a)]=dfs(i,a+coins[i])+dfs(i+1,a)
            return cache[(i,a)]

        return dfs(0,0)
    
    def changeDP(self, amount: int, coins: List[int]) -> int:
        # O(n*m) space still


        dp = [[0]*(len(coins)+1) for i in range(amount+1)]
        dp[0] = [1]*(len(coins)+1)

        for a in range(1, amount+1):
            # Start at amount = 1
            for i in range(len(coins)-1,-1,-1):
                # Start at the final coin
                # We have one coin to choose from

                # One decision: skip the coin at i.
                dp[a][i]=dp[a][i+1]
                if a-coins[i]>=0:
                    # a is the target amount
                    # So here we choose i and move 
                    # to the new amount
                    dp[a][i]+=dp[a-coins[i]][i]
        
        return dp[amount][0]

    def changeOptimalDP(self, amount: int, coins: List[int])->int:
        # Memory complexity: O(n)
        
        # Create an array of 0s, for every from 0 
        dp = [0]*(amount+1)
        # We know that for an amount of 0 there is 
        # 1 way
        dp[0]=1

        for i in range(len(coins)-1,-1,-1):
            # Loop from the last coin to the first


            # Set up the array for the next amount
            # Exactly the same as the base case
            nextDP = [0]*(amount+1)
            nextDP[0]=1

            
            for a in range(1,amount+1):
                # Loop from amount = 1 to target amount
                
                # Given we have chosen coin i, we 
                # could choose any coin i+1. The 
                # number of ways to do this is stored 
                # in the old dp for this amount!
                nextDP[a]=dp[a]

                # We could also choose coin i, let's 
                # see what happens when we do so
                if a-coins[i]>=0:

                    # Ah, we see that we still have an 
                    # amount to select
                    # We have already stored the number 
                    # of ways given we chose this coin 
                    # and have this resulting amount
                    # Add the number of ways here too!
                    nextDP[a]+=nextDP[a-coins[i]]

            # Now dp is populated
            dp = nextDP

        # We have an array of the number of ways that 
        # we could select coin i, where i = 0
        # I.e., the number of ways that we could select 
        # the first coin, the second, etc. and reach 
        # the target amount.
        # This is stored in the amount index of dp!
        return dp[amount]

if __name__ == "__main__":
    sol = Solution()
    amount = 4
    coins = [1,2,3]
    #print(sol.changeRECURSION(amount, coins)) # 4
    #print(sol.changeDP(amount, coins)) # 4
    print(sol.changeOptimalDP(amount, coins)) # 4
    amount = 7
    coins = [2,4]
    #print(sol.changeRECURSION(amount, coins)) # 0
    #print(sol.changeDP(amount, coins)) # 0
    print(sol.changeOptimalDP(amount, coins)) # 0