from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        - You have array nums with n integers [0,n]
        - There are no duplicates
        - Return the single number in the range 
        that is missing from nums
        - Follow up: Use O(1) space and O(n) time 

        - No guarantee that the numbers are in 
        order...

        - I have to assume this, otherwise there 
        is no indication for what my variable 
        should be initialised to for the bit 
        operations

        - Set res = 0
        - From index 0, if res XOR nums[i] != 0, 
        then that number is missing!
        - Increment res each loop 
        '''
        
        res = 0
        for i in range(len(nums)):
            if res^nums[i] != 0:
                return i
            res += 1

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3]
    print(sol.missingNumber(nums)) # 0
    nums = [0,2]
    print(sol.missingNumber(nums)) # 1
    nums = [0,1,2,3,4,5,7,8,9,10,11,12]
    print(sol.missingNumber(nums)) # 6
    nums = [3,0,1]
    print(sol.missingNumber(nums)) # 2