from typing import List

class Node:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = [] if None else children

class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Prerequisite[i] = [a,b] -> you must take b before a
        # Find out if you can complete all the courses
        # 1 <= numCourses <= 1000
        # What is this problem asking?
        # From the course with no prerequisites, can you 
        # keep on choosing courses until you have selected all 
        # in prerequisites
        # 
        # A graph would be a good way of representing prerequisites
        # Every node in the graph has value course, and children 
        # prerequisite courses
        # Intuitively, we want to loop over numCourses
        # For each associated node (stored in a hash map) we search 
        # (using BFS or DFS) and if we see the same node again then
        # we have a cycle which means we cannot complete this course
        # If we 'verify' each node then we return true

        # 1. Create an empty mapping course -> node
        courseNodeMap = {}

        # 2. Create a node for each course and add it to the mapping
        for course in numCourses:
            courseNodeMap[course] = Node(course)

        # 3. For each node add a list of its prerequisites as children
        for prerequisite in prerequisites:
            # Find the node for the prerequisite
            child = courseNodeMap[prerequisite[1]]

            # Find the parent of the child
            parent = courseNodeMap[prerequisite[0]]

            # Add the child to the parent list of children
            parent.append(child)


        # 4. Loop over every course and find its node

            # Create a set of VISITED nodes

            # Do recursive DFS, in that function if you find a node in 
            # VISITED then return False

            # If recursive DFS returns FALSE then we return FALSE

        # 5. We have reached this point so no node has prerequisited 
        # that cannot be completed

        # Return True

        pass

if __name__ == "__main__":
    sol = Solution()
    numCourses = 2
    prerequisites = [[0,1]]
    print(sol.canFinish(numCourses, prerequisites)) # True
    numCourses = 2
    prerequisites = [[0,1],[1,0]]
    print(sol.canFinish(numCourses, prerequisites)) # False

