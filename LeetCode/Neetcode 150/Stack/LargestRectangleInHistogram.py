from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Consider adding one height at a time
        # If you add a height of 4, then 6, then the bar of height 4 
        # can be "extended"
        # However, if you instead added a height of 3, then the bar of  
        # height 4 could not be "extended"
        # 
        # In the case that a bar can no longer have its height be 
        # "extended" makes it irrelevant from that point onwards
        # We just need to calculate the area of the rectangle that 
        # it could contribute to and then we remove it.
        # 
        # Note that we would continue to remove bars until we find 
        # one not of a taller height
        # 
        # This LIFO approach to pushing and popping items makes a stack 
        # useful!
        # 
        # Now the algorithm to do this!
        # We have a stack holding BOTH the start index and the 
        # corresponding height of **that** bar
        # We also hold the max area
        # When the next bar is taller, we simply add the bar and its height
        # We will talk about start index in a minute
        # However, when the next bar is shorter, we start popping from the 
        # stack! For each bar that is taller, you look at its start index 
        # You know that from that bar up to the current index onwards 
        # a triangle of its height could be extended, so you use this 
        # information to calculate its area and update the max area
        # 
        # Now, for the start index we do something smart. We do not 
        # just copy the start index of the bar. 
        # If you think about what we are doing by not adding a shorter 
        # to the stack, we are saying that from wherever the last 
        # **shorter** bar starts, we could extend a triangle of this
        # new bar's height up to wherever it actually is.
        # 
        # Therefore, we actually put the start index as the increment 
        # of the previous entry in the stack (or zero if the stack 
        # is empty)
        # 
        # Pretty neat, huh!
        # 
        # After creating the stack as described, we pop from the stack 
        # and update the max area as described

        # We must keep track of maxArea and a stack
        maxArea = 0
        stack = [] # pair (start index, height)

        # We add to the stack by enumerating heights
        # Basically we loop over heights but also access the index
        for i, h in enumerate(heights):
            # We set start to the real index of the bar
            start = i

            # When the stack is non-empty, we want to 
            # only add bars that are taller
            # So we must review and pop shorter bars
            # while they are in the stack!
            while stack and stack[-1][1] > h:
                #We pop the index and height
                index, height = stack.pop()

                # Calculate area from popped bar's index up to the 
                # index of the bar being added
                maxArea = max(maxArea, height * (i - index))
                # Update start index of the bar accordingly
                start = index
            #We append the start index and the height
            stack.append((start, h))
        
        # We now empty the stack and calculate the areas that their 
        # rectangles may create
        for i, h in stack:
            maxArea = max(maxArea, h*(len(heights)-i))

        return maxArea


        pass


if __name__ == "__main__":
    sol = Solution()
    heights = [7,1,7,2,2,4]
    print(sol.largestRectangleArea(heights)) # 8
    heights = [1,3,7]
    print(sol.largestRectangleArea(heights)) # 7