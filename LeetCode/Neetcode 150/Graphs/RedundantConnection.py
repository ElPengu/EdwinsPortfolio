from typing import List

class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        - Notes from question
        - We originally have a tree
        - We have one more edge so that it is no longer a tree
        - Determine the edge that can be removed
        - If there are many edges then return the FINAL one in edges
        - Fantastic problem for graph theory
        - You may want to consider the DSA for beginners or advanced
        DSA course by Neet
        
        - Tree: Connected, no cycles
        - This is a cycle detection problem
        - We want to DETECT all the edges in the cycle and put them in 
        a hash set
        - Go over the hash set in reverse

        - We could use UNION FIND to detect the cycle too. We'll use it
        - A tree of size N has N-1 edges, keep this in mind
        - We start with all the individual nodes
        - We start connecting two components for each edge
        - As we know we can tell when two components CONNECT
        - But importantly, we can tell when two components DON'T CONNECT
        - At exactly the point that two components do NOT connect, we 
        can return the edge that we are on!
        - Don't fret, after the cycle forms no other edges will appear 
        from this cycle because at exactly the point the cycle forms 
        all the edges in that cycle will be recognised
        '''

        # Set N to be number of edges
        N = len(edges)
        # Set the PARENT array where every node is its parent
        par = [i for i in range(N+1)] 
        # Maintain the RANK initialised to 1
        rank = [1]*(N+1)

        # FIND operation
        # In this implementation we use a RECURSIVE algorithm
        def find(n):
            if n != par[n]:
                # We do not have the parent
                # Path compression. Instead of n pointing to parent, 
                # parent of n points to grandparent of n
                par[n] = find(par[n])
            
            # We have the parent
            return par[n]


        # UNION operation
        # NOTE: This is an incorrect impleme
        def union(n1,n2):
            # Find the parent of n1 and n2
            p1,p2 = find(n1),find(n2)
            if p1 == p2:
                # This is the same connected component
                # In the context of this problem we do NOTHING
                return False
            
            # Connect components represented by p1,p2 by rank
            if rank[p1]>rank[p2]:
                # p1 represents bigger connected component
                par[p2] = p1
                # Increase rank
                rank[p1] += rank[p2]
            else:
                # p2 represents bigger connected component
                par[p1] = p2
                # Increase rank
                rank[p2] += rank[p1]

            return True
        
        # Go edge by edge
        for n1, n2 in edges:
            if not union(n1,n2):
                # We are attempting to UNION the same component 
                # with two different REPRESENTATIVES
                # These REPRESENTATIVES form the cycle!
                return [n1,n2]

if __name__ == "__main__":
    sol = Solution()
    edges = [[1,2],[1,3],[3,4],[2,4]]
    print(sol.findRedundantConnection(edges)) # [2,4]
    edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
    print(sol.findRedundantConnection(edges)) # [3,4]