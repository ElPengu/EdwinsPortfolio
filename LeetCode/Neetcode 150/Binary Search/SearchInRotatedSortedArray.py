from typing import List

class Solution:
    def search(self, nums: List[int], target: int)->int:
        # There is a left and right portion.
        # When nums[l]<=nums[r] then you reduce down to 
        # binary search
        # Otherwise, there is a **pivot**, where the list 
        # goes from max to min
        # If nums[l]<=nums[m], then there is no **pivot**
        # here. Well, in this case we check if our target
        # could occur in the left sublist. If so, we search it
        # 

        # Set a left and right pointer
        l, r = 0, len(nums)-1

        # We use this loop, to deal with the case of len(nums)==1
        while l <= r:
            # Set mid
            mid = l + (r-l)//2

            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]:
                # In this case, the left portion has no pivot, making 
                # it sorted

                if target > nums[mid] or target < nums[l] :
                    # We must search the right portion in this case
                    # This is because the target could not lie in the sorted
                    # left sublist
                    l = mid+1
                else:
                    # The target could lie in the sorted left sublist
                    r = mid-1
            else:
                # The right portion has no pivot, making it sorted
                if target < nums[mid] or target > nums[r]:
                    # The target could not lie in the right sorted sublist
                    # It may lie in the left sorted sublist
                    r = mid - 1
                else:
                    # The target may lie in the sorted right sublist
                    l = mid + 1

        # We have not found a target. So it does not exist in nums
        return -1

    def searchMYSOLUTION(self, nums: List[int], target: int)->int:
        # Extension of find min in sorted array
        # 
        # We find the midpoint value and check whether the target 
        # is equal to it. If so, return the midpoint
        # Else, it is either less than or greater than the target
        # 
        # nums[m]>=nums[l] implies that the pivot (the point from 
        # max to min) does **not** occur here
        # If nums[l]<= target < nums[midpoint] then it may lay in 
        # nums[l:m-1]
        # Else, it may lay in nums[m+1:r]
        # 
        # In the case that nums[m]<nums[l], the pivot occurs in 
        # nums[l:m]
        # If nums[l] <= target < nums[midpoint] then it may lay
        # in nums[m+1:r]
        # Else, it may lay in nums[l:m-1]

        # Set left and right pointers
        l, r = 0, len(nums)-1

        # Loop 
        while (l < r):
            m = l + ((r-l)//2)

            if nums[m] == target:
                # If the midpoint is exactly the solution we break
                break
            if nums[l] == target:
                m = l
                break
            if nums[r] == target:
                m = r
                break
            
            if nums[m] >= nums[l]:
                # The pivot must not occur here

                if target <= nums[m] and target >= nums[l]:
                    # We want to search the left sublist
                    r = m-1
                else:
                    #We want to search the right sublist
                    l = m+1
            else:
                # The pivot must occur here
                
                if target <= nums[m] and target >= nums[l]:
                    # We want to search the right sublist
                    l = m-1
                else:
                    r = m+1

            

        if nums[m] == target:
            return m
        else:
            return -1


if __name__ == "__main__":
    sol = Solution()
    nums = [3,4,5,6,1,2]
    target = 1
    print(sol.search(nums,target)) # 4
    nums = [3,5,6,0,1,2]
    target = 4
    print(sol.search(nums,target)) # -1