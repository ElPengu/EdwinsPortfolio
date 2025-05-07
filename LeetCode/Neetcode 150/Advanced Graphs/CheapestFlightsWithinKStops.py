from typing import List
import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        '''
        - We have n airports labelled 0 to n-1
        - We have an array of flights
        - flights[i] = [from_i,to_i,price_i]
        - There are no duplicate flights nor flights from an airport to 
        itself

        - src, dst: source,destination
        - src IS NOT dst
        - k is maximum number of intermediary airports
        - Cheapest price from src to dst with at most k stops, -1 if 
        impossible

        - We COULD use Djikstra's algorithm, but the constraint about 
        stops makes it not super-efficient, but it is still doable! 
        - We will use the Bellman-Ford algorithm. This shortest-path 
        algorithm can incorporate the at most k stops part

        - This is a shortest path algorithm

        - The main idea used is that we assume that 
        it takes infinite time to reach each city 
        apart from the source
        - Now we ask ourselves how long it would 
        take in 1 step. So we loop over every edge i->j 
        and use the cost to get to i to compute the 
        time to get to j
        - We only store a new cost to get to j if it 
        is smaller than what it was before

        - O(E*V) <- Time complexity for Bellman Ford generally
        - O(E*k) <- Time complexity for Bellman-Ford in this **specific**
        problem where k is the maximum number of stops 
        
        '''

        # Initialise prices to infinity
        prices = [float("inf")]*n
        # Set source to have price 0
        prices[src] = 0

        # We loop k+1 times since destination doesn't count as a stop
        for i in range(k+1):
            # Initialise a temporary mapping for prices
            tmpPrices = prices.copy()

            for s,d,p in flights:
                # source, destination, price
                if prices[s] == float('inf'):
                    # If it takes infinite time to even reach the source
                    # of this edge then there is no reason to compute it
                    continue

                if prices[s]+p < tmpPrices[d]:
                    # We see that we can get a SMALLER price to get here
                    # using i number of stops through s
                    tmpPrices[d] = prices[s]+p

            # We reassign prices to be temp prices
            prices = tmpPrices

        return -1 if prices[dst] == float("inf") else prices[dst]   

if __name__ == "__main__":
    sol = Solution()
    n = 4
    flights = [[0,1,200],[1,2,100],[1,3,300],[2,3,100]]
    src = 0
    dst = 3
    k = 1
    print(sol.findCheapestPrice(n,flights,src,dst,k)) # 500

    n = 3
    flights = [[1,0,100],[1,2,200],[0,2,100]]
    src = 1
    dst = 2
    k = 1
    print(sol.findCheapestPrice(n,flights,src,dst,k)) # 200

