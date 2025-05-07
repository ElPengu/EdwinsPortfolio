from typing import List

class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        '''
        - We have a network of n directed nodes
        - Nodes labelled 1 to n
        - We have directed edges in times
        - times[i] = (source node, dest. node, time 
        taken)
        - We have integer k, the node that we send a 
        signal from
        - Minimum time for all n nodes to receive the
        signal

        - Hmmm
        - Let's say we have nodes k,i0
        - The shortest time will be the one edge k->i0
        - We are really being asked: out of the shortest
        paths from k to each node, which path is the 
        longest?

        - PHASE 1: Find the minimum path
        - We initialise a HASH MAP {node: distance}
        - We use DFS to visit nodes starting at the
        node k
        - For a DFS call we must
        -> Detect whether we are about to create a 
        cycle - We pass a set of vertices visited
        in THIS DFS CALL as a parameter
        -> Know the edge that we are coming from - 
        we pass in the edge vertices used to enter
        this node as a parameter
        -> Know the time taken to traverse the edge -
        we pass the time associated with this edge as
        a parameter
        - Using the DFS call we want to determine the
        minimum path for each node
        -> DFS is called recursively by nodes
        -> Each node that calls it must know the 
        minimum time needed for node k to reach it
        -> Each time it adds up the time of the edge 
        used to reach it (passed in as a parameter) 
        and the minimum time needed by the previous 
        node along this path (determined by the HASH
        MAP)
        -> It updates the hash map with this time
        -> Only now does it call DFS on all of its
        neighbours


        - PHASE 2: Find the maximum out of the minimum 
        paths
        - Trivially maintain a maxPath variable 
        initialised to INF
        - Update INF

        - PHASE 3: Determine that every node can be 
        visited
        - Maintain a VISITED set
        - Every time you VISIT a node you add it to 
        the set
        - IF size(VISITED) = size(nodes): Return maxPATH
        - ELSE: RETURN -1 

        - For the first problem in the network 
        graphs pattern I displayed a pretty deep 
        understanding of it

        - I am proud, before I would have crashed 
        out on this problem!
        '''
        
        pass


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