from typing import List

class Solution:

    def maxArea(self, heights: List[int]) -> int:
        #Set left and right pointer
        #Area is dominated by the minimal height
        #pointed to by left and right
        #The only way to possible increase the height
        #is to shift the pointer to the minimal height
        #inwards, shifting the other does nothing

        maxArea = 0
        left, right = 0, len(heights)-1

        while left < right:
            area = min(heights[left], heights[right]) * (right-left)

            #Shift minimal height inwards
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

            maxArea = max(maxArea, area)
        
        
        return maxArea


if __name__ == "__main__":
    sol = Solution()

    height = [1,7,2,5,4,7,3,6]
    print(sol.maxArea(height)) # 36
    height = [2,2,2]
    print(sol.maxArea(height)) # 4