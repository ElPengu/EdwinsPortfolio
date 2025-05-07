from typing import List

class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        '''
        - We have an array of POSITIVE integers
        - Can we PARTITION into TWO subsets where 
        both have the same sum

        - INTELLIGENT REFRAMING OF PROBLEM
        - How can you partition nums into two subsets
        where ONE (1) partition sums to EXACTLY 
        sum(nums)/2

        - BRUTE FORCE APPROACH
        -> Consider [1,5,11,5]
        -> Our target is 11
        -> Do we choose 1 or nothing?
        -> For either choice, so we choose 5 or nothing
        -> For either of THESE choices we choose 11 or 
        nothing

        - DP APPROACH
        - We want to abstract the idea of including vs
        not including an element in a subset
        - We are only interested in sums, so at every 
        element we ask ourselves: what exactly are the 
        sums of the subsets that we can generate through
        including vs not including this element for every 
        subset that we have created so far?
        - We will hold a set of sums, initially empty
        -> {}
        - Consider [1,5,11,5], target = 11
        - BASE CASE: We could include or not include any 
        elements
        -> {0}
        - We could include 5 or not include 5
        -> {0,5} <- not include 5 vs include 5
        - We could include 11 or not, so consider all 
        that are currently in the set
        -> {0,5,11,16}
        - We could include 5 or not, so consider all 
        that are currently in the set
        -> {0,5,11,16,10,21}
        - We could include 1 or not, so consider all 
        that are currently in the set
        -> {0,5,11,16,10,21,1,6,12,17,22}
        - Finished evaluating
        - RETURN 11 IN SET

        - O(sum(nums)) space <- there are N+1 possible sizes
        - O(sum(nums)) time <- For every possible size you 
        would do constant time addition
        '''

        if sum(nums)%2:     
            # Trivial case: Odd sized nums cannot be
            return False
        
        # Generate a set
        dp = set()
        # BASE CASE
        dp.add(0)

        # We find the target sum for one of the subsets
        target = sum(nums)//2

        for i in range(len(nums)-1,-1,-1):
            # Go through in reverse as we are used to it

            # Generate a new set for nextDP
            nextDP = set()

            for t in dp:
                
                if (t+nums[i]) == target: 
                    # A neat optimisation so that we immediately return
                    # if we find the target

                    return True

                # For every element in dp as it was before
                # considering index i we PUSH the result 
                # of including index i vs not including 
                # index i to dp

                # Include element at i GIVEN it does not exceed target
                if t+nums[i] <= target:
                    # Without this condition we 
                    # would not be O(sum(nums)) as 
                    # we'd be able to exceed target
                    nextDP.add(t+nums[i])
                
                # Do not include element at i
                nextDP.add(t)

            # Reassign dp to the next dp set
            dp = nextDP

        # See if we have found a target       
        return True if target in dp else False


if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4]
    print(sol.canPartition(nums)) # True
    nums = [1,2,3,4,5]
    print(sol.canPartition(nums)) # False
