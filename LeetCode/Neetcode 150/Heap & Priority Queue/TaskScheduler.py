from typing import List
import heapq 
from collections import Counter, deque

class Solution:

    def taskScheduler(self, tasks: List[str], n: int)->int:
        # Example of how to prioritise tasks
        # A,A,A,B,B,C,C, n=1
        # 3A,2B,2C
        # We should consider the task with more occurences 
        # as a priority because it produces the most idle
        # time, so tasks that produce less idle time can
        # occur in between!
        # 
        # This means that we can abstract away the names of the 
        # tasks and just keep the occurences
        # 
        # We will use THREE structures to deal with this problem
        # MAXHEAP: This keeps track of the NEXT task that can
        # be processed at the time you pop it
        # QUEUE: This keeps track of the NEXT NON-IDLE task 
        # that can be added to the MaxHeap at a specific time
        # TIME: This keeps track of the time. Starts at 0. This
        # also abstracts away the need of explicitly adding dead
        # time tasks!
        # 
        # Now the interplay between these structures in complex!
        # 1. At the first instance all tasks COULD be immediately 
        # processed. So add all occurences to a MaxHeap
        # 2. At time t = 0 you select an occurence X
        # 3. Now we move on to time t = 1
        # 4. You can select the occurence X-1>0 times now. 
        # 5. The next time that you can select occurence X-1 is 
        # at time t = t+n. So in this example, you add 
        # [X-1,t+n] to a priority queue. Ordered by time
        # 6. You can select X-1>0 at time t+n+1
        # 7. Now you move up to the next time unit
        # Repeat until the queue AND the maxHeap is empty, 
        # only at this point are there no more tasks to consider
        # 
        # O(n) for selecting n tasks
        # 26 possible tasks, so O(26) for all other operations
        
        # each task 1 unit time
        # minimise idle time
        
        # Set a hash map using Counter
        count = Counter(tasks)
        # Create an array with negatives, 
        # then make a minheap so that it is a maxheap
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        # Set time
        time = 0
        # Set a double ended queue for count and idle time
        q = deque() # pairs of [-cnt, idleTime]

        while maxHeap or q:
            # This means that ALL tasks are checked

            # Increment time
            time += 1

            if maxHeap:
                # We pop from maxHeap if it is non-empty

                # Get the count and INCREMENT IT
                # count is negative, remember?
                cnt = 1+heapq.heappop(maxHeap)
                if cnt:
                    # There is still more of these tasks
                    # We append it with time to the queue
                    q.append([cnt, time+n])

            if q and q[0][1]==time:
                # In this case there is a task that is ready
                # to be processed again!
                heapq.heappush(maxHeap, q.popleft()[0])
                
        
        return time

        

        pass



if __name__ == "__main__":
    sol = Solution()

    tasks = ["X","X","Y","Y"]
    n=2
    print(sol.taskScheduler(tasks, n)) # 5

    tasks = ["A","A","A","B","C"]
    n = 3
    print(sol.taskScheduler(tasks, n)) # 9