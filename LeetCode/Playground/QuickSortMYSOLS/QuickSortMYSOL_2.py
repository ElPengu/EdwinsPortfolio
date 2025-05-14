# Right after 1 review of pseudocode (from wiki) on ANKI

from typing import List

class Solution:
    # Quick sort: Asks Partition for the position 
    # of the pivot for a sublist
    # Partition: Returns the position of the pivot

    def quickSort(self, A: List[int], lo: int, hi: int):
        # Are we in bounds?
        if lo >= hi or lo < 0: 
            return

        # Find pivot
        pivot = self.partition(A, lo, hi)

        # Call quick sort on left and right partitions
        self.quickSort(A, lo, pivot-1)
        self.quickSort(A, pivot+1, hi)

        return A
        

    def partition(self, A: List[int], lo: int, hi: int):
        # Set pivot value to be at hi
        pivot = A[hi]

        # Set boundary for pivot position at lo
        i = lo

        for j in range(i, len(A)-1):

            if A[j]<=pivot:
                # We put A[j] behind the boundary for the 
                # left partition

                # Swap A[j] and A[i]
                tmp = A[j]
                A[j] = A[i]
                A[i] = tmp

                # Advance boundary for pivot position
                i+=1
        
        # All elements before i are smaller or equal to pivot
        # No elements at or after i are smaller or equal to 
        # the pivot
        
        # Swap values at A[i] and A[hi]
        tmp = A[i]
        A[i] = A[hi]
        A[hi] = tmp

        # Return position of pivot, now exactly i
        return i

if __name__ == "__main__":
    sol=Solution()
    nums=[4,2,3,1,7,8,6,5,9,0]
    print(sol.quickSort(nums, 0, len(nums)-1)) # [0,1,2,3,4,5,6,7,8,9]