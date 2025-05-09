from collections import defaultdict
from typing import List

class Solution:

    def topologicalSort(self, edges: List[List[int]]):

        # Create a set of nodes that have been visited
        visited = set()

        # Create a set of all nodes
        nodes = set()

        # Store the adjacency list AND nodes
        adjList = defaultdict(list)
        for edge in edges:
            u, v = edge[0], edge[1]
            adjList[u].append(v)

            nodes.add(u)
        
        

        # Where we store the topologically sorted nodes
        res = []
        
        # DFS call
        def dfs(u):

            # BASE CASES

            if u in visited:
                # We don't need to do anything with any branch from here
                return
            
            # This node WAS unvisited, now it is not
            visited.add(u)

            # Call DFS on its neighbours
            for v in adjList[u]:
                dfs(v)

            # Now we can add this node to our result
            res.append(u)

        
        # Call DFS on all nodes
        for u in nodes:
            dfs(u)

        # Technically res is in reverse order now
        # Reverse it!
        resCopy = res.copy()
        res = []
        for i in range(len(resCopy)-1,-1,-1):
            res.append(resCopy[i])

        # Return res
        return res


        pass


if __name__ == "__main__":
    sol = Solution()
    edges = [
        [0,1],
        [0,2],
        [0,3],
        [1,3]
    ]
    print(sol.topologicalSort(edges)) # [0,1,2,3]