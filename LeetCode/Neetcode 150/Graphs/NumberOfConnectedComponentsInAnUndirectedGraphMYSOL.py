from typing import List
from collections import defaultdict

class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # A connected component means a set of CONNECTED nodes
        # 
        # Intuitively, we want to search every NOT VISITED node
        # Now when we search a node
        # We want to use DFS or BFS to exhaust that component
        # Each time we do this we increment some counter
        #  
        # Concretely...
        # Create VISIT and CYCLE sets
        # Create an adjacency list using edges
        # Loop over n and go into DFS
        # Pass node and prevNode into DFS
        # if node in CYCLE return True
        # if node in VISIT return False
        # Search all neighbours EXCEPT prevNode
        # > Return the value of the DFS call
        # Increment some counter
        # Return the counter
        # 
        # 

        # Create VISIT and CYCLE set
        visit, cycle = set(), set()

        # Create adjacency list
        adjList = defaultdict(list)

        # Create a connected components counter
        connectedComponents = 0

        for edge in edges:
            # Undirected so add accordingly
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        
        # Our DFS function
        def dfs(node, prevNode):
            
            # Base cases
            if node in cycle:
                # We have seen this node before in this component, no
                # need to search further
                return True
            if node in visit:
                # We have already considered the connected component 
                # with this node!
                return False            

            # Perform DFS on all nodes except the node that we travelled
            # from to get here
            for neighbour in adjList[node]:
                if neighbour == prevNode:
                    # We do NOT do DFS on the neighbour
                    continue

                # DFS returns False if we are NOT in an UNSEEN 
                # component
                # If this ever happens then the whole component is
                # rotten, just return False all the way up
                if not dfs(neighbour, node):
                    return False

            # We have visited this node for the first time!
            visit.add(node)
            # We must be in an unseen component!
            return True


        # Loop over n
        for node in range(n):
            if dfs(node, -1):
                # We perform DFS on the node
                # DFS returns True IFF it is in an UNSEEN connected 
                # component
                connectedComponents += 1

        # Return number of components
        return connectedComponents



if __name__ == "__main__":
    sol = Solution()
    n=3
    edges=[[0,1], [0,2]]
    print(sol.countComponents(n, edges)) # 1
    n=6
    edges=[[0,1], [1,2], [2,3], [4,5]]
    print(sol.countComponents(n, edges)) # 2