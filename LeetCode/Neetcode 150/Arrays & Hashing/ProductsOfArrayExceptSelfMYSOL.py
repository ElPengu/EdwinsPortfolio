from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # We want the products of everything to the left 
        # and right of the index, non-inclusive of itself

        # Declare left and right arrays
        left = [1]*len(nums)
        right = [1]*len(nums)

        # Populate left
        for i in range(1, len(nums)):
            left[i]=left[i-1]*nums[i-1]
        
        # Populate right
        for i in range(len(nums)-2,-1,-1):
            right[i]=right[i+1]*nums[i+1]

        # Declare output array
        output = [1]*len(nums)

        # Populate output
        for i in range(len(nums)):
            output[i]=left[i]*right[i]

        return output

        pass

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,4,6]
    print(sol.productExceptSelf(nums)) #[48,24,12,8]
    nums = [-1,0,2,3,4]
    print(sol.productExceptSelf(nums)) # [0,-24,0,0,0]