from typing import List
from collections import defaultdict

class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        '''
        - A connected component means a set of CONNECTED nodes
        - A pretty straightforward problem
        - We **could** make an adjacency list and then perform DFS on every node NOT in set VISITED (with the help of a CYCLE set) and increment the number of connected components for every new connected component
        - This WOULD be O(E+V) time to traverse, O(E+V) space to create the adjacency list
        - However, we can just use **union find** which is EVEN more natural
        - We maintain PARENT array
        - To optimise we also maintain a RANK array
        - PARENT array initially maintains all nodes assuming that all parents are unique connected components of size 1
        -> I.e., we assume that all nodes in PARENT are connected components
        - SET FIND(x)
        ->> Set res = n1
        ->> WHILE res != PARENT[res]
        ->>> PARENT[res] = PARENT[PARENT[res]]
        ->>> res = PARENT[res]
        ->> return res
        - We loop over the list of edges 
        -> Set x = FIND(i), j = FIND(j)
        -> IF x = y (root parent may be itself)
        ->> They are already in the same connected component
        ->> RETURN 0
        -> ELSE 
        ->> SET x,y s.t. RANK[x] >= RANK[y]
        ->> LET PARENT[y] = PARENT[x]
        ->> LET RANK[x] = RANK[x] + RANK[y]
        ->> We have UNION'd two components!
        ->> RETURN 1
        '''

        # Create a PARENT array
        par = [i for i in range(n)]

        # Create RANK array
        rank = [1]*n
        
        # We set up a operation
        def find(n1):
            res = n1

            while res != par[res]:

                # We go until the parent is its own parent
            

                # This is path compression, which ensures that every 
                # node on the path to the REPRESENTATIVE points 
                # directly to the representative
                par[res] = par[par[res]]

                # Set the node to be its parent
                res = par[res]
            
            return res
        
        # Define our union find function
        def union(n1, n2):
            # Find the root parents
            p1, p2 = find(n1),find(n2)

            # Same root parent, so we have already considered this 
            # component
            if p1 == p2:
                return 0
            
            # We do union by rank
            if rank[p2]>rank[p1]:
                # p2 is at the larger component
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                # p1 is at the larger component
                par[p2] = p1
                rank[p1] += rank[p2]

            # We have UNION'd two components!
            return 1

        # Assume we have n components
        res = n
        for n1, n2 in edges:
            # Union returns 1 when two connected components are UNION'd
            # so we have one fewer components
            res -= union(n1,n2)

        # Return all components
        return res



if __name__ == "__main__":
    sol = Solution()
    n=3
    edges=[[0,1], [0,2]]
    print(sol.countComponents(n, edges)) # 1
    n=6
    edges=[[0,1], [1,2], [2,3], [4,5]]
    print(sol.countComponents(n, edges)) # 2