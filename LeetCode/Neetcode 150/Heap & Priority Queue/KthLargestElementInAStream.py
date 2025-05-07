from typing import List
import heapq

class KthLargest:
    # NeetCode feels like this is a medium, not an
    # easy problem!
    # 
    # Note we want the Kth largest, not the Kth 
    # distinct largest
    # [1,2,3,3], K=3 => 2, NOT 1
    # 
    # We must take care of the fact that the stream 
    # may be less than, equal to, or greater than 
    # k in length AT INITIALISATION, but not when 
    # using the add function
    # 
    # We will create a MinHeap of size k BECAUSE 
    # when a number is too SMALL to be in the MinHeap
    # it will NEVER re-enter it since there is 
    # no REMOVE function
    # Why do we take the MINIMUM and remove the MINIMUM
    # from the min heap?
    # 
    # EXAMPLE: Let K = 3
    # [i,i-1,i-2,i-3], we only need the K largest, remove 
    # minimum i-3
    # [i,i-1,i-2], [i-3], The minimum is i-2 <= 3rd largest
    # add(i-1)
    # [i,i-1,i-2,i-1], [i-3], we only need the K largest, remove
    # i-2
    # [i,i-1,i-1], [i-2,i-3], The minimum is i-1 => i-1 <= 3rd largest
    # And so on!
    #
    # Add function calls cost O(log n) time a piece
    # Initialisation is O(n log n) because we create
    # and then pop all excess values
    # 

    def __init__(self, k: int, nums: List[int])-> None:
        # minhead with K largest integers
        
        self.k = k
        self.minHeap = nums

        # Turn minHeap into a heap
        heapq.heapify(self.minHeap)

        # Pop smallest elements, O(log N) for each one
        # This only executes if add more than k 
        # elements
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)



    
    def add(self, val: int)->int:
        # We push onto the heap
        heapq.heappush(self.minHeap, val)

        # Out of the K elements, we pop the smallest 
        # element - O(log n)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # Get the smallest element
        return self.minHeap[0]



if __name__ == "__main__":
    kthLargest = KthLargest(3, [1,2,3,3])
    print(kthLargest.add(3)) # 3
    print(kthLargest.add(5)) # 3
    print(kthLargest.add(6)) # 3
    print(kthLargest.add(7)) # 5
    print(kthLargest.add(8)) # 6

