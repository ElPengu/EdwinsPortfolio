from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # BASE CASE: Start pointer = 0, end pointer = 0
        # Assume that end pointer is at maximum
        # Increment end pointer and update maximum 
        # until end pointer = k-1
        # maximum = max from 0 to k
        # 
        # ASSUMPTION:
        # Assume that currMax = max from i to j
        # 
        # 
        # INDUCTIVE STEP:
        # Start pointer is at i, end pointer is at j
        # CASE 1: j+1>=max
        # # nums[j+1] = max from i+1 to j+1
        # CASE 2: j+1 < max
        # # max lies between i+1 and j+1
        # # Increment start pointer, when it is at i+1, 
        # # set currMax to be nums[start pointer] 
        # # and repeatedly update it until start pointer 
        # # is at j+1
        
        #In case nums has length 1
        if len(nums) == 0:
            return [nums[0]]

        #1. Set up start and end pointers
        startPointer = 0
        endPointer = 0
        
        #2. Set a current maximum variable and maxList
        currMax = nums[0]
        maxList = []

        #3. Base case
        while endPointer+1 < k:
            currMax = max(currMax, nums[endPointer])
            endPointer += 1
        maxList.append(currMax)
        #4. Inductive step
        while endPointer+1 < len(nums):
            if nums[endPointer+1] >= currMax:
                currMax = nums[endPointer+1]
                endPointer+=1
            else:
                endPointer+=1
                while startPointer < endPointer+1:
                    if endPointer-startPointer+1 <= k:
                        currMax = max(currMax, nums[startPointer])
                        pass

                    startPointer += 1

            maxList.append(currMax)
            

        return maxList


if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,1,0,4,2,6]
    k = 3
    print(sol.maxSlidingWindow(nums, k)) # [2,2,4,4,6]