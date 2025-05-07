from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        '''
        - We have prices for NeetCoin on the ith day
        - You may buy and sell one NeetCoid multiple times
        - After selling your NeetCoin you cannot buy another 
        on the next day (cooldown of 1 day)
        - You may own at most ONE (1) NeetCoin
        - You can complete as many transactions as you'd like
        - Maximum profit that you COULD achieve?

        - You have two choices: you COULD buy the NeetCoin 
        or you could NOT buy the NeetCoin
        - My brain is fried, this is the final problem before 
        workday ends

        - Okay, let's slow down
        - Our restrictions are two 
        - whether we SOLD the NeetCoin yesterday -> Whether
        we can buy today
        - Whether we OWN a NeetCoin or not -> Whether we can buy or not

        - What would happen if we had an NX3 dimensional array
        - N days
        - ROW 1: We SOLD yesterday and therefore own no NeetCoin
        - ROW 2: We did NOT SELL yesterday and own 1 NeetCoin
        - ROW 3: We did NOT SELL yesterday but own 0 NeetCoin
        - Note that we cannot have sold yesterday and own a NeetCoin, 
        given the conditions

        - Okay, now what
        - On day i we look at the maximum profit that we could have 
        made by day i-1
        - What if we greedily choose to buy or sell now?
        - Well, that won't work. Consider [1,3,4,0,4]

        - What if we manually stored every single state that you could
        land in?
        - OPT 1: We SOLD yesterday and therefore own no NeetCoin -> BUY
        - OPT 2: We SOLD yesterday and therefore own no NeetCoin -> DO NOTHING (Cannot SELL_
        - OPT 3: We did NOT SELL yesterday and own 1 NeetCoin -> SELL
        - OPT 4: We did NOT SELL yesterday and own 1 NeetCoin -> DO NOTHING (Cannot BUY)
        - OPT 5: We did NOT SELL yesterday but own 0 NeetCoin -> BUY
        - OPT 6: We did NOT SELL yesterday but own 0 NeetCoin -> DO NOTHING (Cannot BUY)

        - We now have 6 possibilities
        - We must avoid branching out. We could go 6->6^2, so on...
        - We will start with day 1 and take the MAX PROFIT based on all 
        choices (this is an O(1) operation)
        - At day i, take the highest profit based on day i-1 and compute
        for each one
        
        - Final issue: If you take OPT 3 THEN you cannot take OPT 1
        - I'd default to -1 to indicate that it is invalid. Also you'd 
        never select it

        - Tough! Took me about 20+ minutes
        '''
        pass

if __name__ =="__main__":
    sol = Solution()
    prices = [1,3,4,0,4]
    print(sol.maxProfit(prices)) # 6
    prices = [1]
    print(sol.maxProfit(prices)) # 0