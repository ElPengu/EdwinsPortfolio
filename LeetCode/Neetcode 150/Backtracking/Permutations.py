from typing import List

class Solution:

    def permute(self, nums: List[int])->List[List[int]]:
        # Permutation: The number of ways that something can
        # be ordered
        # What we will do is interesting, we will 
        # break this down into sub problems with a 
        # single branch
        # 
        # Consider [1,2,3]
        # BRANCH 1: Returns all permutations of [1,2,3]
        # BRANCH 2: Returns all permutations of [2,3]
        # BRANCH 3: Returns all permutations of [3]
        # BRANCH 4: Returns all permutations of []
        # 
        # So permutations of [] is []
        # Permutations of [3] is [3]
        # Interestingly, permutations of [2,3] can
        # be said to be lists where 2 appears ahead
        # of OR behind 3. So [2,3] and [3,2]
        # Now permutations of [1,2,3] can be said 
        # # to be lists where 1 appears in front 
        # of, in the middle of, or behind [2,3]
        # and [3,2] 
        # If we use [2,3], we can get [1,2,3], 
        # [2,1,3] and [2,3,1]
        # If we use [3,2] we can get [1,3,2], [3,1,2] 
        # and [3,2,1]
        # So overall, we insert the current value 
        # into every position within the permutations
        # for the rest of the list
        # 
        # Overall time complexity is 
        # O(n!*n2) time
        # n! <- all permutations
        # n <- Inserting at index i
        # n <- We do n insertions 
        # 
        # O(n!*n) space if we do NOT count the output
        # Due to multiple copies (his words)
        #  


        # Base case: nums is 0
        if len(nums) == 0:
            return [[]]

        # We call permute on all element except the
        # first
        perms = self.permute(nums[1:])
        res = []

        # Go through every permutation
        for p in perms:
            # Go through all indices that we could
            # insert at, incl. the end
            for i in range(len(p) + 1):

                # We use a copy so that we don't 
                # overwrite
                p_copy = p.copy()
                # Insert at index i the first element
                # in nums
                p_copy.insert(i, nums[0])
                # Append p_copy to the result
                res.append(p_copy)

        return res

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3]
    print(sol.permute(nums)) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    nums = [7]
    print(sol.permute(nums)) # [[7]]

