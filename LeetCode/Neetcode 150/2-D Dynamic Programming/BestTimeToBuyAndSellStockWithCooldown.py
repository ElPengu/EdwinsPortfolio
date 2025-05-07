from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        '''
        - This is a very interesting AND challenging problem
        - It will be made to look easy by NeetCode through 
        drawing pictures!

        - We have prices for NeetCoin on the ith day
        - You may buy and sell one NeetCoid multiple times
        - After selling your NeetCoin you cannot buy another 
        on the next day (cooldown of 1 day)
        - You may own at most ONE (1) NeetCoin
        - You can complete as many transactions as you'd like
        - Maximum profit that you COULD achieve?

        - We have so many decisions to make, right? Well, let's 
        draw them out and use an example

        - BRANCHING SECTION

        - EXAMPLE
        - [1,2,3,0,2]
        - We have three choices: BUY, SELL, COOLDOWN
        - On day 0 we can either BUY (profit -1) or COOL DOWN (profit 0)
        - BUY branch
        -> We cannot BUY
        -> SELL (profit +1)
        ->> COOLDOWN (profit 0) # You must skip a day after selling
        ->>> BUY (profit 1)
        ->>>> SELL (profit 3)
        ->>>> COOLDOWN (profit 1)
        ->>> COOLDOWN (profit 1)
        -> COOLDOWN (profit -1)
        ->> ...
        - COOL DOWN branch
        -> BUY (profit -2)
        ->> ...
        -> COOLDOWN (profit 0)
        ->> ...

        - Do you notice that when you can BUY on day i...
        -> You may SELL on day i+1
        -> You may COOLDOWN on day i+1
        - Do you notice that when you can SELL on day i...
        -> You MUST COOLDOWN on day i+1
        -> You may BUY on day i+2
        -> You may COOLDOWN on day i+2
        
        - Okay, with that scaffolding in place, we must shake hands on 
        this next insight
        - Let BUY be TRUE when you can BUY on day j, and FALSE when 
        you CANNOT BUY on day j (i.e., you must sell)
        - If you choose to COOLDOWN on day j, there is exactly no 
        effect on your ability to buy on day j+1
        - If you choose to make a transaction, it must agree with BUY 
        and the conditions for buying
        -> If BUY is TRUE, the only transaction that you may make is 
        to BUY on day j+1
        -> If BUY is FALSE, the only transaction that you may make is 
        to COOLDOWN on day j+1 and SELL on day j+2

        - Now we are ready for profits

        - How does your profit change based on the action taken on 
        day i?
        - SELL on day i -> profit(can BUY on day i+1)+prices[i]
        - BUY on day i -> profit(cannot BUY on day i+1)-prices[i]
        - COOLDOWN on day i -> profit(carry forward ability to BUY 
        XOR SELL on day i+1)

        - With THAT piece of scaffolding in mind, we now move on to 
        how exactly we calculate the maximum profit
        - It looks like we calculate the profit on day i and then move 
        to day i+1, but that is WRONG
        - We are asking ourselves: given the choices that we can make on 
        day i, what is the maximum profit that we can make through to 
        the final day? We take that choice
        - The only way to find this out is to ask this exact question 
        for day i+1 for each choice
        - So we go from 2 choices on day i to four choices total to day 
        i+1
        - So we calculate the choice that generates maximum profit from 
        day i to day N-1

        - Won't this go on forever though?
        - Nope! We have the inductive step, now we create the base case
        - We say that on day N (i.e., the day after the final day) we 
        make exactly ZERO profit. Thus we RETURN ZERO 
        -> Think of it as us saying that whether you intend to BUY, 
        SELL, or COOLDOWN, you are sent away because the market is closed
        - Now we bubble to day N-1
        - Both our choices resulted in making ZERO profit
        - Now we find the choice that gave the maximum profit and we 
        return THAT PROFIT
        - Don't we need the choice?
        - Consider this. We only want the maximum profit from day i to 
        day N-1
        - We ask ourselves: based on the available choices on day i, 
        how much profit can we make?
        - As soon as we have calculated this profit, we have what we 
        want 

        - CACHING
        - How exactly could we repeat any information?
        - Consider that along the COOLDOWN only branch we can choose to 
        BUY on day i
        - Consider that along the very same COOLDOWN only branch we could 
        BUY on day i-3, SELL on day i-2, COOLDOWN on day i-1, and BUY on 
        day i
        - This implies that we need to remember the following
        -> What is the maximum profit gained based on our BUY state on 
        day i
        - Therefore we will create mapping (i, BUY)->max_profit after 
        making the two choices on day i for whatever BUY condition we 
        in
        - This will be our second base case so that we needn't repeat 
        calculations
        - The first time that we create the mapping though we'll just 
        store it as explained and then return it!
        - O(n) time <- There are n possibilities for BUY vs SELL
        '''

        # State: ABLE to Buy or ABLE to Sell
        # If Buy -> i+1 (when you buy you can sell or cooldown on the 
        # next day)
        # If Sell -> i+2 (when you sell you must cooldown, so skip a 
        # day)

        # key=(i, buying) val = max_profit
        dp = {}

        def dfs(i, buying):
            # BASE CASE
            if i >= len(prices):
                # We are out of bounds!
                # We can't make any profit here
                return 0
            if (i, buying) in dp:
                # Assume max profit with this key has been stored
                # This is the cache coming into action!
                return dp[(i,buying)]
            
            # We can always cooldown, in which case our profit stays 
            # the same
            # Also we carry on the state of being to buy XOR sell 
            # onto the next day
            cooldown = dfs(i+1, buying)

            # Are we buying or selling
            if buying:
                # We can buy, but then on the next day we CANNOT buy 
                # on the next day!
                # Also we lose profit from buying the coin
                # Buying was TRUE, flip it to FALSE
                buy = dfs(i+1, not buying) - prices[i]

                
                # Take the best choice out of the 
                # choices of buying and cooling 
                # down
                dp[(i, buying)] = max(buy, cooldown)
                
            else:
                # We must take a cooldown day
                # We move two days on and we are NOT buying
                # Also we make profit from selling the coin
                # BUYING was False, flip it to TRUE
                sell = dfs(i+2, not buying) + prices[i]

                # Take the best choice out of the 
                # choices of selling and cooling 
                # down
                dp[(i, buying)] = max(sell, cooldown)
            
            # After making these choices
            return dp[(i, buying)]
        
        # We can always buy
        return dfs(0, True)

if __name__ =="__main__":
    sol = Solution()
    prices = [1,3,4,0,4]
    print(sol.maxProfit(prices)) # 6
    prices = [1]
    print(sol.maxProfit(prices)) # 0