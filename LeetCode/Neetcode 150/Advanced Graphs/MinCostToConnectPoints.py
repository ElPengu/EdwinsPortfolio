from typing import List
import heapq

class Solution:

    def minCostConnectPoints(self, points: List[List[int]])->int:
        '''
        - We have a list of points on a 2D plane
        - Cost of connecting two points is Manhattan distance
        - We want the Minimum Spanning Tree
        
        - There is no graph though?!
        - Don't worry, we will just create all the possible edges

        - After this we will apply Prim's algorithm (we could use Kruskal's
        but Neet says that Prim's is usually better)
        - O(n2 log n) time
        -> n2 <- connect each point
        -> log n <- a heap is used

        - Let's say we have a graph with five nodes, we want to join
        them into a tree. This means we'll need four edges (refer to 
        tree definition)
        - To achieve the MST we want to get this tree with as little
        weight as possible

        - PRIM'S ALGORITHM
        - Perform BFS on an arbitrary node
        - ADD node to VISIT hash set
        -> VISIT hash set <- adding same node twice creates a cycle
        - ADD (weight, destination node) per node from node to MINHEAP
        -> MINHEAP <- Maintains the node that we could reach AND the weight
        of creating the connection. We put the weight FIRST so that the 
        minheap is ordered by weight
        -> NOTE we don't add EDGES to the minheap because we are only 
        interested in the WEIGHT of the graph
        - We STOP when we have visited all five nodes!

        - We maintain a COST variable, updated based on the cost of reaching
        the NEXT node
        '''

        # We begin by creating the adjacency list
        N = len(points)

        # We use numbers as labels for nodes
        # i: list of [cost, node]
        adj = {i:[] for i in range(N)}
        # Build out the adjacency list
        for i in range(N):
            # Get x and y coordinates
            x1, y1 = points[i]
            for j in range(i+1,N):
                # Get x and y coordinates
                x2, y2 = points[j]

                # Get Manhattan distance
                dist = abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])

        # Prim's

        # Start of with a cost of 0
        res = 0
        # A set of visited node
        visit = set()
        # We start at node 0, which costs 0 to get to trivially
        minH = [[0,0]] # [cost,point]

        while len(visit) < N:
            # Pop from the minimum heap
            cost, i = heapq.heappop(minH)

            if i in visit:
                # We don't want to revisit
                continue
            
            # Add the cost of this fresh, new node
            res += cost

            # We visit this node
            visit.add(i)

            for neiCost, nei in adj[i]:
                # We add the costs to reach new neighbours now that we can
                # go from node i
                if nei not in visit:
                    # Again, we do not want to visit new nodes
                    heapq.heappush(minH, [neiCost, nei])
        
        # We have the cost of our MST
        return res


if __name__ == "__main__":
    sol = Solution()
    points = [[0,0],[2,2],[3,3],[2,4],[4,2]]
    print(sol.minCostConnectPoints(points)) # 10