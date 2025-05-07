from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # prerequisite[i] = [a,b] -> course B must be taken before 
        # course a
        # You must take courses 0,...,numCourses-1
        # We want any valid ordering of courses you can take to complete
        # the courses
        # If there is none, return an empty array
        # 
        # How to do this...
        # Again, we want to see if we can point from every course to 
        # some CORE course (no prerequisites)
        # As before we can maintain an adjacency list
        # On an intuitive level we want to take a course and see 
        # the order in which you must complete courses
        # This implies that for a course you want to do BFS, 
        # because you want to know every prerequisite that you need 
        # for your course first, THEN every prerequisite at the 
        # second level, and so forth
        # Question: What if we start evaluating a course that itself
        # is a prerequisite?
        # Just went to the washroom and realised a way when returning!
        # What you are really asking is: how could we connect one 
        # list of prerequisites for course i and another for course 
        # j, assuming that course i is a prerequisite of course j and 
        # that we create the list for course i first?
        # Okay, let's say that we have created the list for course i
        # We want to evaluate course j until we reach the LEVEL at 
        # which course i appears
        # So we will need to record whenever we reach the start of 
        # a new list
        # Then we want to CONNECT the lists
        # What do we do?
        # We could do this...
        # Maintain a mapping [start course, order list]
        # Whenever you reach a level where you find a start course, 
        # connect the lists, ADD a key for this NEW start course 
        # and then delete the old start course!
        # I.e.
        # Stage 1: [start course: order list]
        # Stage 2: [start course: order list, new start course: 
        # new connected order list]
        # Stage 3: [new start course: new connected order list]
        # Return values of keys
        # Too much to code at the level I am at NOW, but I am proud
        # that I have progressed to think this deeply about these 
        # problems. Just need to keep pushing and learning!!

        pass


if __name__ == "__main__":
    sol = Solution()
    numCourses = 3
    prerequisites = [[1,0]]
    print(sol.findOrder(numCourses, prerequisites))
    numCourses = 3
    prerequisites = [[0,1],[1,2],[2,0]]
    print(sol.findOrder(numCourses, prerequisites))