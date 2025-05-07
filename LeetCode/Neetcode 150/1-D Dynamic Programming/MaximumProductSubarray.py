from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        - Find subarray with the largest product within
        the array and return that product
        - Subarray: contiguous non-empty sequence of 
        elements within an array
        
        - If every num is positive this is trivial
        - But negatives make the sign switch. The 
        fact that this may occur means that we 
        also want to remember when we have a 
        negative product for a sub problem, in case
        we get another negative number
        - In fact, we want the minimum in general!

        - We maintain a max and min for every 
        subproblem
        - Consider [-1,-2,-3,4]
        -> -1 -> [-1,-1]
        -> -1,-2 -> [2, -2]
        -> -1,-2,-3 -> [6,-6]
        -> -1,-2,-3,4 -> [24,-24]

        - Now we want to strictly define how 
        we update curMax and curMin

        - Assume that we have the maximum and
        minimum for a subarray ending at index i-1
        - Now we are at index i
        - curMax
        -> Whether nums[i-1] was positive or negative, 
        curMax could be maximised by multipling it 
        with curMax or curMin 
        ->> nums[i]*curMax, nums[i]*curMin
        -> What if nums[i-1] was zero?
        ->> We will have set curMax to zero, so we 
        want to set curMax to nums[i]
        ->> nums[i]
        -> This all implies that for curMax we want
        max(curMax*nums[i], curMin*nums[i], nums[i])
        - curMin
        -> Literally all of the logic before, but now
        we minimise!
        -> min(curMax*nums[i], curMin*nums[i], nums[i])
        
        '''

        # Initialise res to the maximum value in nums
        # as default
        res = max(nums)

        # Maintain min and max to multiplicative 
        # identity
        curMin, curMax = 1,1

        for n in nums:
            print(f"curMax: {curMax}, curMin: {curMin}")
            # We temporarily hold curMax*n so 
            # that we can use it to calculate
            # curMin too
            tmp = curMax*n

            # Update curMax
            curMax = max(n*curMax, n*curMin, n)
            # Update curMin
            curMin = min(tmp, n*curMin, n)
            res = max(res, curMax,curMin)
        print(f"curMax: {curMax}, curMin: {curMin}")    
        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,-3,4]
    print(sol.maxProduct(nums)) # 4
    nums = [-2,-1]
    print(sol.maxProduct(nums)) # 2
    nums = [7,0,4,3]
    print(sol.maxProduct(nums)) # 0