from typing import List

class Solution:

    def carFleet(self, target: int, position: List, speed: List) -> int:
        # For where Neetcode is coming from
        # This is a weird turn, but it helps to consider the position 
        # and speed of the cars as a system of linear equations
        # 
        # Imagine a position and time graph. So the speed of a car is 
        # the slope, and position determines where the car is at time 0
        # 
        # Naturally, where the line of the i and i+1 cars intersect it 
        # where it becomes a fleet
        # 
        # The solution itself
        # Now we order the list of position,speed pairs into ascending 
        # order by position
        # We can see that if a car at position 7 arrives at the end
        # after a card at position 10, then they become a fleet
        # If this happens, which car should we consider if we add 
        # a car at position 3 next? We must compare to the one at 
        # position 7 because it is the bottleneck for *this* fleet
        # Hence, when a fleet occurs, we delete the information 
        # of the car *joining* the stack
        # The length of the stack will give us the number of fleets!

        # Create an array of pairs
        pair = [[p,s] for p, s in zip(position, speed)] # list comprehension

        # Create a stack
        stack = []

        # We sort the pairs, and then iterate through it in reverse order
        for p, s in sorted(pair)[::-1]:
            # We want to know the *time* the car reaches the position
            # We can use decimal form because it is pairs
            stack.append((target - p) / s)
            # Now we see if the just added car overlaps with the preceding
            # car
            # Also, we 
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                #We must pop from the stack
                stack.pop()

        # Now we just return the length of the stack
        return len(stack)

        pass


if __name__  == "__main__":
    sol = Solution()
    target = 10
    position = [1,4]
    speed = [3,2]
    print(sol.carFleet(target, position, speed)) # 1
    target = 10
    position = [4,1,0,7]
    speed = [2,2,1,1]
    print(sol.carFleet(target, position, speed)) # 3
