from typing import List
import heapq

class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        # We choose two heaviest stones, smash them, 
        # and add the remnant of any stone left
        # I.e. Let y>x IF y-x>0 ADD y-x
        # 
        # We use a maxheap
        # Converting stones into heap is O(n) 
        # operation
        # We will get the maximum n times. Since
        # getting the maximum is O(log n), we 
        # get to O(n log n)
        # 
        # O(n log n) + O(n) = O(n log n) time
        # 
        # Note that we will use a minheap, but 
        # by negating values in it we get the 
        # effect of a maxheap
        # 
        # Note that in case that there are NO stones,
        # we append a 0

        # Negate all values in list
        stones = [-s for s in stones]

        # Heapify the stones
        heapq.heapify(stones)
        
        # Smash stones until there is 1 left
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            # first >= second
            # Since we work with negatives, the
            # second will be heavier in magnitude
            # I.e. abs(second) >= abs(first) 

            if second > first:

                # y >= x, y-x
                # first>=second, first - second
                # Simple mathematical manipulation 
                # with negatives 
                heapq.heappush(stones, first - second)

        # In case there are no stones, we return 0
        stones.append(0)

        # Return the remaining stone
        return abs(stones[0])
        

if __name__ == "__main__":
    sol = Solution()
    stones = [2,3,6,2,4]
    print(sol.lastStoneWeight(stones)) # 1
    stones = [1,2]
    print(sol.lastStoneWeight(stones)) # 1
