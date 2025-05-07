from typing import List

class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        - Blind 75 problem!

        - We have non-overlapping intervals
        - interval[i] = [start_i, end_i]
        - intervals is sorted in ascending order by start_i
        - You arge given newInterval = [start, end]
        - Insert newInterval into intervals such that intervals 
        is still in ascending order
        - You may merge overlapping intervals
        - NOTE: Intervals are non-overlapping if they have no common 
        point

        - Consider [[1,2],[3,4],[5,6]]
        - Let's say that newInterval is [X,0]
        - We would naturally insert it at the start and keep the rest
        - [[X,0],[1,2],[3,4],[5,6]]
        - How about [7,X]
        - Similarly we'd intert is at the end
        - [[1,2],[3,4],[5,6],[7,8]]
        
        - But what about edge cases, like new interval overlapping 1, 
        overlapping 6, or just in between
        
        - Okay, suppose we somehow have an interval like [2.25,2.75]
        - We start with res = 0
        - We see that [1,2] is smaller and separate from [2.25,2.75]
        -> 2<2.75
        -> start > 2
        - res = [[1,2]]
        - Now [2.25,2.75] is next, but hold on!
        - We must check the interval that ORIGINALLY succeeded [1,2]
        - Does [2.25,2.75] overlap with [1,2]? No
        - res = [[1,2],[2.25,2.75]
        - res = [[1,2],[2,25,2.75],[3,4]]
        - res = [[1,2],[2,25,2.75],[3,4],[5,6]]

        - What about newInterval = [0,3]
        - We see that newInterval [0,3] OVERLAPS with 
        curInterval [1,2]
        -> start, end = newInterval[0], newInterval[1]
        -> start<=curInterval[1] AND end>=curInterval[0] 
        - We must merge them
        - mergedInterval = 
        [min(start,curInterval[0]), max(end,curInterval[1])]
        = [0,3]
        - Set curInterval = [3,4]
        - We don't add mergedInterval just yet, now we see 
        if it OVERLAPS with this new curInterval
        - start<=curInterval[1] AND end>=curInterval[0]
        -> 0<=4 AND 3>=3
        - It does overlap!
        - mergedInterval = 
        [min(start,curInterval[0]), max(end,curInterval[1])]
        = [0,4]
        - Set curInterval = [5,6]
        - We don't add mergedInterval just yet, now we see 
        if it OVERLAPS with this new curInterval
        - end >/= curInterval[0]
        -> 4>/=5
        - Nope!
        - NOW we add mergedInterval
        - res = [[0,4]]
        - And we add curInterval
        - res = [[0,4],[5,6]] 

        - O(n) time <- to iterate over intervals
        - O(n) space <- to store the intervals with insertion
        '''
        
        res = []

        for i in range(len(intervals)):
            # Loop over intervals
            if newInterval[1] < intervals[i][0]:
                # newInterval ends BEFORE this interval
                # If this is the case then we can finally add 
                # newInterval
                res.append(newInterval)
                # Append the rest of the intervals from i
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                # newInterval strictly comes AFTER the 
                # interval at this index, just add whatever 
                # interval is at i
                res.append(intervals[i])
            else:
                # Okay, two things are true
                # 1. newInterval does NOT end AFTER this interval
                # 2. newInterval does NOT start BEFORE this interval
                # We must merge the intervals and update newInterval 
                # accordingly
                newInterval = [min(newInterval[0],intervals[i][0]), 
                               max(newInterval[1],intervals[i][1])]
        
        # There are two ways that we exited
        # 1. The newInterval is NEVER smaller than 
        # the final interval, so the first IF 
        # statement did not execute
        # 2. The newInterval was smaller than the 
        # final interval, so the first IF statement 
        # did execute
        # In the second way, we would return!
        # So we safely append newInterval to res!
        res.append(newInterval)
        
        return res    

if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,3],[4,6]]
    newInterval = [2,5]
    print(sol.insert(intervals, newInterval)) # [[1,6]]
    intervals = [[1,2],[3,5],[9,10]]
    newInterval = [6,7]
    print(sol.insert(intervals, newInterval)) # [[1,2],[3,5],[6,7],[9,10]]