from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 
        # We want to remember at index i the previous temps that
        # we have seen and the distance to the previous 
        # We can use a stack to remember this
        # 
        # Consider [73,74,...]
        # We see that temp 1 is warmer than temp 0, and the distance is 
        # obviously 1. So we append a 1 to the output and pop index 0
        # So monotonic increasing order temps here
        # 
        # But what if we have [73,72,...]?
        # 
        # So we see that our stack will be in monotonic (not strictly) 
        # decreasing order
        # 
        # Here is an O(n) worked example
        # [73,74,75,71,69,72,76,73]
        # We store temp and index in the stack
        # We start appending temps to the left side of the stack.
        # If you append a decrease in temp to the tail, pop the tail 
        # and add the distance between temp i and the tail to the index 
        # of tail
        # At the end, indices of remaining temps are 0
        # 

        # Default of zeros
        res = [0] * len(temperatures)

        # Stack with temperature and index
        stack = [] # Pair: [temp, index]

        # Loop through the temperatures array
        # We will enumerate to get the index and temp
        for i, t in enumerate(temperatures):
            # While there are lower temperatures at the tail
            while stack and t > stack[-1][0]:
                # In this case, we immediately pop the temp and index 
                # in the stack at the tail
                stackT, stackInd = stack.pop()
                # In the result value for the index, we add the 
                # difference to the newly added temp
                res[stackInd] = (i-stackInd)

            # Now we append current temp and index to the stack
            stack.append([t,i])

        #Return the result
        return res
        pass


if __name__ == "__main__":
    sol = Solution()
    temperatures = [30,38,30,36,35,40,28]
    print(sol.dailyTemperatures(temperatures)) #[1,4,1,2,1,0,0]
    temperatures = [22,21,20]
    print(sol.dailyTemperatures(temperatures)) # [0,0,0]
