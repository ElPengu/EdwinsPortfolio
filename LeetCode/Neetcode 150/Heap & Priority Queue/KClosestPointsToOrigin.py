from typing import List
import heapq

class Solution:

    def kClosest(self, points: List[List[int]], k)->List[List[int]]:
        # We can use a minheap for this to get 
        # O(n log n)
        # The first index is used by heapify to 
        # create the minheap
        # Heapify actually is O(n), not O(n log n)
        # 
        # We pop k times, and the pop operation is 
        # O(log n)
        # Therefore, we get to O(k log n)

        # Set the minheap as an array initially
        minHeap = []

        # Compute distance for every point
        for x, y in points:
            # We will be lazy since we DON'T need
            # to square root
            dist = (x**2) + y**2

            # Append [distance, x, y] so we sort by
            # distance
            minHeap.append([dist, x, y])

        # Min heap the minHeap
        heapq.heapify(minHeap)
        
        # Create the list
        res = []
        # We pop until k is 0
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k-=1

        return res



    def kClosestMYSOL(self, points: List[List[int]], k)->List[List[int]]:
        import math
        
        # Best option is to use a min-heap
        # 
        # The min-heap must be arranged by euclidean distance from 
        # origin
        # 
        # How do we create the minimum heap so that it is arranged
        # by euclid. distance AND refers to the point?
        # 
        # We could create a hash map mapping distances to points?
        # 
        # In Python, heaps are recognises the first element of a tuple!!
        #
        # We will create a list of tuples = [(euclid dist, point)] <- O(n)
        # Convert the tuple into a heap <- O(n log n)
        # Pop the top K elements <- O(k log n)
        # O(n) + O(n log n) + O(k log n) = O(n log n)
        # > Note that k <= n
        # 
        # 

        # Create list of tuples
        distAndPoints = []
        for point in points:
            # Get x and y coords
            x = point[0]
            y = point[1]

            # Find the euclidean distance to (0,0)
            euclidDist = math.sqrt((x-0)*(x-0) + (y-0)*(y-0))
            
            # Append euclid distance and point
            distAndPoints.append((euclidDist, point))

        # Heapify the list of tuples
        heapq.heapify(distAndPoints)

        # Create a list of closest points
        closestPoints = []

        # Pop the K smallest points
        while len(closestPoints) < k:
            # Pop a euclidean distance point pair
            pair = heapq.heappop(distAndPoints)

            # Get the point at first index
            point = pair[1]

            # Add point to closest points
            closestPoints.append(point)

        
        # Return the closest points
        return closestPoints


if __name__ == "__main__":
    sol = Solution()
    points = [[0,2],[2,2]]
    k = 1
    print(sol.kClosest(points, k)) # [[0,2]]
    points = [[0,2],[2,0],[2,2]]
    k = 2
    print(sol.kClosest(points,k)) # [[0,2],[2,0]]
