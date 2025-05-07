from typing import List

class Solution:

    def subsetsWithDup(self, nums: List[int])->List[List[int]]:

        # We want to avoid duplicates subsets.
        # A duplicate subset would occur if we branch out, and 
        # on both branches we end up considering two of the same
        # value
        # We must sort nums so that each time we branch, we 
        # ensure that one of the branches does NOT consider
        # a duplicate (read: adjacent and same) value
        # 
        # Beyond this, we either include a value at an index or 
        # we exclude it
        # 
        # Time complexity: O(n*2^n)
        # 2^n <- Possible subsets
        # n <- Maximum length of a subset

        res = []

        # We sort nums <- O(n log n)
        nums.sort()

        

        def backtrack(i, subset):
            # Check if we have considered all indices
            if i == len(nums):
                # Add a copy of combination to res
                res.append(subset.copy())
                # Return
                return
            
            # We have not considered all combinations

            # CHOICE 1: Add the value at this index
            subset.append(nums[i])
            backtrack(i+1, subset)

            # Unroll choice 1
            subset.pop()
            # CHOICE 2: Add the next DIFFERENT value 
            # IF it exists
            while i+1 < len(nums) and nums[i]==nums[i+1]:
                i=i+1

            # Now index i+1 has the next DIFFERENT value
            # OR there is no different value in the rest
            # of the list
            backtrack(i+1, subset) 
        
        # Call dfs on index i=0 and empty subset
        backtrack(0, [])

        return res


if __name__ == "__main__":

    sol = Solution()
    nums = [1,2,1]
    print(sol.subsetsWithDup(nums)) # [[],[1],[1,2],[1,1],[1,2,1],[2]]
    nums = [7,7]
    print(sol.subsetsWithDup(nums)) # [[],[7],[7,7]]