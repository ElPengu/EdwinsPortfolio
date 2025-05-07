from typing import List

class Solution:

    def combinationSum2(self, candidates: List[int], target: int)->List[List[int]]:

        # The idea behind 3Sum helps with duplicates!
        # This is an extention of Combination Sum
        # 
        # We can still use two branches!
        # You sort it! Why? This means that any same
        # values are adjacent
        # So you have two choices
        # CHOICE 1: Include the same value as much 
        # as you want#
        # CHOICE 2: Absolutely do NOT use that same 
        # value!
        # We use a while loop to shift our pointer 
        # until the value changes to fulfil CHOICE
        # 2
        #
        # Time complexity: n*2^n
        # n <- One combo
        # 2^n <- branching 

        res = []
        
        # Sort the input array
        candidates.sort()

        def dfs(i, cur, total):
            # Base cases
            # Total = target
            # Total > target
            # i is out of bounds

            if total == target:
                # We append a copy of cur
                res.append(cur.copy())
                return

            if total > target or i == len(candidates):
                return
            
            # Recursive case

            # Include at index i
            cur.append(candidates[i])
            dfs(i+1, cur, total+candidates[i])

            # Undo
            cur.pop()

            # Skip at index i
            # This is a tiny bit complicated!
            # We want to skip the value of the 
            # element at index i completely
            # ALSO, we must consider the case of 
            # the final elements being all the same,
            # so we must stop comparing if i+1 exceeds
            # candidates
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            # At this point, i+1 is different from i
            # So we move onto index i+1
            dfs(i+1,cur, total)


        dfs(0,[],0)



        # Return res
        return res




if __name__ == "__main__":
    sol = Solution()
    candidates = [9,2,2,4,6,1,5]
    target = 8
    print(sol.combinationSum2(candidates, target)) # [[1,2,5],[2,2,4],[2,6]]
    candidates = [1,2,3,4,5]
    target = 7
    print(sol.combinationSum2(candidates, target)) # [[1,2,4],[2,5],[3,4]]