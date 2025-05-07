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

        - Oh my word, this is so smart...
        - What does it mean to need a day?
        - When they overlap
        - What is the minimum number of days?
        - The maximum number of overlapping meetings 
        at any given time  

        - We will maintain count
        - count <- number of meetings that are 
        occuring at this moment
        - When we see a meeting is at its start, we 
        will increment count
        - When we see a meeting is at its end, we 
        will decrement count
        - We just maintain when count is at its 
        maximum

        - What about (0,8) and (8,10)?
        - We will always first consider end, then 
        start
        - A meeting must end before the next one 
        starts, intuitively makes sense, no?

        - We will maintain two lists
        - start <- list of start times IN ORDER
        - end <- list of end times IN ORDER

        - How we will work through the lists
        - We will maintain pointers startP and endP
        - Consider the example below
        - start = [>0<,5,10]
        - end = [>10<,15,30]
        - Since 0<10, we have one meeting when we 
        are at t=0. 
        - We increment count and shift 
        startP
        - count=1
        - start = [0,>5<,10]
        - end = [>10<,15,30]
        - Since 5<10, we have another meeting 
        starting at t=5, but we are still waiting 
        for the meeting ending at 10 to end
        - We increment count and shift startP
        - count=2
        - start = [0,5,>10<]
        - end = [>10<,15,30]
        - Since 10 !< 10 (a tie), a meeting ENDS at 
        10
        - Decrement count and shift endP
        - count=1
        - start = [0,5,>10<]
        - end = [10,>15<,30]
        - Okay, now 10<15, so the meeting at 10 
        starts but we are still waiting for the 
        meeting at 15 to end
        - Increment count and shift startP
        - count=2
        - start = [0,5,10]><
        - end = [10,>15<,30]
        - I won't write the rest, but we finish 
        with count=0

        - What was the general question?
        - We are about to start this next meeting, 
        at this time is the meeting that is due to 
        end to do so later? If so, we need another 
        day! <- CRITICAL QUESTION 

        - O(n log n) <- sort
        - O(n) space <- To store the sorted list 
        '''

        # Create an array for all start and end 
        # times
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        # Set res for max count, and count
        res, count = 0, 0

        # Pointer for start, pointer for end
        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                # We have a meeting starting but 
                # we are still waiting for a 
                # meeting to end

                # Move to the next meeting to start
                s+=1
                # Increment count
                count+=1
            else: 
                # We have a meeting ending at or 
                # before the next meeting is due to 
                
                # Move to the next meeting to end
                e+=1
                # Decrement count
                count-=1
            # Update res
            res = max(res,count)
        return res

if __name__ == "__main__":
    sol = Solution()
    intervals = [(0,40),(5,10),(15,20)]
    print(sol.minMeetingRooms(intervals)) # 2
    intervals = [(4,9)]
    print(sol.minMeetingRooms(intervals)) # 1