from typing import List

class Node:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = [] if None else children

class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # We have numCourses of courses to take, from 0 to numCourses-1
        # Some courses have prerequisites
        # -> prerequisite[0][1] -> you must take course 1 before course 0
        # Let's think, what does it mean for a course to NOT be possible
        # to solve?  
        # Well, if for course i0, you need to take course i1, which needs
        # course i2, ..., which needs course iN-1, which needs i0! 
        # This lends itself to GRAPHS
        # We will say that prerequisite[i][j] means we have edge j->i
        # So for each course in numCourses just do DFS or BFS and 
        # detect a cycle. We will use DFS
        # One more thing, do we need a graph? Neetcode says no!
        # We'll use an adjacency list preMap represented with a hash map
        # preMap = [course, prerequisite list]
        # We do DFS on preMap
        # Why an adjacency list?
        # > I remember, it saves space!
        # 
        # To do DFS on the adjacency list we search every course in 
        # numCourses
        # Maintain VISITED
        # Now for DFS
        # > Base cases: in VISITED -> False, if preMap[course] = [] 
        # then True (it can be completed)
        # > We are VISITING this course, add to VISITED
        # > For every child run DFS and if False then return False
        # > We have finished VISITING this course, add to VISITED
        # > This course can be completed so set preMap[course] = 
        # [] (indicates it can be completed for base case)
        # > This course can be completed so we return True
        # 
        # Since the graph may be DISCONNECTED, we run DFS 
        # on every course
        # 
        # O(n+p), n for courses, p for prerequisites
        # -> We visit every course and prerequisite at most once


        # Create our prerequisite map, map course to empty list
        # Remember that prerequisite map is an adjacency list
        preMap = {i:[] for i in range(numCourses)}

        # Append prerequisites to courses in adjacency list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Create a visit set
        visitSet = set()
        # Create a dfs
        def dfs(crs):

            # Look at our base cases

            if crs in visitSet:
                # We have a loop!
                return False
            if preMap[crs] == []:
                # We need no prerequisites
                return True
            
            # We are visiting this course now
            visitSet.add(crs)
            for pre in preMap[crs]:
                # For each prerequisit
                if not dfs(pre):
                    # We have a loop, immediately return False
                    return False
            
            # We have finished visiting this course
            visitSet.remove(crs)

            # This course can be completed, so change this to an 
            # empty list
            preMap[crs] = []

            # We can complete this course
            return True
        
        for crs in range(numCourses):
            # We must check every course since the graph might NOT be 
            # connected
            if not dfs(crs):
                # At least one course is impossible
                return False
            
        # Every course is complete-able!
        return True


        pass

if __name__ == "__main__":
    sol = Solution()
    numCourses = 2
    prerequisites = [[0,1]]
    print(sol.canFinish(numCourses, prerequisites)) # True
    numCourses = 2
    prerequisites = [[0,1],[1,0]]
    print(sol.canFinish(numCourses, prerequisites)) # False

