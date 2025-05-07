from typing import List
import heapq
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:

    def canAttendMeetings(self, intervals: List) -> bool:

        '''
        - We have meeting time intervals
        - start_i<end_i
        - Determine if a person could add all their 
        meetings to their schedule without conflict 

        - NOTE: (0,8) and (8,10) DO NOT OVERLAP

        - Break this down into subproblems
        - 1. We need to have some order by time
        - 2. We need to determine what it means for 
        two intervals to conflict

        - SUBPROBLEM 1: Ordering the intervals
        - heapq.heapify(intervals)
        - Now we just pop
        - O(nlogn) time for the intervals

        - Subproblem 2: Determining conflict
        - We maintain a start and an end
        - If start_i<end: return False
        - end = end_i
        - Note that, given no conflict 
        end_i<end_i+1 

        - 10 minutes, hehe
        - My solution is so good that, again we will 
        study it!
        '''

        # Store intervals in a heap
        heapq.heapify(intervals)

        # Pop first interval to set start and end
        interval = heapq.heappop(intervals)
        start, end = interval[0], interval[1]

        while intervals:
            # Pop an interval
            interval = heapq.heappop(intervals)
            # Store start and end for this interval
            start_i, end_i = interval[0], interval[1]

            if start_i < end:
                # These intervals overlap!
                return False
            # These intervals do not overlap
            # Maximise end
            # Necessary? 
            end = end_i

        # No overlaps!
        return True

if __name__ == "__main__":
    sol = Solution()
    intervals = [(0,30),(5,10),(15,20)]
    print(sol.canAttendMeetings(intervals)) # false
    intervals = [(5,8),(9,15)]
    print(sol.canAttendMeetings(intervals)) # true