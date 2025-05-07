from typing import List

class Solution:

    def jump(self, nums: List[int]) -> int:

        '''
        - We have integers nums
        - You can jump from index i up to nums[i] steps
        - You start at nums[0]
        - Minimum number of jumps to last position?
        - There is always a valid answer

        - We can solve this with a greedy solution, 
        which is O(n)
        - Funnily enough, the DP solution would be 
        O(n^2)
        - For greedy, we use a BFS-like solution
        - We have a segment of size 1 for where 
        we could reach in 0 steps (i.e. index 0)
        - We generate a segment of all positions 
        that we could land on OUTSIDE this segment
        - We move to this new segment
        - We repeat until the goal is in our segment

        - Example: nums=[2,3,1,1,>4<]
        - Let us rewrite this: [[2],3,1,1,>4<]
        - We are on level 0
        - The goal is not in the segment
        - Using 2 in our segment, we can get to 
        [2,[3,1],1,>4<]
        - We are on level 1
        - The goal is not in the segment
        - Using this segment, which portion can 
        we reach OUTSIDE this portion?
        - Using 3, we could get to [2,3,1,[1,>4<]]
        - Using 1, we could reach [2,3,1,[1],>4<]
        - Hence: [2,3,1,[1,>4<]]
        - We are on level 2
        - The goal IS in our segment
        - Return 2
        '''

        # Count the number of steps
        res = 0

        # Set a left and right pointer initialised 
        # to 0
        l = r = 0

        while r < len(nums)-1:
            # The first time that r is at or beyond 
            # the final index is when we can reach 
            # it

            # Who can jump the farthest
            # Assume we cannot jump at all
            farthest = 0
            for i in range(l, r+1):
                # We loop across the window from l 
                # up to AND INCLUDING r
                
                # We store the farthest that we could
                # jump
                farthest = max(farthest, i+nums[i])

            # Set left pointer to position after right
            l=r+1
            # Set right pointer to farthest that we 
            # can reach
            r=farthest

            # We take a step
            res+=1
        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [2,4,1,1,1,1]
    print(sol.jump(nums)) #2
    nums = [2,1,2,1,0]
    print(sol.jump(nums)) #2