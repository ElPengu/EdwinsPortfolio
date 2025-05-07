from typing import List
import heapq

class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        - intervals[i] = [start_i, end_i]
        - Return an array of all non-overlapping intervals covering 
        all the intervals in the input
        - You may return answer in any order
        
        - Let's break this into subproblems that make sense
        - We need to know WHICH intervals "overlap"
        - We can break this down into two subproblems as 
        shown below

        - Subproblem 1: Finding the ordering of the intervals
        - This can be done by heapifying the intervals by start_i
        - heapq.heapify(intervals)

        - Subproblem 2: Which intervals overlap
        - When we pop from the heap, start_0 will be the start of the 
        interval of the first merged interval
        - What about the end?
        - The end will be end_i, where the start is AT MOST equal to 
        the current end

        - Now this problem seems more simple!
        - First, we need res = []
        - Next, we need to heapify the intervals list
        -> O(n) time
        - Now we start popping. We set start, and then as we pop we 
        update end with the maximum end that we have seen
        - Once we see a start that comes after this maximum end, we 
        add an interval with start and maximum end, and reset start 
        to this later start!
        - Naturally, if the heap is empty you must add the final 
        start and end that we have   


        - Wow, that was so sophisticated! My brain just did that in 
        19 minutes with a heap (including fail checks!)
        - This solution is as efficient as Neet's, in lines and 
        complexity, and is the same logic
        - For this reason, for the first time, I will endorse 
        THIS version of the solution to be studied!
        '''

        # Set up res
        res = []

        # Heapify the intervals list
        heapq.heapify(intervals)

        # Set start and end
        start, end = intervals[0][0], intervals[0][1]

        # Length of intervals
        N = len(intervals)

        while intervals:
            interval = heapq.heappop(intervals)
            if interval[0] > end:
                # We have an interval to be merged in the new group!

                # We must add the old merged interval
                newInterval = [start,end]
                res.append(newInterval)

                # Now we update start
                start = interval[0]
            
            # We must merge this interval

            # Maximise end
            end = max(end, interval[1])
        
        newInterval = [start,end]
        res.append(newInterval)
        return res


if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,3],[1,5],[6,7]]
    print(sol.merge(intervals)) #[[1,5],[6,7]]
    intervals = [[1,2],[2,3]]
    print(sol.merge(intervals)) #[[1,3]]
    intervals = [[1,3],[4,5],[5,7]]
    print(sol.merge(intervals)) # [[1,3],[4,7]]
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(sol.merge(intervals)) # [[1,6],[8,10],[15,18]]
    intervals = [[1,4],[4,5]]
    print(sol.merge(intervals)) # [[1,5]]