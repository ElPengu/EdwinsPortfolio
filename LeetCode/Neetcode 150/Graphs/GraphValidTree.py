from typing import List
from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # Another blind 75 problem, woooh!
        # We have n nodes from 0 to n-1 and undirected
        # edges in edges
        # A tree has two conditions
        # > Condition 1: No cycles
        # > Condition 2: Every node is connected
        # We want to create an ADJACENCY LIST and 
        # perform DFS or BFS to determine if it is 
        # the tree
        # How we will do it
        # > Create an adjacency list using edges
        # > Select arbitrary node 0
        # > DFS to detect cycles, which stores BOTH
        # node AND previous node PREV as parameters
        # >> To avoid checking the previous node 
        # we maintain it in PREV and we do DFS on 
        # all NON-PREV neighbours of the node!!! 
        # > Check if we have visited all the nodes
        # Note that we maintain previous because it 
        # makes doing DFS on all the relevant 
        # neighbours easy. Remember that edges 
        # are UNDIRECTED edges, so doing DFS means 
        # that we want to exclude the edge that we 
        # used to reach an edge!
        # O(E+V) time as each is checked at most once
        # O(E+V) space because we create the 
        # adjacency list

        if not n:
            # Base case, no nodes to traverse
            # # Trivially true
            return True
        
        # Create adjacency list
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            # Remember that edges are undirected
            adj[n1].append(n2)
            adj[n2].append(n1)

        # Track visited nodes
        visit = set()

        # Define DFS
        def dfs(i, prev):
            # Base cases
            if i in visit:
                return False
            
            # Now we have visited i
            visit.add(i)

            for j in adj[i]:
                # We SKIP the previous node
                if j == prev:
                    continue
                if not dfs(j, i):
                    # This node is BAD
                    return False
            # This node is NOT BAD
            return True
        
        # Arbitrarily do DFS on 0 AND arbitratily
        # set previous to -1
        # ALSO if we have enough nodes!
        return dfs(0,-1) and n == len(visit)



if __name__ == "__main__":
    sol = Solution()
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print(sol.validTree(n, edges)) # true
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    print(sol.validTree(n, edges)) # false

