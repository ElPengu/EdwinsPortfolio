from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #We first create output array
        #We want to know what the product is of 
        #everything to the LEFT of the current 
        #index, and to the RIGHT of the current 
        #index
        #
        #So we need to create a left array, where 
        #every index has the product of all values
        #to the LEFT of that index
        #Similar idea for right array
        #
        #In this way... 
        #forall i: output[i]=left[i]*right[i]
        
        #1. Create output array
        output = []

        #2. Create left and right arrays
        left = [1]
        right = [1]

        #Loop over other nums indices
        for i in range(1, len(nums)):
            #We multiply the last element added
            #to left by the preceding element in 
            #nums
            left.append(left[-1]*nums[i-1])

        #Loop from end to beginning over nums
        for i in range(len(nums)-2, -1, -1):
            #Muliply the last element added to 
            #right by succeeding element in 
            #nums
            right.append(right[-1]*nums[i+1])

        #Reverse right array
        rightCopy = []
        for r in right:
            rightCopy.insert(0, r)
        right = rightCopy

        #Append values to output using left, right
        for i in range(len(nums)):
            output.append(left[i]*right[i])

        
        return output

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,4,6]
    print(sol.productExceptSelf(nums)) #[48,24,12,8]
    nums = [-1,0,2,3,4]
    print(sol.productExceptSelf(nums)) # [0,-24,0,0,0]