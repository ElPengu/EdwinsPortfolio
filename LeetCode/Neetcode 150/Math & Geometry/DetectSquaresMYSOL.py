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
    - Storing the points
    - Being able to store duplicate points 
    separately
    - Finding out the number of squares that a 
    query point can be a part of

    - Storing the points
    - Use a hash map, where the point is the key

    - Being able to store duplicate points 
    separately
    - Within the hash map, the value should be 
    the number of points occupying that location

    - Finding out the number of squares that a 
    query point can be a part of
    - Given a query point, we know that another 
    possible point must have the same x- or y- 
    coordinate
    - We can loop through all the keys in O(N) 
    time
    - When you get a key with the same x- or y- 
    coordinate, you derive what the other key must 
    be
    - If the other key exists, you derive what the 
    final key must be
    - If all these other keys are used, store them 
    in a set visited so that you do not use them 
    again
    '''
    
    def __init__(self):
        # We need to store the points
        
        # Create a hash map
        # Defaults to zero
        self.coordMap = defaultdict(int)
        pass

    def add(self, point: List[int])->None:
        # We get point [x,y]

        # Convert it to a tuple
        point = tuple(point)
        
        # Store it in the coordMap
        self.coordMap[point] += 1

        return None 

    def count(self, point: List[int])->int:
        # For consistency convert point to 
        # tuple
        point = tuple(point)
        # Store x and y coordinates of point
        x, y = point[0], point[1]
        
        # Create a set for visited points
        visited = set()

        # Keep count
        count = 0

        for key in self.coordMap:
            # If the key is visited, skip it
            if key in visited: continue

            # Store x and y coordinates of key
            keyX, keyY = key[0], key[1]

            # Since we loop over keys, we cannot 
            # land on the same point

            if x == keyX:
                # Find distance between 

                pass
            if y == keyY:


                pass
            # Add this visited key to visited
            visited.add(key)


if __name__ == "__main__":
    countSquares = CountSquares();
    countSquares.add([1, 1]);
    countSquares.add([2, 2]);
    countSquares.add([1, 2]);

    countSquares.count([2, 1]) # return 1.
    countSquares.count([3, 3]) # return 0.
    countSquares.add([2, 2]) #  Duplicate points are allowed.
    countSquares.count([2, 1]) # return 2. 