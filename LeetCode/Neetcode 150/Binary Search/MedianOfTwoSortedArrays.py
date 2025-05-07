from typing import List

class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int])->float:
        # We cannot merge two array. The worst case would be O(n+m)
        # 
        # What is exactly a median? A middle value
        # For a list of 13 elements, there are 6 elements to the left 
        # and 6 elements to the right of the median. I.e. left and right 
        # partition
        # For a list of 12 elements, there are 6 elements to the left 
        # and 6 elements to the right. The median is the middle of the 
        # last element of the left partition and the first of the right 
        # partition
        # 
        # We use this idea of partitions!
        # We begin by finding the total length of nums1 and nums2. 
        # (len(nums1)+len(nums2))//2 -> length of left and right 
        # partition
        # Next we find the middle of the nums1. We assume that elements 
        # nums[0:m] gives us the left partition of elements in nums1
        # NOTE: len(nums[0:m])<len(leftPartition) intuitively (my 
        # understanding)
        # We immediately set the left partition in nums2 based on the 
        # size of the left partition of nums1
        # We want to make sure that every element in the general 
        # left partition is less than every element in the general 
        # right partition.
        # We need to ask ourselves: if the right-most value in each 
        # array less than the left-most value in the corresponding array?
        # 
        # Finally you calculate the median using the minimum of the 
        # left-most value of the right partition and the right-most 
        # value of the left partition
        # 
        # Note that if the comparisons mentioned above fail, you update 
        # nums1 using binary search to update the middle!
        # 
        # For edge cases we default to [-math.inf,...,math.inf] for both
        # arrays
        # 
        # log(min(n,m))
        
        # Set variables A and B
        A, B = nums1, nums2

        # Find total length
        total = len(nums1)+len(nums2)
        # The size of the left partition (always floor to deal with 
        # even vs odd total)
        half = total//2

        # We set A to be the smaller of the arrays
        if len(B) < len(A):
            A, B = B, A

        # Set left and right
        l, r = 0, len(A)-1
        # Lazily While True because we have a guaranteed median
        while True:
            i = l + ((r-l)//2) # middle value in A
            j = half - i - 2 # Since j and i start at 0, we subtract 2 to get index


            # If ij is out of bounds, then we are saying that we want 
            # a partition with values less than in that list. Default 
            # to negative infinity
            # If ij+1 is out of bounds, then we are saying that we want 
            # a partition with values greater than in that list. Default
            # to positive infinity
            Aleft = A[i] if i >= 0 else float("-infinity")# Left-most of A right partition
            Aright = A[i+1] if (i+1) < len(A) else float("infinity") # Right-most of A left partition
            Bleft = B[j] if j >= 0 else float("-infinity") # Left-most of B right partition
            Bright = B[j+1] if (j+1) < len(B) else float("infinity") # Right-most of B left partition

            # Now we see if the comparisons for the partitions are correct
            if Aleft <= Bright and Bleft <= Aright:
                
                if total%2:
                    # Odd length
                    #The median is exactly one value
                    
                    return min(Aright, Bright)
                else:
                    # The median is the middle of two adjacent values
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                # We have too many elements from A
                # Reduce size of left partition from A
                r = i - 1
            else:
                # We have too few elements from A
                # Increase the size of right partition from A
                l = i + 1


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1,2]
    nums2 = [3]
    print(sol.findMedianSortedArrays(nums1, nums2)) # 2.0
    nums1 = [1,3]
    nums2 = [2,4]
    print(sol.findMedianSortedArrays(nums1, nums2)) # 2.5