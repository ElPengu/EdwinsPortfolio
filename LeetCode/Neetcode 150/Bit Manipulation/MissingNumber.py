from typing import List

class Solution:
    '''
    - You have array nums with n integers [0,n]
    - There are no duplicates
    - Return the single number in the range 
    that is missing from nums
    - Follow up: Use O(1) space and O(n) time 

    - No guarantee that the numbers are in 
    order!

    - There are two methods
    - The XOR method
    - The SUM method
    
    - The XOR method
    - The trick is to realise that Y XOR Y is 0
    - We generate the entire range of integers, 
    excluding 0
    - We set res to 0, thus capturing the 
    integer excluded
    - We set res to itself XOR every element in 
    the entire range and that of nums
    - All identical numbers will cancel out, 
    except our missing number! 

    - The SUM method
    - Find Q, the sum of nums
    - Find P, the sum of the entire possible 
    range
    - Return P-Q   
    '''

    def missingNumberXOR(self, nums: List[int]) -> int:
        
        
        # Generate entire list
        allElements = [i for i in range(1, len(nums)+1)]
        
        # Set res to 0
        res = 0

        for i in nums:
            res=res^i
        for i in allElements:
            res=res^i
        
        return res
    
    def missingNumberAND(self, nums: List[int]) -> int:
        sum = 0
        N = len(nums)
        for i in range(N+1):
            sum+=i
        for n in nums:
            sum-=n
        return sum


if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3]
    print(sol.missingNumberXOR(nums)) # 0
    print(sol.missingNumberAND(nums)) # 0
    nums = [0,2]
    print(sol.missingNumberXOR(nums)) # 1
    print(sol.missingNumberAND(nums)) # 1
    nums = [0,1,2,3,4,5,7,8,9,10,11,12]
    print(sol.missingNumberXOR(nums)) # 6
    print(sol.missingNumberAND(nums)) # 6
    nums = [3,0,1]
    print(sol.missingNumberXOR(nums)) # 2
    print(sol.missingNumberAND(nums)) # 2