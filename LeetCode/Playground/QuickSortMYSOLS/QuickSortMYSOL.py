# FAIL

from typing import List

class Solution:
    # Quick sort: Asks Partition for the position 
    # of the pivot for a sublist
    # Partition: Returns the position of the pivot

    def quickSort(self, nums: List[int]):
        if len(nums)>1:
            # Find position of the pivot using 
            # partition
            pivot = self.partition(nums)
            # Call quick sort on left and right 
            # partitions
            if pivot>-1:
                nums[0:pivot] = self.quickSort(nums[0:pivot])
            if pivot+1<len(nums):
                nums[pivot+1:] = self.quickSort(nums[pivot+1:])
        return nums

    def partition(self, nums: List[int]):
        # Let pivot be the final element
        pivot = nums[-1]
        # Set left and right pointers
        l, r = 0, pivot-1
        # Loop until we cross
        while l<r:
            while l<pivot and nums[l]<nums[pivot]: l+=1
            while r>l and nums[r]>nums[pivot]: r-=1
            tmp = nums[l]
            nums[l]=nums[r]
            nums[r]=tmp
        # Swap pivot if smaller
        tmp = nums[pivot]
        nums[pivot] = nums[l]
        nums[l] = tmp
        # Return pivot
        return pivot

if __name__ == "__main__":
    sol=Solution()
    nums=[4,2,3,1,7,8,6,5,9,0]
    print(sol.quickSort(nums)) # [0,1,2,3,4,5,6,7,8,9]