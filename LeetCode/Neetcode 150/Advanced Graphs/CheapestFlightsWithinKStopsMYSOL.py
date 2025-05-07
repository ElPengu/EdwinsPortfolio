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

        - This is a shortest path problem, i.e. Djikstra's algorithm
        - How does it work again?
        
        - DECLARE SET VISIT
        - DECLARE MINHEAP of cost,vertex,stops
        - PUSH (src_cost,src,0) TO MINHEAP
        - PUSH src TO VISIT
        - WHILE VISIT < n:
        -> POP airport_cost,airport,stops FROM MINHEAP
        -> IF airport IN VISIT: continue
        -> IF stops>k: continue # We don't want to consider paths that 
        take too many stops
        -> IF airport IS dst: RETURN airport_cost
        -> FOR destAirport IN flights[airport]:
        ->> PUSH (destAirport_cost+airport_cost,destAirport,stops+1) 
        to MINHEAP
        ->> PUSH destAirport TO VISIT

        - Crap, but what if you want to back track if you go too deep?!
        '''

        # For this to work we need to create an adjacency list
        adjList = defaultdict(list)        
        for flight in flights:
            source = flight[0]
            destination = flight[1]
            cost = flight[2]
            
            adjList[source].append((destination, cost))

        # Create a visit set
        visit = set()

        # Declare min heap
        minH = []

        # Push source airport with cost 0, and 0 stops
        minH.append((0, src, 0))

        while minH:
            # We loop until we have considered all nodes that we can 
            # reach in k stops

            # Pop from the minimum heap
            airport_cost, airport, stops = heapq.heappop(minH)

            if airport in visit:
                # We have already seen this, no need to reprocess
                continue
            
            # Push airport onto visit set
            visit.add(src)

            if stops > k:
                # We don't want to consider paths that take too many stops
                continue
            if airport == dst:
                # We are at the destination airport AND we have taken 
                # at most the number of stops allowed
                return airport_cost
            
            for destAirportInfo in adjList[airport]:
                destAirport = destAirportInfo[0]
                ticketCost = destAirportInfo[1]
                destAirportCost = ticketCost+airport_cost

                # Push all neighbouring airports to heap
                if destAirport == dst:
                    # We do not increment a stop for the destination
                    heapq.heappush(minH, (destAirportCost, destAirport, stops))
                else:
                    heapq.heappush(minH, (destAirportCost, destAirport, stops+1))

        # If we exit this loop then there was no way to reach the 
        # destination in the given time
        return -1

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

