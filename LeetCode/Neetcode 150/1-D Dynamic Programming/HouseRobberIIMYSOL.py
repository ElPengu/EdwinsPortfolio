from typing import List

class Solution:

    def rob(self, nums: List[int]) -> int:
        '''
        - nums[i] = money at house i
        - house i neighbours i+1 and i-1
        - house 0 neighbours N-1 and 1
        - house N-1 neighbours N-1 and 1

        - You cannot rob two adjacent houses
        - Maximum amount of money?

        - This is weird
        - So you cannot rob the end houses too
        - How would you represent this?
        
        - Intuitively you could start at house 1 
        and 2
        - You find the max value you could get 
        at house N-2 and N-1
        - Only now do you consider house 0
        - You return max(nums[0]+nums[N-2],nums[N-1])
        '''

        N = len(nums)

        # Initialise rob1 and rob2
        rob1, rob2 = 0,0

        
        for i in range(1, N):
            # Loop until we consider all houses EXCLUDING
            # house 0
            
            temp = rob2
            
            rob2 = max(nums[i]+rob1, rob2)
            rob1 = temp

        if N > 3: rob1 += nums[0]
        
        return max(rob1, rob2)
        

if __name__ == "__main__":
    sol = Solution()
    nums = [3,4,3]
    print(sol.rob(nums)) # 4
    nums = [2,9,8,3,6]
    print(sol.rob(nums)) # 15
    nums = [1]
    print(sol.rob(nums)) # 1