from typing import List
import heapq

class Solution:

    def findKthLargestQUICKSORT(self, nums: List[int], k: int)->int:
        # We could use a max heap
        # Heapify <- O(n)
        # Pop k times <- O(k log n)
        # 
        # O(n) + O(k log n)
        # 
        # There is a ANOTHER solution that is O(n) 
        # AVERAGE case, but it is O(n2)
        # So depends on what time complexity you want 
        # This is called QUICK SORT
        # 
        # As you know quick sort works by partitioning
        # the array about a pivot in a recursive 
        # manner
        # 
        # Here is a useful explanation of this 
        # implementation
        # You have a pointer p where all elements 
        # less than pivot lay to the left, and 
        # greater to the right
        # You go through the list
        # When you see an element less than or 
        # equal to the pivot, you want it to lie
        # to the left of p, so you leave it where 
        # it is and shift p
        # Otherwise you want it to lie beyond p,
        # so you leave p here. This means that
        # when you see a lesser or equal value
        # than it, it will be swapped past p
        # At the final iteration the pivot is
        # swapped with p anyway, so if p "stalls"
        # before some values larger than the pivot,
        # the pivot will be thrown before all of 
        # them! 
        # 
        # 
        # 
        # Average case is O(n)
        # Why?
        # We will only do quick sort on the portion
        # of the list containing the index that 
        # the Kth largest value may lie in
        # On average the pivot will be the middle 
        # value. So the size of the search array 
        # will halve
        # 
        # Leading to...
        # n+n/2+n/4+... = 2n => O(n)
        # 
        # Worst case O(n2)
        # The searchable array decreases in size by 1
        # at a time
        # n+(n-1)+(n-2)...=n2-1 => O(n2)

        # Get the index of the Kth largest element
        k = len(nums) - k
        
        # Recursive quick select algorithm
        def quickSelect(l,r):
            # Choose the right most value as pivot,
            # p is at the left most index
            pivot, p = nums[r], l

            # Go from left index  up to BUT NOT 
            # INCLUDING right
            for i in range(l,r):
            
                if nums[i]<= pivot:
                    # We have reached an index 
                    # with a value less than the
                    # pivot

                    # swap p and i
                    nums[p], nums[i] = nums[i], nums[p]
                    
                    # Now we increment p
                    p += 1

            # Swap p with pivot/right-most value
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                # The k index lies to the left 
                # of the pivot, so we search the 
                # left partition
                return quickSelect(l, p-1)
            elif p < k:
                # The k index lies to the right
                # of the pivot, so we search the 
                # right partition
                return quickSelect(p+1, r)
            else:
                # The k index is exactly at the 
                # pivot
                return nums[p]

        # Run on entire array
        return quickSelect(0, len(nums)-1)


    def findKthLargestMAXHEAP(self, nums: List[int], k: int)->int:
        # We want the Kth largest, not Kth distinct
        # largest
        # Without sorting, we could use a heap
        # Create a max heap <- O(n)
        # Pop k elements <- O(k log n)
        # Return kth element <- O(1)
        # 
        # O(n) + O(k log n) + O(1) = O(k log n)
        # 
        
        # Literally just get the kth largest value
        # using this function!
        return heapq.nlargest(k, nums)[-1]


if __name__ == "__main__":
    sol = Solution()

    nums = [2,3,1,5,4]
    k = 2
    print("MAXHEAP")
    print(sol.findKthLargestMAXHEAP(nums, k)) # 4
    print("QUICKSORT")
    print(sol.findKthLargestQUICKSORT(nums, k)) # 4

    print()
    nums = [2,3,1,1,5,5,4]
    k = 3
    print("MAXHEAP")
    print(sol.findKthLargestMAXHEAP(nums, k)) # 4
    print("QUICKSORT")
    print(sol.findKthLargestQUICKSORT(nums, k)) # 4