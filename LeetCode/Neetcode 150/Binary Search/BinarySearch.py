from typing import List
import math


class Solution:
    def binary_search(self, nums: List[int], target: int) -> int:
        # A very standard algorithm
        # Takes O(log n) time because 
        # the size of the problem keeps on halving 
        # With size n, it will take x iterations, 
        # with 2^x = n -> log2(n) = x

        # Set 2 pointers
        l, r = 0, len(nums)-1

        # Use less than or equal to so that we only 
        # exit if there is no solution
        while l <= r:
            # Find midway point using floor
            m = l + ((r - l) // 2)  
            
            # If the midpoint does not point to the 
            # solution, do not include it in the 
            # next iteration!
            if nums[m] > target:
                r = m-1
            elif nums[m]<target:
                l = m+1
            else:
                #The midpoint will point to 
                # the solution
                return m
            
        #If we exit the loop, then there is no solution
        return -1 

        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [-1,0,2,4,6,8]
    target = 4
    print(sol.binary_search(nums, target)) # 3
    nums = [-1,0,2,4,6,8]
    target = 3
    print(sol.binary_search(nums, target)) # -1