from typing import List

class Solution:

    def rob(self, nums: List[int]) -> int:
        '''
        - nums[i]-> money in house i
        - i neighbours i-1 and i+1
        - We cannot rob two adjacent houses
        - What is the most money that we can rob?

        - We must rob EITHER house n-1 or n-2
        - At house i we have two options
        -> OPTION 1: rob house i+2 and house i
        -> OPTION 2: rob house i+1

        - INITIALISE ONE, TWO = nums[N-2], nums[N-1]
        - IF LEN(nums) == 2: RETURN max(ONE,TWO)
        - i = N-3
        - WHILE i >= 0:
        -> temp = ONE
        -> ONE = max(nums[i]+TWO, ONE)
        -> TWO = temp
        -> i-=1
        - RETURN max(ONE,TWO)
        '''

        # Store length of nums
        n = len(nums)

        # Initiliase ONE and TWO
        one, two = nums[n-2], nums[n-1]

        # Trivial case
        if len(nums) == 2: return max(one,two)

        # Initialise index i
        i = n-3

        while i >= 0:
            # Store whatever cost from one is
            temp = one
            # Find out whether we should use house i or not
            one = max(nums[i]+two,one)
            # Update two
            two=temp
            # Move to previous house
            i-=1
        
        # Start at house 0 or 1, whichever is best cost
        return max(one,two)
        


if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,3,3]
    print(sol.rob(nums)) # 4
    nums = [2,9,8,3,6]
    print(sol.rob(nums)) # 16