from typing import List

class Solution:

    def rob(self, nums: List[int]) -> int:
        '''
        - Google really likes DP problems, and this
        is an excellent one to start with

        - nums[i]-> money in house i
        - i neighbours i-1 and i+1
        - We cannot rob two adjacent houses
        - What is the most money that we can rob?

        - We must rob EITHER house n-1 or n-2
        - At house i we have two options
        -> OPTION 1: rob house i+2 and house i
        -> OPTION 2: rob house i+1

        - We will use a top-down solution here
        - Imagine we start at house 0 and 1, with 
        labels rob1 and rob2 respectively
        - We move to house 2
        - Now we ask ourselves: is nums[0]+nums[2]
        better than nums[1]?
        - We store this as rob2
        - We set rob1 to what rob2 was previously
        - Now rob2 will hold the maximum value we 
        could get by the time we reach house 3
        - We can repeat this until we get to house 
        N-1   
        '''

        # Initialise rob1 and rob2 to 0
        rob1, rob2 = 0, 0

        for n in nums:
            # Loop over every house

            # Store The max value we can get at house
            # i in temp
            temp = max(n+rob1, rob2)
            # Store value we can get by house i-1 in 
            # rob 1
            rob1=rob2
            # Store value we can get by house i in 
            # rob 2 
            rob2=temp
        return rob2
        


if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,3,3]
    print(sol.rob(nums)) # 4
    nums = [2,9,8,3,6]
    print(sol.rob(nums)) # 16