from typing import List

class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        '''
        - You are given a non-empty array of 
        integers
        - Every integer appears twice except for one
        - Return the integer that appears only ONCE
        - The solution must take O(n) time
        - The solution must take only O(1) extra 
        space

        - Problems
        - Using O(1) space to consider each number 
        - Parsing the logic of how XOR can be used 
        to determine the single number

        - Using O(1) space to consider each number 
        - We use XOR, setting res to 0
        - We loop over every number
        
        - Parsing the logic of how XOR can be used 
        to determine the single number
        - We set res to 0, and XOR it with each 
        value in nums
        - Consider nums = [...,x,...,x,...]
        - We get something like res^...^x^...^x^... 
        - XOR is associative, so we rewrite it as 
        res^...^(x^...)^...^(x^...)
        - XOR is commutative, so we rewrite it as 
        res^...^(x^x)^...
        - Finally, we use the fact that x^x=0, 
        getting: res^...^(0) => res^...
        - This applies to every duplicate
        - We use the fact that 0 XOR X => X to see 
        that the single number will be left
        '''

        # Set res to 0
        res = 0
        for n in nums:
            # Loop over every number, XOR with res
            res^=n
        # Return single number
        return res

if __name__ == "__main__":
    sol = Solution()
    nums = [3,2,3]
    print(sol.singleNumber(nums)) # 2
    nums = [7,6,6,7,8]
    print(sol.singleNumber(nums)) # 8