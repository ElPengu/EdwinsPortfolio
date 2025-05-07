from typing import List
from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # You have nodes from 0 to n-1 and undirected edges
        # Check if it is a valid tree
        # Reverse thinking, what is NOT a tree
        # A graph which is NOT CONNECTED is NOT a tree
        # A graph with a CYCLE is NOT a tree
        # Yup, that's it!
        # 
        # At a high level
        # Select a node n
        # Perform DFS or BFS (we'll use DFS)
        # If you see a node TWICE then return FALSE
        # Complete DFS
        # If you have NOT seen EVERY node then return FALSE
        # Else return true 
        # 
        # Each time that we complete DFS on a child of a node 
        # then we cancel that child to say that we have visited it
        # We maintain a CYCLE set which contains nodes that are
        # being visited in an ongoing DFS call
        # 
        # Note that since we have undirected edges you must check 
        # both "sides" of the edge for a node in the DFS call
        # 
        # How to select all children of a node?!
        # We are dealing with a list of undirected edges AND 
        # [0,1] is the same as [1,0]
        # Hold on
        # We could loop over the edge list every time, but that 
        # seems quite inefficient
        # WAITTTTT
        # We could have a hash map where every node points to its 
        # neighbour
        # Then we use the hash map as an ADJACENCY LIST
        # 
        # Updated solution
        # At a high level
        # Create adjList hash map {node: neighbour list}
        # Loop over edge list and populate adjList
        # Select arbitrary node i
        # Perform DFS or BFS (we'll use DFS) ON adjlist
        # If you see a node TWICE then return FALSE
        # Complete DFS
        # If you have NOT seen EVERY node then return FALSE
        # Else return true 
        # 
        # If only I had the time to fix my code
        # Screw it, I'll do it quickly!!! Gimme 10 mins over time

        # Select node 0 arbitrarily
        node = 0

        # Create a hash map for adjacency list
        adjList = defaultdict(set)

        # Populate adjList
        for edge in edges:
            adjList[edge[0]].add(edge[1])
            adjList[edge[1]].add(edge[0])

        # Maintain a set of nodes explored in an ongoing DFS call
        cycle = set()

        # We maintain a set of nodes that we have visited
        visit = set()

        # DFS function
        def dfs(cur):
            # Base cases

            # We have seen this node before so we are in a cycle!
            if cur in cycle:
                return False
            
            # We are not in a cycle

            # Add this to cycle set as we are visiting it
            cycle.add(cur)

            # Perform DFS on all the children of this node
            for child in edges[cur]:
                # Break the connection parent->child
                adjList[cur].pop(child)
                
                if not dfs(child):
                    # If even one node is bad the whole graph is, 
                    # force False all the way back up
                    return False
                else:
                    # As we bubble back up we break connection child->parent
                    adjList[child].pop(cur)

            # We are no longer searching this node in this DFS call
            # Remove from cycle
            cycle.remove(cur)

            # Add this to the list of visited nodes
            visit.add(cur)

            # Valid node
            return True

        if not dfs(node):
            # At least one "bad" node was found
            # Not a tree
            return False

        # Check if we have all the nodes and return
        return len(visit) == n


if __name__ == "__main__":
    sol = Solution()
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print(sol.validTree(n, edges)) # true
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    print(sol.validTree(n, edges)) # false