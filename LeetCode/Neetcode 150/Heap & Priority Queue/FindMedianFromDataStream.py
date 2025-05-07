import heapq

class MedianFinder:

    # Median: 1 element in a list with the partition to its LEFT and 
    # RIGHT being equal, else the middle point of two elements with that
    # property. Whichever is possible
    # 
    # Initial solution: Create an array. Add a number to the correct 
    # position in the array in O(n) time. Find the median in O(1) time
    # 
    # Can we do better than O(n) time for addNum?
    # 
    # Maintain two heaps
    # One heap is labelled small, the other is labelled large
    # The peak of small must be the largest element in the left 
    # partition.
    # The peak of large must be the smallest element in the right
    # partition
    # Finding the median is O(1), as you just pop from the relevant 
    # left/right heap
    # However, to *rebalance* we must ensure that the difference between
    # the heaps is never > 1. Shifting an element to the other heap 
    # in this case is O(log n)
    # Likewise, addNum has the same consideration. To add to either heap
    # is O(log n)
    # Better than O(n)!
    # 
    # Let small be a max heap, and max be a min heap.
    # This way the peak of small is the largest element in the left
    # partition, while the peak of large is the smallest element in
    # the right partition
    
    def __init__(self):
        # large is a min heap, small is a large heap
        # heaps should be equal size
        self.small, self.large = [], []  

    def addNum(self, num: int) -> None:
        # We immediately add num to the partition that
        # it must be in
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        # Now we rebalance the heaps if one partition
        # has more than 1 element in excess than the 
        # other
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # If either partition is unequal, return top
        # of larger partition
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        # Here partitions are equal
        return (-1 * self.small[0] + self.large[0]) / 2.0

    



if __name__ == "__main__":
    medianFinder = MedianFinder()
    print(medianFinder.addNum(1))    # arr = [1]
    print(medianFinder.findMedian()) # return 1.0
    print(medianFinder.addNum(3))    # arr = [1, 3]
    print(medianFinder.findMedian()) # return 2.0
    print(medianFinder.addNum(2))    # arr[1, 2, 3]
    print(medianFinder.findMedian()) # return 2.0