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

        - Let's break this down into subproblems
        - Subproblem: Store the outputs
        - Subproblem: Order the intervals by start
        - Subproblem: Iterate through the queries 
        one at a time
        - Subproblem: Determine which intervals are 
        possible for a query
        - Subproblem: Set the output for an 
        interval as the minimum length if possible, 
        else -1
        - Subproblem: Store the output in outputs
        - Subproblem: return the outputs 

        - Subproblem: Store the outputs
        - Trivial

        - Subproblem: Order the intervals by start
        - Heapify

        - Subproblem: Iterate through the queries 
        one at a time
        - Trivial, loop over queries

        - Subproblem: Determine which intervals are 
        possible for a query
        - Make a copy of the heap
        - Pop interval from the heap
        - Possible if 
        interval[0]<=queries[j]<=interval[1]

        - Subproblem: Set the output for an 
        interval as the minimum length if possible, 
        else -1
        - Initialise length = -1
        - Maintain left and right initialise to 0
        - For each possible queries, if 
        right-left+1 < right_i-left_i+1: 
        right = right_i, left=left_i, update length

        - Subproblem: Store the output in outputs
        - Trivial

        - Subproblem: return the outputs 
        - Trivial

        - Hard problem in 27 minutes? Ujiangalia, 
        Gaitho! Ura!
        '''
        
        # Subproblem: Store the outputs
        outputs = []

        # Subproblem: Order the intervals by start
        heapq.heapify(intervals)
        
        # Subproblem: Iterate through the queries one at a time
        for query in queries:
            # Make a copy of the heap
            intervalsCopy = intervals.copy()

            # Initialise output, left, and right
            # For initial maximum length, set right to infinity
            output, left, right = -1,0,math.inf


            # Subproblem: Determine which intervals are possible for a query
            while intervalsCopy:
                # Pop an interval
                interval = heapq.heappop(intervalsCopy)

                if interval[0]<=query<=interval[1]:   
                    # Subproblem: Set the output 
                    # for an interval as the 
                    # minimum length if possible, 
                    # else -1
                    length = right-left+1
                    left_i,right_i = interval[0],interval[1]
                    length_i=right_i-left_i+1

                    if length_i<length:
                        
                        # Update output
                        output=length_i
                        
                        # Update left and right
                        left=left_i
                        right=right_i
            
                # Subproblem: Store the output in outputs
                if not intervalsCopy: outputs.append(output)

        # Subproblem: return the outputs 
        return outputs

if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,3],[2,3],[3,7],[6,6]]
    queries = [2,3,1,7,6,8]
    print(sol.minInterval(intervals, queries)) # [2,2,3,5,1,-1]