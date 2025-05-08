from typing import List


class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr, L, M, R):
            
            # We get the left and right halves of the array
            # We need copies so that we do not overwrite values
            # in arr
            # Note that in Python arr[x,y] includes x but NOT Y
            left, right = arr[L:M+1], arr[M+1:R+1]

            # We set three pointers
            # i: for array
            # j: left half
            # k: right half
            i, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    # Put left value into the actual array
                    arr[i] = left[j]

                    # We increment the j pointer to look at the 
                    # next in the left half
                    j+=1
                else:
                    # The right pointer must be smaller!
                    arr[i] = right[k]

                    # We must increment the k pointer
                    k+=1
                
                # Move to the next value to add
                i+=1
            
            # Now one of the halves will not be exhausted!
            while j < len(left):
                nums[i] = left[j]
                j+=1
                i+=1
            
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1

        def mergeSort(arr, l, r):
            # l and r show us the subarray that we are working with

            if l == r:
                # At this point, we just return
                return arr
            
            
            # Find the midpoint
            m = l+(r-l)//2
            
            # We want to run merge sort on the left and right subarrays
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)

            # We abstract the merging part
            merge(arr, l, m, r)

            # Now the array is sorted!
            return arr
        
        # Call merge sort on the left and right boundaries
        return mergeSort(nums, 0, len(nums)-1)


        
if __name__ == "__main__":
    sol = Solution()
    nums = [5,2,8,4,2,3,8,6,3,1,0,7]
    print(sol.sortArray(nums)) # [0, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 8]