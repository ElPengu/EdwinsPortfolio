from typing import List


class Solution:

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        '''
        - Pretty difficult, but accessible if you are good at graphs
        - You have a list of DIRECTED tickets
        - We are guaranteed that an individual started from "JFK", 
        and all other airports are 3 lettered
        - We must use every ticket EXACTLY ONCE
        - We return the itinerary in lexical order
        -> E.g., [JFK,LGA,JFK,LGB,JFK], NOT [JFK,LGB,JFK,LGA,JFK]
        
        - We must have a good understanding of graphs. We use DFS
        - We INITIALISE a HASHMAP adjList out of tickets
        - We SORT tickets by source airport (this groups source
        airports) together, then by destination airport (this 
        puts the destination airports for each source airport in 
        order)
        - We POPULATE adjList with tickets with source as key, 
        destination as value to APPEND
        - We INITIALISE LIST res to keep track of the CITIES that we visit
        - We APPEND JFK to res
        - We perform DFS from JFK and add cities visited
        - Whenever we call DFS on neighbours, we use adjList, which 
        holds cities in lexographical order already!!!
        - RETURN adjList WHEN len(res) = len(tickets)+1
        - Plus one because we begin with res holding JFK

        - Right...
        - One more thing: what if we have more tickets to use, but we 
        cannot use them at our airport?
        -> Example: A citizen is in Paris. He has tickets to JFK and 
        Kinshasa, and a return ticket <Paris, Kinshasa>. If he chose to
        go to JFK then his return ticket <Paris, Kinshasa> would go 
        unused! Upon realising this he'd DELAY going back to JFK until 
        travelling to Kinshasa! 
        - This implies that we cannot always be greedy, we must be able
        to back track
        -> In the example, the citizen cannot just go airport by airport 
        otherwise he'll get stuck. He'd have to sit down with a book the 
        night before and work through his itinerary

        - O((V+E)2)->O(E2) time <- due to backtracking, note that V < E
        - O(E) space for the adjacency list  

        - Wow I was so close with my thinking! I just did not consider
        the possibility of sink cities. I am so happy with and proud of
        the progress that I have made
        '''

        # Map every source city to an empty list for adjaceny list
        adj = {src: [] for src, dst in tickets}

        # Sort our tickets
        tickets.sort()

        # Populate adj
        for src, dst in tickets:
            # Append the destination city
            adj[src].append(dst)
        
        # Initialise city list with JFK
        res = ["JFK"]
        def dfs(src):
            # Base cases
            if len(res) == len(tickets)+1:
                # We have found the order in which this citizen 
                # travelled
                return True
            if src not in adj:
                # This means that the source has no outgoing edges
                # If we have not reached the condition above by 
                # this point then we will never be able to complete
                # the path!
                return False 

            # We create a copy of the neighbour list
            # We don't want to change the actual list in place as
            # we iterate through it
            temp = list(adj[src])

            # We use enumerate so that we get the index of each 
            # neighbour too
            for i, v in enumerate(temp):
                # For the input source we go through all the neighbours

                # This it the citizen essentially saying okay, we are at 
                # Paris. Let's go to JFK 
                # 
                adj[src].pop(i)
                # We assume that we visit this city
                res.append(v)

                # Run DFS - if it returns true then we know that through
                # THIS airport we can visit all the other cities
                if dfs(v): return True
                
                # This looks weird, but bear with me
                # What we are saying is that we cannot visit this 
                # city YET, lest we leave some tickets unused
                # This is the equivalent of the citizen realising 
                # that if he goes to Paris from JFK then he'll 
                # be unable to use his ticket from Paris to Kinshasa 
                # and back because there are no flights 
                # directly from JFK to Kinshasa and back 
                adj[src].insert(i, v)
                res.pop()
            # No city here was correct along this DFS
            return False
        
        dfs("JFK")
        return res


if __name__ == "__main__":
    sol = Solution()
    tickets = [["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]
    print(sol.findItinerary(tickets)) # ["JFK","BUF","HOU","SEA"]
    tickets = [["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]
    print(sol.findItinerary(tickets)) # ["JFK","HOU","JFK","SEA","JFK"]