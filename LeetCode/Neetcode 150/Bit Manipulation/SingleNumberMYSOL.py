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
        - ...

        - No idea how to do this with O(1) extra 
        space

        '''

        pass

if __name__ == "__main__":
    sol = Solution()
    nums = [3,2,3]
    print(sol.singleNumber(nums)) # 2
    nums = [7,6,6,7,8]
    print(sol.singleNumber(nums)) # 8