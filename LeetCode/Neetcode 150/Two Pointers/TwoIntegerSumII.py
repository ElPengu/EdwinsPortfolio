from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # - CONCEPT: Note that the list is non-decreasing
        # - When two numbers sum up to over the target, you 
        # - are also seeing that numbers to the left and right
        # - of those numbers have the same property 
        # - Same idea for when they sum to under the target
        # - So when you update left and right, nothing 
        # - to the left of left nor to the right of right
        # - matters because for the purposes of this problem, 
        # - they hold the same property regarding summing to target

        #Set two pointers left and right
        #If left+right<target, we need a bigger number
        #This is achieved by incrementing left
        #If left+right>target, we need a smaller number
        #This is achieved by decrementing right
        #If left+right==target and they don't point to the same number,
        #return the indices

        left = 0
        right = len(numbers)-1
        while left < right:
            if numbers[left]+numbers[right] < target:
                left+=1
            elif numbers[left]+numbers[right] > target:
                right-=1
            else:
                if numbers[left] != numbers[right]:
                    #Note that we want 1-indexed values
                    return [left+1,right+1]
            

        pass

if __name__ == "__main__":
    sol = Solution()
    numbers = [1,2,3,4]
    target = 3
    print(sol.twoSum(numbers, target)) # [1,2]
