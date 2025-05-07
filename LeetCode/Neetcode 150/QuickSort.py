class Solution:

    def quicksort(self, arr, left, right):
        # Just check if there are at least two elements
        if left < right:
            # We get the position of the pivot element
            # Our helper 
            partition_pos = self.partition(arr, left, right)
            
            # We call quick sort on all elements LESS
            # than the pivot element
            self.quicksort(arr, left, partition_pos-1)

            # We call quick sort on all elements 
            # GREATER than the pivot element
            self.quicksort(arr, partition_pos+1, right)
        
        # Return arr
        return arr


    def partition(self, arr, left, right):
        # Define the left and right pointers
        i = left
        j = right - 1

        # Set the pivot to the last element to be 
        # lazy
        pivot = arr[right]

        # Shift i and j until they cross
        while i < j:
            # While i is not at the end of the array
            # and is less than the value at the 
            # pivot, we increment i
            while i < right and arr[i] < pivot:
                i += 1

            # While j is NOT at the start of the 
            # array and is greater than or equal
            # to the pivot, we shift it
            while j > left and arr[j] >= pivot:
                j-=1

            # Swap i and j
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        # We ONLY swap pivot with i if pivot is 
        # smaller
        if arr[i] > pivot:
            arr[i], arr[right] = arr[right], arr[i]

        # Now we return the index of the pivot
        return i



if __name__ == "__main__":
    sol = Solution()

    arr = [22, 11, 88, 66, 55, 77, 33, 44]
    print(sol.quicksort(arr, 0, len(arr)-1))
