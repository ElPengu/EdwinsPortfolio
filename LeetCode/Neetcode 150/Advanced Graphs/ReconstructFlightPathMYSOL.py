from typing import List

class Solution:

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        '''
        - We have tickets from 3 lettered airports
        - ticket[i] = [source_i, dest_i]
        - All tickets belong to someone who departed from "JFK"
        - Reconstruct the flight path taken by this person, assuming
        that each ticket is used exactly once
        - If there are multiple paths, return the "lexographically" 
        smallest one

        - What are we asked for?
        - We want to find the path from JFK to some airport i1 at level 
        1
        - This path will be length 1
        - At level 2 we want the path from JFK to some airport i2
        - To save space we simply append i2 to this path
        - We could use DFS here

        - But we could have bidirectional arcs
        - To deal with this we maintain a VISITED set of EDGES, not 
        nodes
        - This means that we do not VISIT a city along the same edge
        more than once

        - Okay, fine. But how exactly do we distinguish different 
        paths. If we could choose to go from JFK along 10 different 
        paths at the first level, we have 10 different ways ....
        - OHHHHHHHHHHHHHHHH, I JUST REALISED!!!
        - You SPECIFICALLY choose the edge whose destination is 
        lexographically smaller. 

        - To wrap this into a solution
        - We have a list of edges
        
        
        - STAGE 1: Create helper variables
        - INITIALISE SET VISIT
        - INITIALISE HASHMAP adjList
        
        - STAGE 2: Iterate over tickets to populate adjList
        - FOR src, dest in tickets
        -> APPEND dest TO LIST adjList[src] 


        - STAGE 2: Perform DFS from JFK
        - DFS(city, ticketList):
        -> PREPEND city TO ticketList
        -> INITIALISE LIST neighbours
        -> FOR neighbour in adjList[src]:
        ->>  APPEND neighbour to neighbours
        -> SORT neighbours
        -> FOR neighbour in neighbours:
        ->> APPEND DFS(neighbour) TO ticketList
        -> RETURN ticketList 
        

        - STAGE 3: Return output of DFS on JFK
        - RETURN DFS("JFK", [])


        - With only 5 seconds after 20 minutes
        - I really feel like this would work.
        - Writing the code is so hard, but the pseudo code is difficult
        but a lot more accessible
        '''

        pass


if __name__ == "__main__":
    sol = Solution()
    tickets = [["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]
    print(sol.findItinerary(tickets)) # ["JFK","BUF","HOU","SEA"]
    tickets = [["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]
    print(sol.findItinerary(tickets)) # ["JFK","HOU","JFK","SEA","JFK"]