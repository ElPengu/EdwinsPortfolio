from typing import List

class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # We made a mistake in understanding initially,
        # so let's understand this question first
        # -> I was on 3 hours of sleep to be fair
        # This is NOT asking you about rates of flow, 
        # this water is not flowing every unit of 
        # time or whatever
        # We are asking for the oceans that water 
        # in a cell COULD end up in
        # -> Imagine if you are offered to go to 
        # any cell of equal or less height, and you 
        # wanted to reach the sea. It is within THIS 
        # framing that the question is set up 
        # 
        # Across left and top of heights is pacific
        # Across bottom and right is atlantic
        # Water flows from a cell to a neighbouring cell which has 
        # the same level or lower
        # Water flows from a cell into the sea
        # Water can flow from four directions
        # 
        # We use a DFS solution, but we could do BFS 
        # We start from the cells by the 
        # pacific ocean and the atlantic ocean
        # We start at X ocean, and we see its neighbours that can 
        # reach it and which has not been VISITED. These neighbours
        # can reach X ocean.
        # We keep a set of atlantic cells and pacific ocean
        # If a cell can reach both pacific and Atlantic ocean then that 
        # cell can reach BOTH oceans!
        # 
        # We specifically start at row 0 and 1. 
        # Nodes at row 0 -> pacific
        # Nodes at row N-1 -> atlantic  
        # What about nodes at
        # -> column 0 -> pacific
        # -> column N-1 -> atlantic
        # We'll cover these nodes separately!
        # 
        # O(m*n) time,space


        # Get the dimensions of the grid
        ROWS, COLS = len(heights), len(heights[0])

        # Keep hash set of cells by pacific and atlantic
        pac, atl = set(), set()

        # Define the DFS function 
        def dfs(r,c,visit,prevHeight):
            if ((r,c) in visit or 
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                heights[r][c] < prevHeight):
                # If we have visited this position already, OR
                # OR if we are out of bounds
                # OR we are at a lower height than the calling 
                # node
                return
            
            # We have visited this node. Add it to visit!
            visit.add((r,c))

            # Call dfs on neighbours
            dfs(r+1,c,visit, heights[r][c])
            dfs(r-1,c,visit, heights[r][c])
            dfs(r,c+1,visit, heights[r][c])
            dfs(r,c-1,visit, heights[r][c])


        # Go through every position in the first row
        # I.e. every column
        for c in range(COLS):
            # Row is 0, every column
            # We run DFS on this position
            # We pass in the visit set for the pacific ocean
            # We also pass in the previous heigh to check against
            dfs(0, c, pac, heights[0][c])
            # We do the same for atlantic ocean bordering nodes
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        # Also the first and last row will be the pacific or atlantic
        for r in range(ROWS):
            # Column is 0 for first row
            # Column is N-1 for last row
            dfs(r,0,pac,heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])
        
        # Go through every position and check if it is in both oceans
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res


if __name__ == "__main__":
    sol = Solution()

    heights = [
                [4,2,7,3,4],
                [7,4,6,4,7],
                [6,3,5,3,6]
                ]
    print(sol.pacificAtlantic(heights)) # [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]

    heights = [[1],[1]]
    print(sol.pacificAtlantic(heights)) # [[0,0],[0,1]]