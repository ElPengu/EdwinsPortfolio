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
        # Since we want to know of any course the nature of other courses
        # this is a natural GRAPH problem
        # 
        # We will use something called TOPOLOGICAL SORT
        # > Don't worry, this problem TEACHES you what TOPOLOGICAL SORT
        # is
        # 
        # We begin by building an adjacency list to store nodes and 
        # neighbours
        # We create an output list
        # -> prereq = [course: prerequisite list] 
        # We will start at every node in prereq and perform DFS
        # At node i we do DFS until we find node iN-1 which has no 
        # prerequisites and "cross it out" and APPEND it to our output 
        # list. We bubble back up s.t. nodes iN-1,...,i are "crossed
        # out" and APPENDED to output IN THAT ORDER
        # Now let's say we have nodes j and k that POINT directly to i
        # This means we need course i to take courses j and k
        # So we APPEND course j and k to output
        # 
        # What if there is a cycle?
        # We will maintain a hash set of VISITING nodes. If we land 
        # on a node that we are already VISITING in the search tree
        # then we have a cycle! So return []
        # 
        # So there are three states
        # > Visited: A course that has been added to output. No need 
        # to add it twice
        # > Visiting: A course that we have not added to output BUT 
        # we have seen in the CURRENT search tree. Used for cycle 
        # detection
        # > Unvisited: A course that has not been added to output 
        # nor seen in the CURRENT search tree
        # 
        # We visit every node and edge at most two times
        # > O(E+V) time, E = prerequisites, V = courses 


        # We build an adjacency list of prerequisites
        prereq = { c:[] for c in range(numCourses)}

        for crs, pre in prerequisites:
            # Append each prerequisit of a course to its list in
            # the adjacency list
            prereq[crs].append(pre)

        # An output list
        output = []
        # A set of courses that we have VISITED and added to the output
        # lis
        visit = set()
        # A set of courses that we are VISITING in the CURRENT search 
        # tree
        cycle = set()

        # Definition of depth first search
        def dfs(crs):
            # Base cases first!
            if crs in cycle:
                # We have a cycle! 
                return False
            if crs in visit:
                # We don't need to visit it twice
                return True
            
            # We are VISITING this course
            cycle.add(crs)

            # Go through EVERY prerequisite
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    # We have a cycle!
                    return False
            
            # We are NO LONGER VISITING this course
            cycle.remove(crs)

            # We have VISITED this course, add it to visit AND our 
            # output as we have added all of its prerequisites 
            # already!
            visit.add(crs)
            output.append(crs)
            return True
        
        # We must go through every course
        for c in range(numCourses):
            # run through DFS on every course and see if we have a cycle
            if dfs(c) == False:
                # We have a cycle!
                return []
            
        # All courses can be completed! Return output
        return output


if __name__ == "__main__":
    sol = Solution()
    numCourses = 3
    prerequisites = [[1,0]]
    print(sol.findOrder(numCourses, prerequisites)) # [0,1,2]
    numCourses = 3
    prerequisites = [[0,1],[1,2],[2,0]]
    print(sol.findOrder(numCourses, prerequisites)) # []
