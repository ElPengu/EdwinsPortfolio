from typing import List

class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        - We have non-overlapping intervals
        - interval[i] = [start_i, end_i]
        - intervals is sorted in ascending order by start_i
        - You arge given newInterval = [start, end]
        - Insert newInterval into intervals such that intervals 
        is still in ascending order
        - You may merge overlapping intervals
        - NOTE: Intervals are non-overlapping if they have no common 
        point

        - Doesn't seem... horrible
        - Let start, end = newInterval[0], newInterval[1]
        - Loop over interval[i], interval[i+1]
        - If start >= interval[i][0] and start <= interval [i+1][0], 
        STOP
        - Determine if you must merge with newInterval with interval[i], 
        if so merge and update newInterval
        - Now determine if you must merge newInterval with 
        interval[i+1], if so merge and update newInterval
        - Add these to res 

        - Wait, what if newInterval encompasses like 8 intervals
        - I think it has to be the FIRST interval[i] where its end is...
        - Hm
        '''

        # To hold the intervals with newInterval inserted
        res = []

        # Set start and end
        start, end = newInterval[0], newInterval[1]

        # Store size of intervals
        N = len(intervals)
        
        # It is easier to deal with the case that intervals is size 0, 
        # size 1, and size > 1 separately
        if len(intervals) == 0:
            # Just add newInterval to res
            res.append(newInterval)
        elif len(intervals) == 1:
            # Set first and second, where first is the interval with 
            # the smaller start value
            first, second = intervals[0], newInterval
            if first[0] > second[0]:
                temp = second
                second = first
                first = temp

            # Check if there is a common point by seeing 
            # the end value of first and the start value of second 
            if first[1] >= second[1]:
                # Overlap!
                res.append([first[0], second[1]])
            else:
                # Don't overlap!
                res.append(first)
                res.append(second)
            
        else:
            # Iterate over intervals
            for i in range(N):
                
                
                pass

        # Return res
        return res
        

if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,3],[4,6]], newInterval = [2,5]
    print(sol.insert(intervals, newInterval)) # [[1,6]]
    intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]
    print(sol.insert(intervals, newInterval)) # [[1,2],[3,5],[6,7],[9,10]]