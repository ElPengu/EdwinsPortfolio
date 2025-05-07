from typing import List

class Solution:

    def maxCoins(self, nums: List[int]) -> int:

        '''
        - Nums is list of integers
        - ith element is balloon with value nums[i]
        - You must burst all of the balloonw
        - If you burst the ith balloon, you receive 
        -> nums[i-1]*nums[i]*nums[i+1]
        - If j=i-1 OR i+1 is out of bounds, nums[j]=1
        - Find the maximum number of coins

        - EXAMPLE
        - nums: [4,*2*,3,7]->[4,*3*,7]->[*4*,7]->[*7*]->0
        - coins: (4*2*3)+(4*3*7)+(1*4*7)+(1*7*1)=143

        - My intuition is to check every balloon and then 
        recursively pop all the available neighbours
        - AVAILABLEBALLOONS <- balloons available
        - There is definitely repeated work
        
        - Let's say we pop i=3, and i=4 and i=5 are in 
        AVAILABLEBALLOONS
        - This implies that we should have a cache
        - We specifically want to cache when we pop on the 
        same PAIR of balloons
        - DP <- Maps (i1,i2)->coins

        - We can think of this like a matrix now!
        - Let x-axis be the balloons on the LEFT
        - Let y-axis be the balloons on the RIGHT
        - Let N = size(nums)
        - BASE CASES 
        - No balloons on the LEFT AND RIGHT
        - (N,N) -> 1
        - No balloons on the LEFT OR RIGHT
        -> (N,i2) -> (N,i2+1)*nums[i2]*1, (i1,N) -> 1*nums[i1]*(N,i1+1)
        - Now we need to fill the gaps, up to (0,0)
        - INDUCTIVE STEP
        - What exactly do we represent at (N-1,N-1)?
        - We are at a state with exactly ONE (1) balloon on the left 
        and right
        - I.e., we are at the same balloon
        - 
        
        - WAITTTT, I JUST THOUGHT THIS
        - The matrix needs to store POPPED and UNPOPPED balloons
        - LET x-axis be unpopped balloons
        - LET y-axis be popped balloons
        - At (N,N), all balloons are popped... and none are popped
        - DAMN!

        '''
        pass

if __name__ == "__main__":
    sol = Solution()
    nums = [4,2,3,7]
    print(sol.maxCoins(nums)) # 167