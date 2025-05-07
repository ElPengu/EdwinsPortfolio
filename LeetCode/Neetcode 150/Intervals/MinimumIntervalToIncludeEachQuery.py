from typing import List
import heapq
import math

class Solution:

    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        '''
        - intervals[i] = [left_i,right_i]
        - left_i<- start
        - right_i<- end (INCLUSIVE)
        - queries[j] = length of shortest interval 
        i such that...
        - left_i<=queries[j]<=right_i
        - If no such interval exists, the result of 
        the query is -1
        - Return an array output where...
        - output[j] is the result of queries[j]
        - NOTE: interval length = right_i-left_i+1

        - Okay, let's try understand the problem
        - We have a bunch of intervals
        - For each query, we want to find some 
        intervals where left_i<=queries[j]<=right_i
        - Finally, we want to take the SMALLEST 
        one of these intervals
        - And if we have an interval, give its 
        length as the answer, else set its length 
        to -1

        - We will do this in O(nlog n + q logq)
        - We will sort the intervals
        - We will sort the queries
        - We will use min heap minH for the 
        intervals

        - Let's imagine a number line
        - On the upper side are intervals 0,...,i
        - On the lower side are queries 0,...,j
        - For an interval to even be VALID for a 
        query, it must start before and end after 
        the query
        - So it might help to think of a query 
        happening at a TIME
        - So during an interval (think meeting) 
        we want to make a query at a time, we can 
        only go to the intervals that are occuring
        - This motivates sorting the queries and 
        intervals, so that when we see a query we 
        are close to intervals that occur at the 
        same time
        
        - Now there are quite a few subproblems
        - For a query we want to know the next 
        valid intervals in one block
        - Subproblem: Sorting the intervals
        - We do not want to jump across disparate 
        blocks of intervals each time we try to 
        solve a different query
        - Subproblem: Sorting the queries
        - Given a query we want to know whether 
        the next interval is to be considered as 
        a candidate
        - Subproblem: Determine whether the next 
        query is valid
        - Given a candidate interval that we 
        cannot consider, we want to know what to 
        do next
        - Subproblem: Ascertain what it means 
        when a candidate interval is invalid
        - Given a set of valid intervals, we want 
        to quickly know which one is the shortest 
        in length for our query
        - Subproblem: Knowing the shortest interval 
        for a query
        - Given a query we want to only consider 
        candidate intervals that are truly valid
        - Subproblem: Knowing the valid intervals 
        for a query based on the ones we have 
        previously seen
        - Whilst the queries are sorted, we want to 
        format outputs such that it is ordered as 
        our inputted queries list is
        - Subproblem: Returning outputs in the order 
        that the queries are in

        - Let's go step by step, shall we?

        - Subproblem: Sorting the intervals
        - We sort using the start time as the key

        - Subproblem: Sorting the queries
        - As queries are times, we sort the queries

        - Subproblem: Determine whether the next 
        query is valid
        - With our sorted intervals list, we 
        ask one question
        - left_i<=query
        - If this is so, we might be able to ask
        the query during that interval

        - Subproblem: Ascertain what it means 
        when a candidate interval is invalid
        - This means that from that interval and 
        onwards the query cannot be asked
        - Therefore we must consider only the 
        candidate intervals

        - Subproblem: Knowing the shortest interval 
        for a query
        - This also solves the issue of what to 
        do with candidate intervals
        - Whenever we come across a candidate 
        interval, we push it onto a minimum heap
        minH
        - We want the shortest interval so we 
        use its length as the sorting key 
        - To help with the subproblem of determining 
        whether a candidate interval is valid or not 
        we must also include when it ends
        - We needn't order by right_i too, but it 
        does not change much. It's inclusion is 
        explained in the following subproblem
        - PUSH (right_i-left_i+1, right_i) ON minH

        - Subproblem: Knowing the valid intervals 
        for a query based on the ones we have 
        previously seen
        - At this point, we have no more intervals 
        that can be candidates
        - We look to our minH
        - We have added all intervals that start 
        before us, which is good
        - But a candidate intervals is only valid 
        if it ends at of after us
        - So we TOP minH
        - If right_i>=query then that shortest 
        interval is valid for us!
        - What if it is not?
        - Let's think about it, all queries after 
        this query occur at or after it
        - The query is too late for this candidate 
        interval
        - Therefore we needn't consider it ever 
        again
        - POP minH
        - Once we TOP minH and see a valid 
        candidate interval you LEAVE IT and you 
        MAP query->length

        - Subproblem: Returning outputs in the order 
        that the queries are in
        - This motivates using a hash map
        - Simply put, we will create hash map 
        query->length, as alluded to in the previous 
        subproblem
        - When generating outputs we will create 
        a blank outputs list
        - We will loop over queries and will append 
        hashMap[query] (i.e., length)

        - This is NOT an easy problem
        - There are so many things to keep up with
        - I.e., many subproblems, even though the 
        code is short
        - Comments from Neetcode

        - Hard problem in 27 minutes? Ujiangalia, 
        Gaitho! Ura!
        '''
        
        # We will sort our intervals
        intervals.sort()
        
        # We will maintain a minimum heap
        minHeap = []
        
        # res <- query->length
        # i <- interval we are at
        res, i = {}, 0

        for q in sorted(queries):
            # Don't worry, this loops through a 
            # COPY of queries in sorted order!

            while (i < len(intervals) and 
                   intervals[i][0] <= q):
                # We keep on looping until the 
                # candidate intervals that do NOT 
                # start after q are added to our 
                # heap

                # Get left and right
                l, r = intervals[i] 

                # Push length and right for this 
                # candidate interval
                heapq.heappush(minHeap, (r-l+1, r))
                # Go to next interval
                i+=1
            
            # Now we have all candidate intervals
            # If there are any
            
            while minHeap and minHeap[0][1] < q:
                # Ensure that there is a candidate 
                # interval
                # Ensure that the candidate interval
                # ends BEFORE the query q can take 
                # place
                # Remove such invalid candidate 
                # intervals
                heapq.heappop(minHeap)

            # Now all that are left are valid 
            # intervals IF THERE ARE ANY
            # If minHeap is not empty we add the 
            # length at its top
            # Else there are no valid intervals for 
            # query q, so we add length of -1
            # But where do we add the length?
            # We map q->length in res
            res[q] = minHeap[0][0] if minHeap else -1
        # Now the dictionary is populated

        # Now how do we return a list of the 
        # lengths in the same order as queries
        # In python we can use some list 
        # comprehension!
        # We loop over queries, and for each q
        # we append res[q] to the list
        return [res[q] for q in queries]

if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,3],[2,3],[3,7],[6,6]]
    queries = [2,3,1,7,6,8]
    print(sol.minInterval(intervals, queries)) # [2,2,3,5,1,-1]