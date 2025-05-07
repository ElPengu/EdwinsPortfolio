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

        - Let's break this up into subproblems

        - How do we determine if some intervals 
        overlap?
        - We could heapify the intervals by start_i 
        - Now we inspect elements until we have a 
        group of overlapping intervals
        - Subproblem: identify overlapping intervals

        - Now we have a group of overlapping 
        intervals, how do we determine which ones to 
        remove?
        - Would it not just be the longest one? 
        - That seems too simple, but let's think
        - Okay, no it isn't that
        - Consider [[1,10],[9,11],[11,20]]
        - You want to remove [9,11], which is not the 
        longest
        - But WHY do you want to remove [9,11], what 
        makes it special?
        - It is the fact that it overlaps with 2 
        intervals, but the others overlap with 1
        - How can we generalise this?
        - Could you greedily look for the next 
        interval
        - Like, you keep [1,10], then go [11,20]
        - Not really, consider...
        - [[1,12],[2,3],[4,5],[6,7],[8,9],[10,11]]
        
        - Maybe we could group all non-overlapping 
        intervals here
        - So from [[1,10],[9,11],[11,20]] we get 
        [[1,10],[11,20]] and [[9,11]]
        - Now we know that we should remove [[9,11]]
        - I feel like you could get more than two 
        non-overlapping groups though
        - Consider [[1,4],[2,5],[3,6]]
        - You get [[1,4]], [[2,5]], [[3,6]], three 
        separate groups
        - Wait, hold on, we don't want to know 
        what the group is, do we?
        - No, we specifically want to know the... 
        the what?
        - We want something about the start and end
        
        - This is harder than I thought...
        '''

        pass

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