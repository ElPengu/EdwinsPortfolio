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

        - If you remember house robber 1, you
        calculated the max you could rob up 
        to house 0, then house 1, and so on, 
        given that you cannot rob adjacent 
        houses

        - We can reuse the answer to house robber
        1!

        - Let houseRobber1 be a helper function
        - Run houseRobber1 on subarray of all elements
        except the first, and then except the last
        - This works because you are NOT allowed 
        to rob the first and last house together, so 
        in PRACTISE you just have two separate 
        subproblems where you exclude house 0 vs house
        N-1

        - Also note that if we have only 1 house we would
        skip the first and last house and thus return 0
        - So we also consider the raw value of the first
        house

        - The max of these three values is the answer!

        - Simple!
        
        - O(n) extra time
        - O(1) extra space
        '''

        # If there is only one house then we'd get 0 
        # from the helper function, but we'd want the
        # value of the house. Hence nums[0]
        # We must call helper on all except house 0 and 
        # then on all except house N-1
        return max(nums[0], 
                   self.helper(nums[1:]), 
                   self.helper(nums[:-1]))


    def helper(self, nums):
        # Helper function from house robber 1
        
        # We initialise rob1 and rob2
        rob1, rob2 = 0, 0

        for n in nums:
            # Store what rob2 was
            temp = rob2
            # Calculate max at house n, store in rob2
            # We could rob rob1 and n OR rob2 (before
            # n)
            rob2 = max(rob1+n, rob2)
            # Update rob1 to temp, i.e. what rob2 was
            rob1 = temp

        # Rob2 will hold the max value by robbing up to 
        # house N
        return rob2
            


        pass
        

if __name__ == "__main__":
    sol = Solution()
    nums = [3,4,3]
    print(sol.rob(nums)) # 4
    nums = [2,9,8,3,6]
    print(sol.rob(nums)) # 15
    nums = [1]
    print(sol.rob(nums))