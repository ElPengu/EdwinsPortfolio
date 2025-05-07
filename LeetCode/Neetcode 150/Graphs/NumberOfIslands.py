from typing import List
from collections import deque

class Solution:

    def numIslands(self, grid: List[List[str]])->int:

        # Island: connected adjacent lands both horizontally
        # and vertically (all edges are water)
        # Popular with tech companies like Google and Uber
        # If you understand this, you will get graphs - NeetCode
        # One of Neetcode's favourite problems
        # 
        # You can ask yourself how a kid would explore it
        # > A kid would start at some island. He would branch out 
        # until he stops seeing 1s
        # > He'd then go to water and not consider it until he 
        # gets to some land.
        # > Since this land is a part of a NEW island, he would
        # branch out to all connected neighbours
        # > Hence in this example he'd say two islands
        # 
        # We use graph theory to visit neighbouring LAND
        # Since we want to explore ALL the neighbours ON the first
        # later before exploring neighbours of the first layer 
        # this lends itself to BFS or DFS. We use BFS in this 
        # implementation
        # 
        # We keep a set of visited pieces of land globally, and 
        # we loop over every coordinate
        # Don't worry! We only BFS/DFS from land and to neighbouring
        # UNVISITED land, and we keep track of any land that we visit
        # So every coordinate is iterated over EXACTLY once!
        # 

        # Trivial base case
        if not grid:
            return 0
        
        # Set our rows and columns
        rows, cols = len(grid), len(grid[0])
        # A set of visited positions
        visit = set()
        # Islands seen
        islands = 0

        def bfs(r,c):
            
            # Queue
            q = deque()
            # We visit this node!
            visit.add((r,c))
            q.append((r,c))

            while q:
                # Pop from the queue
                row, col = q.popleft()
                # We can go in four directions
                # left, right, up, down
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                # We check every direction row, direction 
                # column pair
                for dr, dc in directions:
                    # We store the coordinates of the 
                    # next possible location
                    r,c = row+dr, col+dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r,c) not in visit):
                        # We only visit an in bounds, UNVISITED, 
                        # piece of LAND
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                # We must not increase islands if we see this 
                # land again
                if grid[r][c] == "1" and (r,c) not in visit:
                    # When we get to an island node we 
                    # BFS on it!
                    bfs(r,c)
                    islands += 1
        
        return islands

    pass


if __name__ == "__main__":

    sol = Solution()
    grid = [
        ["0","1","1","1","0"],
        ["0","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(sol.numIslands(grid)) # 1
    grid = [
        ["1","1","0","0","1"],
        ["1","1","0","0","1"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(sol.numIslands(grid)) # 4