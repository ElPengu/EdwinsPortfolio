from typing import List

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    # Helper function to build graph from adjacency
    # list
    # [[2],[1,3],[2]]
    # Node: List of neighbours
    # Node 1: [2]
    # Node 2: [1,3]
    # Node 3: [2]
    def buildGraph(adjList):
        if not adjList:
            return None

        nodes = {}  # Dictionary to store created nodes

        # Create nodes for each index
        for i in range(len(adjList)):
            nodes[i + 1] = Node(i + 1)  # Nodes are 1-based index

        # Connect nodes according to the adjacency list
        for i, neighbors in enumerate(adjList):
            nodes[i + 1].neighbors = [nodes[n] for n in neighbors]

        return nodes[1]  # Return the first node as the graph's entry point

    # [[2],[1,3],[2]]
    # Node: List of neighbours
    # Node 1: [2]
    # Node 2: [1,3]
    # Node 3: [2]
    def printAdjList(node):
        if not node:
            return
        
        visited = set()  # Track visited nodes to avoid infinite loops
        adjList = {}  # Dictionary to store adjacency list representation

        def dfs(curr):
            if curr.val in visited:
                return
            visited.add(curr.val)
            adjList[curr.val] = [neighbor.val for neighbor in curr.neighbors]
            for neighbor in curr.neighbors:
                dfs(neighbor)

        dfs(node)  # Start DFS traversal

        # Print the adjacency list in order
        for key in sorted(adjList.keys()):
            print(f"{key}: {adjList[key]}")

class Solution:

    def cloneGraph(self, node: Node) -> Node:
        
        # This is a BRILLIANT explanation of how 
        # recursion works
        # We will use recursive DFS
        # We will use a hash map to map nodes 
        # to their deep copies
        # Call 0: We begin at the node and create a 
        # clone. 
        # We check that we have NOT already seen it
        # This is IMPLICITLY true if it is 
        # NOT iN the map
        # We add a mapping of node to clone
        # to the hash map if so
        # Next we use BFS or DFS to branch 
        # out to ALL its neighbours
        # Call 1: Now we create a clone of its 
        # neighbour 
        # We check that we have NOT already seen it
        # This is IMPLICITLY true if it is 
        # NOT iN the map
        # We add a mapping of node to clone
        # to the hash map if so
        # Next we use BFS or DFS to branch 
        # out to ALL its neighbours
        # Etc.
        # Call n: Once we have no more unvisited 
        # neighbours we exit this call, returning 
        # the created copy. 
        # Now we reach call n-1
        # Call n-1: We now have both a deep copy
        # of the node created at call n-1 AND 
        # the nodes created at call n
        # We make the deep copy of the node 
        # created at call n-1 neighbour those
        # created at call n
        # Now we exit this call
        # ...
        # Call 0: We now have both a deep copy
        # of the node created at call 0 AND 
        # the nodes created at call 1
        # We make the deep copy of the node 
        # created at call 0 neighbour those
        # created at call 1
        # 
        # WAIIITTTTTTTT
        # But what about the neighbour itself?
        # Sure, we create the edge 
        # node i -> node i+1
        # But what about node i+1-> node n???
        # This is where we really bring the genius
        # in!
        # See, what ever node we are at, we 
        # call dfs on EVERY neighbour
        # If the neighbour happens to already 
        # be in the map, it has been "seen", right?
        # So we immediately return the deep copy
        # as seen in the map
        # This means that if we look more closely at 
        # the example...
        # Call n: Calls DFS on neighbours at level 
        # n-1, gets the deep copies of these nodes
        # adds these as neighbours to the deep copy 
        # at node n 
        # So at call n-1, we already have the 
        # adjacency in direction n-1->1!

        # We create a mapping of old to new
        oldToNew = {}

        def dfs(node):

            # See if the node is in our hash map
            if node in oldToNew:
                return oldToNew[node] 
            
            # We have NOT added this to our map
            # We create a copy and add to our hash 
            # map
            copy = Node(node.val)
            oldToNew[node] = copy

            # We go through every neighbour in DFS
            for nei in node.neighbors:
                # We neighbour this to the copy
                copy.neighbors.append(dfs(nei))
            # Return the copy
            return copy

        # Call dfs on the original node
        # If no graph return nothing
        return dfs(node) if node else None
    

if __name__ == "__main__":
    sol = Solution()

    adjList = [[2],[1,3],[2]]
    # Build the graph
    graph = Node.buildGraph(adjList)
    print(Node.printAdjList(sol.cloneGraph(graph))) # [[2],[1,3],[2]]

    adjList = [[]]
    # Build the graph
    graph = Node.buildGraph(adjList)
    print(Node.printAdjList(sol.cloneGraph(graph))) # [[]]

    adjList = []
    # Build the graph
    graph = Node.buildGraph(adjList)
    print(Node.printAdjList(sol.cloneGraph(graph))) # []
