from typing import List

class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Across left and top of heights is pacific
        # Across bottom and right is atlantic
        # Water flows from a cell to a neighbouring cell which has 
        # the same level or lower
        # Water flows from a cell into the sea
        # Water can flow from four directions
        # How to find cells where we can flow into BOTH oceans?
        # 
        # Okay, let's try to understand this on 3 hours of sleep...
        # Every unit of time water must flow SOMEWHERE
        # A cell on the edge will direct water to the sea
        # Now we move to its neighbours
        # If a neighbour is in bounds AND 
        # has not deposited to either sea AT THIS UNIT OF TIME
        # AND has the same or higher level of water, then it will
        # deposit water to it 
        # 
        # This makes a lot more sense now!
        # We set up a set for pacific cells and for atlantic cells
        # We also create a set of VISITED cells
        # Also create a set of pacificAndAtlantic cells
        # We create a queue of all cells neighbouring a sea
        # BASE CASE: all cells by the sea are added to the corresponding
        # sets for pacific and for atlantic cells
        # If you add to the set for one sea and it is already in the 
        # other, add it to pacificAndAtlantic cells
        # Now we begin to loop
        # Pop cells at this layer
        # Check neighbours
        # If neighbour fits conditions, add corresponding sea
        # If the neighbour is already in the set for the other sea,
        # add it to pacificAndAtlantic cells
        # After checking a layer, add all cells to VISITED
        # 
        # At the very end return pacificAndAtlanticCells
        # 
        #  


        pass


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