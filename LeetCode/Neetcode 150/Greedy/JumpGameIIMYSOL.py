from typing import List

class Solution:

    def jump(self, nums: List[int]) -> int:

        '''
        - We have integers nums
        - You can jump from index i up to nums[i] steps
        - You start at nums[0]
        - Minimum number of jumps to last position?
        - There is always a valid answer

        - Can you start at the end like the last one and 
        greedily jump backwards?
        - Do we even need to?
        - Let's say we are at the goal
        - To get here, we want to start from as far back 
        as we can to position furthestBack, because 
        however we get to the goal, we could also land 
        on furthestBack
        - How do we calculate furthestBack efficiently?
        - It seems to be O(n^2) whether you iterate 
        backwards or forwards
        - In fact, I think it has to be: you must check 
        every element before the goal, and at worst-case 
        you will move the goal back one step 
        '''

        # Set goal to final index
        goal = len(nums)-1

        # Set steps that we must take, initially 0
        steps = 0

        for i in range(len(nums)-1,-1,-1):
            if i > goal:
                # Move to next iteration if we are 
                # above the goal
                continue
            
            for j in range(i):
                if j+nums[j] >= goal:
                    # We could reach the goal from here
                
                    # Take a step to the new goal
                    steps += 1

                    # Update goal
                    goal = j

                    # This is the earliest position that 
                    # we could jump from, so break out 
                    # of this loop 
                    break


        return steps


if __name__ == "__main__":
    sol = Solution()
    nums = [2,4,1,1,1,1]
    print(sol.jump(nums)) #2
    nums = [2,1,2,1,0]
    print(sol.jump(nums)) #2