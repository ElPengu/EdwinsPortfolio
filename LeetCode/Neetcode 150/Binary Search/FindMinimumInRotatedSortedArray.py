from typing import List

class Solution:

    def findMin(self, nums: List[int]) -> int:
        # We use the fact that it was originally ascending and that the
        # values are unique to our advantage
        # 
        # We could look for the pivot (max->min) but our solution will 
        # work slightly differently
        # 
        # We shall search for the minimum value
        # We set up left and right, and find the midpoint. We assume 
        # that the midpoint is the minimum value
        # We want to decide whether we will find the minimum value in 
        # nums[l:m] or nums[m+1:r]
        # Well, there is only one pivot. 
        # If we find that nums[l]<=nums[m] then the pivot **cannot**
        # occur in nums[l:m] because that sublist is monotonically 
        # increasing. So it must occur in nums[m:r]. More specifically, 
        # the minimum must occur in nums[m+1:r]
        # Else, the pivot **must** occur in nums[l:m], because a 
        # massive drop happens somewhere in that sublist
        # Note that if we ever see that left is less than right, 
        # then the minimum is left.

        # We set a result variable
        res = nums[0] #  Arbitrarily set

        # Left and right pointers set up
        l, r = 0, len(nums) - 1

        # Typical loop
        while l <= r:

            if nums[l] < nums[r]:
                # If we ever reach this case, then the pivot 
                # occurs at indices [-1,0] (for this sublit). 
                # So we return the left
                res = min(res, nums[l])
                break
            
            # Find the midpoint
            m = l + (r-l)//2

            # We set the result to be the midpoint if necessary
            res = min(res, nums[m])
        
            if nums[m] >= nums[l]:
                # In this case, there are further increases in the 
                # right sublist, so move left pointer up
                l = m + 1
            else:
                # In this case there is a massive drop (and hence the 
                # pivot) in the left sublist. We move the right pointer
                # down
                r = m - 1
        return res

        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [3,4,5,6,1,2]
    print(sol.findMin(nums)) # 1
    nums = [4,5,0,1,2,3]
    print(sol.findMin(nums)) # 0
    nums = [4,5,6,7]
    print(sol.findMin(nums)) # 4