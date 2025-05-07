from typing import List

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List) -> int:

        '''
        - start_i < end_i
        - Find the minimum number of days to 
        schedule all meetings without any conflicts
        - Note: (0,8),(8,10) is not considered a 
        conflict at 8

        - Let's break this down into subproblems
        - It would be useful to have the intervals 
        in a sort of order
        - Subproblem: sort the intervals
        - It would be useful if we knew when 
        meetings had a conflict
        - Subproblem: determine which meetings 
        conflict
        - It would be useful to know which "day" a 
        meeting should go in
        - Subproblem: which day a meeting should go 
        in

        - Subproblem 1: Sort the intervals
        - heapq.heapify(intervals)

        - Subproblem 2: Determine which meetings 
        conflict
        - Given interval_i and interval_i+1
        - start_i+1 > end_i <- conflict

        - Subproblem 3: Determine which day a 
        meeting should go in 
        - First of all, we should represent a day
        - Subproblem 3a: Represent a day
        - A day has a start and end. We can default 
        start=end=0 for a day
        - Next we should be able to store days
        - Subproblem 3b: Since two days could have 
        the same start, we should store a list of 
        days
        - Now how do we determine the day to put 
        a meeting in?
        - We must evaluate intervals until they 
        overlap
        - When this occurs, take the one that 
        ends LATER and add it to the previous 
        day
        - Now carry on

        - Do we even need days?
        - Could we not use a count variable?
        - Using sub problems 1 and 2 we can 
        greedily determine conflicting meetings
        - When two meetings conflict, we need a 
        separate day between them
        - To reduce the chance of conflict, the 
        meeting that ends EARLIER should stay in 
        the same day
        - The LATER meeting should go in a 
        different day
        - So really we only need a list of days 
        represented by when the day ENDS
        - If the conflicting meeting starts AFTER 
        some day, it can occur at that time

        - Summary
        - 1. Order the meetings
        - 2. Keep a list of end times for days
        - 3. Update end time for they day until you 
        see a conflict
        - 4. Update end time for the earlier ending 
        conflicting meeting
        - 5. Add a new day for the later ending 
        conflicting meeting 
        
        - Final question: How do we know what day 
        to add a conflicting meeting to?
        - We could traverse the list and update the 
        day with the latest end time?


        '''

        pass

if __name__ == "__main__":
    sol = Solution()
    intervals = [(0,40),(5,10),(15,20)]
    print(sol.minMeetingRooms(intervals)) # 2
    intervals = [(4,9)]
    print(sol.minMeetingRooms(intervals)) # 1