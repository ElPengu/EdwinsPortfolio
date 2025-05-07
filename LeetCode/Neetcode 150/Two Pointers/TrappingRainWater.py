from typing import List

class Solution:

    def trap(self, height: List[int]) -> int:
        # Conceptually a non-end point bar j
        # can hold at least 0 water
        # If there are two bars i,k on either 
        # side which are the tallest 
        # on either side, then bar j 
        # can hold the difference between 
        # it and the minimum of bars i,k
        # 
        # The solution requires two pointers 
        # on either end. Label these pointers 
        # i and k
        # We find out the smaller bar (for ease 
        # we'll call it bar j'), and place 
        # bar j one bar towards the centre of 
        # this bar
        # Now this is kind of non-intuitive 
        # at the moment, but bar j can hold the 
        # difference between it and bar j' (or zero 
        # if this is negative) because somewhere on 
        # the other side of bar j there is a bar 
        # taller than bar j' which means that the 
        # water will not spill over
        # 
        # It helps to imagine heights [15,3,1,100]
        # with indices 0,1,2,3
        # height[3] is so tall that height[1] has 
        # height[0] as its bottleneck, even though 
        # the third bar is so short!
        
        # 1. Trivial case
        if not height:
            return 0

        # 2. We set two pointers for left and right
        # at both ends of the array
        l, r = 0, len(height) - 1

        # 3. We set leftMax and rightMax to hold the 
        # maximum left and right height so far
        leftMax, rightMax = height[l], height[r]

        # 4. We set res to 0
        res = 0

        # 5. We iterate until l meets r
        while l < r:

            # We shift the pointer with the
            # minimal height
            if leftMax < rightMax:
                # Now l refers to the bar 
                # exactly one step to the right
                l += 1

                # Since we know that the 
                # minimum height to the 
                # left (now) is the bottleneck, 
                # we use it to determine the height 
                # that this bar can hold
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                # Now l refers to the bar 
                # exactly one step to the right
                r -= 1
                
                # Since we know that the 
                # minimum height to the 
                # right (now) is the bottleneck, 
                # we use it to determine the height 
                # that this bar can hold
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
            
            



if __name__ == "__main__":
    sol = Solution()

    height = [0,2,0,3,1,0,1,3,2,1]
    print(sol.trap(height)) # 9