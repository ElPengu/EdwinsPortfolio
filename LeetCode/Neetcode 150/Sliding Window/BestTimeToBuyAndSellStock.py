from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Assume we are at index i
        #To maximise profit, we must find index j 
        #where prices[j]-prices[i] is at a maximum
        #If we find index k such that prices[k]<prices[i]
        #this is a new minimum, so set i=k, and find a new j
        #Return the maximum profit found

        maxProfit = 0
        minimumIndex = 0

        for i in range(len(prices)):
            if prices[i] < prices[minimumIndex]:
                minimumIndex = i
            else:
                profit = prices[i]-prices[minimumIndex]
                maxProfit = max(maxProfit, profit)

        return maxProfit


if __name__ == "__main__":
    sol = Solution()
    prices = [10,1,5,6,7,1]
    print(sol.maxProfit(prices)) # 6
    prices = [10,8,7,5,2]
    print(sol.maxProfit(prices)) # 0