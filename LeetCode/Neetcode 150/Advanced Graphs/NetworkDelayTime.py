from typing import List
from collections import defaultdict, heapq


class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ''' 
        -This uses a pretty rare problem where you
        need to use DJIKSTRA'S algorithm
        - We have times as weights, edges are 
        directed, and nodes are numbered 1 to n
        
        - Djikstra's algorithm uses BFS and it needs
        a MinHeap
        - MinHeap: {(path, Node)}
        - LET MinHeap = {0, k} for initial node K
        - Use BFS to get all neighbours of node k
        - POP from MinHeap
        - LET node i0,i1,i2... be neighbours of node
         k where i0_path <= i1_path <=i2_path <= ... 
        - INSERT [(i0_path, i0),...] INTO MinHeap in
        this order
        - Repeat this approach until the MinHeap is 
        empty

        - NOTE: we might put multiple paths for the
        same node
        - One way of dealing with this is to 
        specifically UPDATE the length to the node
        only if it decreases

        - Let E = edges
        - Let V = Vertices
        - At most E = V2
        - MinHeap depends on edges
        - O(E) = O(V2) SPACE <- MinHeap is worst case 
        - O(log E) = O(V2) <- So each MinHeap operation 
        - We call MinHeap for every edge, since we add
        - We get Elog(V2) -> 2Elog(V) -> ElogV
        - Hence O(E log V) time
        '''
        
        # We create an adjacency list to represent edges
        edges = defaultdict(list)

        for u,v,w in times:
            # Add each edge
            edges[u].append((v,w))

        # Trivially speaking we travel for no time
        # to get to node k
        minHeap = [(0,k)]
        
        # Visit set to avoid cycles in BFS
        visit = set()
        # This is the minimum time to reach the last
        # node
        t = 0

        while minHeap:
            # Pop a node
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                # We skip a node if we have visited it
                # Wait, but we want the minimum path,
                # I hear you cry
                # Notice the subtlety: we only visit
                # a node AFTER popping it, NOT when
                # pushing it
                # At the moment we pop it, the 
                # shortest path to n1 has already been 
                # found
                # All subsequent paths must take longer
                # because they must go through nodes
                # which take longer to reach the source
                # node!!!
                continue
            
            # We visit this node
            visit.add(n1)
            # We update t
            t = max(t,w1)

            # Now for the BFS part
            for n2, w2 in edges[n1]:
                # Go over neighbours of n1
                if n2 not in visit:
                    # We add the new node and how
                    # long it takes k to reach it
                    heapq.heappush(minHeap, (w1+w2, n2))

                # If we enter here then we have already
                # visited n2
                # This specifically means that at some
                # point the shortest path found by 
                # Djikstra's algorithm was to n2
                # No path evaluated after this point 
                # will be smaller, so the path to n2
                # cannot be minimised further! 
    
        # After this is done executing we should get 
        # the time IF it is possible
        return t if len(visit) == n else -1

if __name__ == "__main__":
    sol = Solution()
    times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]] 
    n = 4 
    k = 1
    print(sol.networkDelayTime(times,n,k)) # 3
    times = [[1,2,1],[2,3,1]]
    n = 3 
    k = 2
    print(sol.networkDelayTime(times,n,k)) # -1