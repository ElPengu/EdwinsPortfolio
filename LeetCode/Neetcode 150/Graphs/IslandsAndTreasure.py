from typing import List
from collections import deque

class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # We have obstacles/water that cannot be traversed marked -1
        # 0 marks a gate/treasure
        # INF marks an empty room. 
        # We want distance from empty room/land cell
        # 
        # You may be tempted to use DFS, but this is inefficient!
        # DFS would be O((mn)2) as we have to do DFS from every 
        # position to ensure that we minimise the position for 
        # each position relative from every possible start position
        # We can remove repeated work by doing BFS
        # A BFS solution would not work if we start from the rooms
        # However if we start from a gate, we know that all
        # positions at the first layer of neighbours in 1
        # Now, what about multiple gates?
        # We do BFS from every gate **simultaneously**
        # This way, whenever we expand 1 layer, you set the 
        # distances for all not in VISITED nodes, and only add nodes 
        # to the queue which are not in VISITED
        # Naturally we expand in every possible direction: up, down, 
        # left, and right. 
        # Think about it logically, if you move 1 step at a time 
        # from every gate, then the first time that a position is 
        # visited will strictly be from the closest gate!
        # O(m*n) time, space <- We visit every node ONCE, store 
        # VISITED nodes

        # Get dimensions of grid
        ROWS, COLS = len(grid), len(grid[0])
        # Create set of visited nodes
        visit = set()
        # Set a queue
        q = deque()

        # Helper function to add neighbours to queue
        def addRoom(r,c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                (r,c) in visit or grid[r][c] == -1):
                # This determines whether a position is invalid
                # If the row index is out of bounds
                # If the column index is out of bounds
                # If we have already VISITED this position, and 
                # therefore set its minimum distance
                # If we are at a wall
                return
            
            # We now visit this node
            visit.add((r,c))

            # Append this node to the hash set
            q.append([r,c])



        # We add all gate/treasure coordinates to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))

        # Initialise distance to 0
        dist = 0
        while q:
            # For every node at layer N, we 
            # add all neighbouring nodes 
            # at layer N+1
            for i in range(len(q)):
                # Pop row and column from queue
                # This is the first layer
                r, c = q.popleft()

                # Set the value to dist
                grid[r][c] = dist

                # We add all four adjacent rooms to 
                # the queue with abstracted function
                # addRoom
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)

            # Increment distance by 1 as 
            # we move to the next layer
            dist +=1
        # Return the grid
        return grid


if __name__ == "__main__":
    sol = Solution()

    grid = [
            [2147483647,-1,0,2147483647],
            [2147483647,2147483647,2147483647,-1],
            [2147483647,-1,2147483647,-1],
            [0,-1,2147483647,2147483647]
            ]

    print(sol.islandsAndTreasure(grid)) 
    '''
    [
    [3,-1,0,1],
    [2,2,1,-1],
    [1,-1,2,-1],
    [0,-1,3,4]
    ]
    '''

    grid = [
            [0,-1],
            [2147483647,2147483647]
            ]
    
    print(sol.islandsAndTreasure(grid))
    '''
    [
    [0,-1],
    [1,2]
    ]
    '''