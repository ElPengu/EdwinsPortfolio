from typing import List
from collections import defaultdict

class CountSquares:
    '''
    - You are given a stream of points of x-y 
    coordinates on a 2D plane
    - Add - new points are added to the data 
    structure. Duplicate points are allowed and 
    should be treated as separate
    - Query - Given a single query point, count 
    the number of ways to choose three additional 
    points such that they and the query point form 
    a square. The square must have all sides 
    parallel to the x-axis and y-axis 
    -> Recall that a square must have four equal 
    sides 

    - Problems
    - Determining how many squares you can create 
    given duplicate points
    - Storing the points given we must store 
    duplicates
    - Detecting a square
    - Determining what a diagonal is


    - Determining how many squares you can create 
    given duplicate points
    - If you have x duplicate points, then you can 
    use each x point for a different square
    - Hence, x different squares
    - If you have x duplicate points, and y 
    different duplicate points, then you can use 
    each x point for a different square, and for 
    each of those squares you can use each y point 
    for a different square
    - Hence, x * y different squares 

    - Storing the points given we must store 
    duplicates
    - Naturally this lends itself to a hash map
    - Key: Set of coordinates of a point
    - Value: A count for the number of such points 

    - Detecting a square
    - We use some geometry
    - We check every point for whether it is a 
    DIAGONAL point
    - We verify whether these two points can form 
    a square
    - Let query point = (Px,Py), diagonal point = 
    (x,y)
    - We see if one point exists with the x-coord 
    of 1 and y-coord of the other
    - (x,Py), (Px,y)

    - Detecting a rectangle
    - A fun little trick, but detect a square 
    except you don't care whether the two points 
    form a DIAGONAL 

    - Determining what a diagonal is
    - A diagonal is formed by points p0 and p1
    - You can start at p0, walk in the x direction 
    for X steps, and then walk in the y direction 
    for X steps
    - After this you reach point p1
    - Given p0 = (x_p0, y_p0), p1=(x_p1,y_p1)
    - abs(x_p1-x_p0) == abs(y_p1-y_p0)
    '''
    
    def __init__(self):
        # Dictionary defaulting to count 0
        self.ptsCount = defaultdict(int)

    def add(self, point: List[int])->None:
        # We increase the count of this point 
        # by 1

        # Remember to transform the list to a tuple 
        # so that it can be a key!
        self.ptsCount[tuple(point)] += 1

        return None 

    def count(self, point: List[int])->int:
        # Set count
        res = 0

        # Extract x and y coordinates of point
        px, py = point
        for x, y in self.ptsCount:
            # Go through all possible diagonal 
            # values

            # Verify if it is a diagonal point
            if (abs(py-y) != abs(px-x) or 
                x == px or y == py):
                # We don't consider non-diagonals
                # We do not consider points that 
                # stack on top of each other
                continue
            if ((x,py) in self.ptsCount and (px,y) in self.ptsCount):
                # If statement so that we don't 
                # accidentally increase the size of 
                # ptsCount
                
                # Multiply the counts to see the number 
                # of squares
                res += self.ptsCount[(x,py)] * self.ptsCount[(px,y)]
        
        return res

if __name__ == "__main__":
    countSquares = CountSquares();
    countSquares.add([1, 1]);
    countSquares.add([2, 2]);
    countSquares.add([1, 2]);

    print(countSquares.count([2, 1])) # return 1.
    print(countSquares.count([3, 3])) # return 0.
    countSquares.add([2, 2]) #  Duplicate points are allowed.
    print(countSquares.count([2, 1])) # return 2. 