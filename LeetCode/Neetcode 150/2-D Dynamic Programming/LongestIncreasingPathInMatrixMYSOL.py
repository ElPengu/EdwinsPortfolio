from typing import List

class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
        - 2D grid of integers
        - Every integer >= 0
        - To form a path you may move horizontally or vertically
        - Return the length of the longest strictly increasing path

        - Note on the definition of a path: vertices nor edges may 
        repeat

        - What is the base case for a strictly increasing path?
        - I believe that we must start at every position in the matrix, 
        because there is no way to determine where such a path may start 

        - Okay, what do you do when you start from an arbitrary position
        - You want to know the length of the longest strictly increasing 
        path by going left, right, up, or down

        - Okay, hold on...
        - This implies that you can hold a cache where every position is 
        mapped to the length of the longest strictly increasing path by 
        going through THAT position
        - So you start at a position, and you keep on searching every 
        path until you reach a "deadend" position
        - Deadend position: a position holding a number greater than any 
        of its neighbours
        - Then you can back track
        
        - With this framing, a bottom-up solution would be to start AT 
        THE DEADEND and then work your way backwards
        -> E.g., start at deadend (i,j) with length 0, so its neighbours 
        get the max of whatever length it maps to (default 0) and 1

        - I have a prototype for a solution!!!
        - Map every position (i,j) to path length 0 in a cache
        - Start from every position as if it is the dead end
        - Search every neighbour recursively until no position has a 
        neighbour with a smaller value
        - For each neighbour visited, set 
        DP[i][j] = max(DP[i][j], pathLength+1)

        - I feel like there is repeated work here
        - We don't need to keep on searching when DP[i][j]>pathLength+1
        - Why?
        - Because if DP[i][j] is set, then we have already searched the 
        neighbours of DP[i][j]

        - Optimised solution
        - Map every position (i,j) to path length 0 in a cache
        - Start from every position as if it is the dead end
        - Search every neighbour recursively until no position has a 
        neighbour with a smaller value
        - For each neighbour visited:   
        -> IF DP[i][j]< pathLength+1: 
        ->>DP[i][j] = max(DP[i][j], pathLength+1)

        - Now this feels really good
        - Let's go over run time
        - O(m*n) time <- Since we start from every position
        - O(m*n) time <- At every position we might create a NEW path 
        in the worst case of starting at the end of a path each time
        - O((m*n)^2) <- O(m*n)+O(m*n)

        - This implies that we should iterate from the position that 
        maps to the largest number each time, so that we cover as much 
        of the path each time
        - I don't think I can work out the time complexities from this 
        optimisation YET, since I have 30 seconds, but here is my 
        optimal solution

        - Optimisal solution
        - Map every position (i,j) to path length 0 in a cache
        - Start from every position FROM LARGEST TO SMALLEST as if it is 
        the dead end
        - Search every neighbour recursively until no position has a 
        neighbour with a smaller value
        - For each neighbour visited:   
        -> IF DP[i][j]< pathLength+1: 
        ->>DP[i][j] = max(DP[i][j], pathLength+1)

        '''


        pass


if __name__ == "__main__":
    sol = Solution()
    matrix = [[5,5,3],[2,3,6],[1,1,1]]
    print(sol.longestIncreasingPath(matrix)) # 4
    matrix = [[1,2,3],[2,1,4],[7,6,5]]
    print(sol.longestIncreasingPath(matrix)) # 7
