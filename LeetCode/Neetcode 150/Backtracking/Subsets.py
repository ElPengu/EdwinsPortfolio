from typing import List

class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        # We will use backtracking
        # For every element we have a choice. We can 
        # either add an element or NOT add it
        # We have 2^n possible subsets. Since a subset is 
        # worst case O(n), at best we can get O(n*2^n)
        # Backtracking is the most efficient way with this
        # in mind
        # 
        # Backtracking
        # Imagine a tree. We start with an empty set at 
        # level 0.
        # Next, we have a choice of adding the first element
        # or not. We create two separate branches for this
        # decision.
        # We now have two nodes at level 1.
        # We have the exact same choice for the second index
        # and level 2
        # In this way we will generate all subsets at the 
        # **final** level
        # 
        # We will use a recursive DFS approach to do this 
        # backtracking
        # It is somewhat counter-intuitive, I will present
        # as lean an explanation as I can
        # DFS CALL 1 - Adding state
        # We add the element at the ith index to a global
        # subset list, until all indices have been considered.
        # We return at this stage. This brings us to the 
        # popping state
        # DFS CALL 2 - Popping state
        # We pop the last element added SO FAR. Now we enter 
        # a DFS call for the next index, bringing us to 
        # the adding state again
        # Since the adding state comes before the popping state
        # we always return after trying to ADD
        # 
        # 
        
        # We store subsets here
        res = []

        # Create a subset array
        subset = []
        def dfs(i):
            # Index i is what we are considering

            if i >= len(nums):
                # We are out of bounds. Return a copy of the subset
                res.append(subset.copy())
                return
            
            # Decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # Decision to not include nums[i]
            # We POP the element that we added in the previous call
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res
            


if __name__ == "__main__":

    sol = Solution()
    nums = [1,2,3]
    print(sol.subsets(nums)) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    nums = [7]
    print(sol.subsets(nums)) # [[],[7]]