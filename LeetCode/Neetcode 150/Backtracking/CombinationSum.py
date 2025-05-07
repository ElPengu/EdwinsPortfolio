from typing import List

class Solution:

    def combinationSum(self, nums: List[int], target: int)->List[List[int]]:
        
        # Unlimited number of choices of any number implies BACKTRACKING
        # At every index we have a choice: add or do not add the value
        # We stop adding a value if we exceed the target. At this point
        # we peel back the last added element and move to the NEXT index
        # to try and add
        # We are guaranteed that 2 <= nums[i] <= 30 so we will either 
        # stop at or beyond the target
        # We maintain a total variable to compare to 
        # target
        # 
        # O(2^t) time where t is target 

        # We return a list of lists
        res = []

        # Values added so far
        cur = []

        def dfs(i, cur, total):
            if total == target:
                # We append a copy of cur
                res.append(cur.copy())
                # Done with this branch, return
                return
            if i >= len(nums) or total > target:
                # We cannot find a solution

                # No more indices OR total is beyond
                return
            
            # We append at the current index
            cur.append(nums[i])
            # Now we go into the decision of 
            # including this value
            dfs(i, cur, total+nums[i])

            # Second decision is to NOT include the
            # value
            # We peel back the addition
            cur.pop()
            # Now we move to the next index
            dfs(i+1, cur, total)


        dfs(0, [], 0)

        

        # We return res
        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [2,5,6,9] 
    target = 9
    print(sol.combinationSum(nums, target)) # [[2,2,5],[9]]


    nums = [3,4,5]
    target = 16
    print(sol.combinationSum(nums, target)) # [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]

    nums = [3]
    target = 5
    print(sol.combinationSum(nums, target)) # []