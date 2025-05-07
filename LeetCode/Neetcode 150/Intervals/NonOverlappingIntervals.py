from typing import List

class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        '''
        - intervals[i] = [start_i, end_i]
        - Return the MINIMUM number of intervals 
        you need to remove for the rest to be 
        non-overlapping

        - NOTE: intervals are non-overlapping even 
        if they have a common point
        - [1,3] and [2,4] are overlapping
        - [1,2] and [2,3] are non-overlapping

        - This is from the blind 75!

        - Consider [[1,2],[2,3],[3,4]]
        - Now we introduce [1,3]
        - [[1,2],[2,3],[3,4],[1,3]]
        - We could remove [1,3]... OR we could 
        remove [[1,2],[2,3]]
        - The solution is to remove [1,3], but what 
        is the algorithm that we used to determine 
        this?

        - BRUTE FORCE
        - Consider removing or not removing each 
        interval, two choices
        - O(2^n) time <- two choices
        - We can do better

        - GREEDY
        - We could order by the start point or 
        end point, we'll do by the start point 
        - We will check adjacent intervals
        - Now suppose we have [[1,5],[6,10]]
        - How do we know whether [1,2] overlaps with 
        [3,4]?
        - Clearly, it is because 2<3
        - end_i<=start_i+1 -> NOT OVERLAPPING
        - Okay, what about [[1,5],[4,10]]
        - We see that they overlap
        - end_i>start_i+1 -> OVERLAPPING
        - We have an edge case though
        - Consider [[1,5],[2,3]]
        - They overlap, but now what if [6,7] comes 
        after?
        - What you must understand is that GIVEN they 
        overlap, we must choose one interval to keep
        - Does it not make sense to select the 
        interval with the smaller end point, so 
        that we end as early as possible, lowering 
        the chance we overlap with the NEXT one?
        - Don't see it yet?
        - Consider [[1,10],[5,6],[9,11]], clearly 
        you want to remove [1,10]
        - Consider [[1,5],[3,10],[9,11]]], clearly 
        you want to remove [1,10]
        
        - To summarise
        - We store a value called prevEnd
        - When we see an interval, we check whether 
        start_i >= prevEnd
        -if so we NEVER remove 
        the previous interval, and set prevEnd = 
        end_i
        - Else, they overlap! Therefore we choose 
        to keep the interval that ends the earliest 
        by setting prevEnd=min(prevEnd,end_i), and 
        remove the interval by incrementing a count  

        - O(n log n) time <- Sorting the list
        '''

        # Sort the list of intervals by the start 
        # value
        # Here it also sorts by the end, but that 
        # doesn't matter for this solution
        intervals.sort()

        # Count
        res = 0
        # We maintain the end so far
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            # Go over the remaining intervals
            if start>=prevEnd:
                # The intervals do NOT overlap
                # We march on, seeing that we do 
                # NOT need to delete the previous 
                # interval
                prevEnd = end
            else:
                # We overlap!
                # We remove ONE of the intervals
                # Hence increment count
                res+=1
                # Now we minimise prevEnd between 
                # the two intervals
                prevEnd = min(end, prevEnd)

        return res

if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,2],[2,4],[1,4]]
    print(sol.eraseOverlapIntervals(intervals)) #1
    intervals = [[1,2],[2,4]]
    print(sol.eraseOverlapIntervals(intervals)) #0
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    print(sol.eraseOverlapIntervals(intervals)) # 1
    intervals = [[1,2],[1,2],[1,2]]
    print(sol.eraseOverlapIntervals(intervals)) # 2