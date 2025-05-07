from typing import List

class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        - We have a connected undirected graph with n nodes from 1 to n
        - Initially it has no cycles and n-1 edges
        - One additional edge is added with two different vertices chosen 
        from 1 to n and the edge did not previously exist
        - Find the edge
        - If there are multiple edges then return the last one travelled
        by
        
        - We are essentially removing a cycle
        - We could do DFS. 
        - What does it mean when we get back to a VISITED node? We have a 
        cycle
        - What happens if we were to remove the last edge travelled?
        - Let edge (i,j) be s.t. i->j is that final edge, with j visited
        - again
        - If that edge is removed you can still travel j->...->i
        - If i is connected to any other vertices then you can travel
        j->...->i then go to those vertices!
        
        - To implement
        - Create a hash map of nodes pointing to neighbours in a list
        - Maintain VISITED set
        - Maintain EDGESTRAVELLED set
        - Initialise lastRedundantEdge
        - Perform recursive DFS from node 1, taking arguments node, 
        previous node, and edge travelled
        -> When you see a node already in VISITED add the edge travelled
        by to EDGESTRAVELLED set
        - Iterate over edges and update lastRedundantEdge to be the last
        one seen that is in EDGESTRAVELLED

        - Wait I don't think that this totally works
        - Example 2 in NeetCode 150 is messing me up
        - The only thing that I can think is that technically ANY edge 
        in the cycle can be deleted!
        - This implies that you not only delete that final edge, no.
        - As you return back up the cycle you could delete all of 
        those edges I think
        '''

        # Set up hash map adjList
        adjList = {}

        # Maintain VISITED set


        # Maintain EDGESTRAVELLED SET


        # Initialise lastRedundantEdge

        # Recursive DFS function


        # Iterate over edges and update lastRedundantEdge


        # Return lastRedundantEdge

        pass

if __name__ == "__main__":
    sol = Solution()
    edges = [[1,2],[1,3],[3,4],[2,4]]
    print(sol.findRedundantConnection(edges)) # [2,4]
    edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
    print(sol.findRedundantConnection(edges)) # [3,4]