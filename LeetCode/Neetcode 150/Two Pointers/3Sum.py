from typing import List
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #This is a standard 2 sum problem type
        #My idea
        #Create a list of tuples: (num, index)
        #Sort nums into non-increasing <- O(nlogn) time
        #Select a num to be target*-1
        #x+y+target=0 -> x+y=-target
        #Set left and right pointers
        #While left < right, compare numbers
        #If left -> target, increment
        #If right -> target, decrement
        #If nums[left] + nums[right] < target, we need a 
        #bigger number
        #left += 1
        #If nums[left] + nums[right] > target, we need a 
        #smaller number
        #right -= 1
        #Else, we have a solution
        #Find indices using hash map, put 
        #into a set, and add it to a set of solutions
        #O(n2) time

        #Solutions set
        solutions = set()

        #Sort nums
        nums.sort()

        #Loop over every index
        for targetIndex in range(len(nums)):
            #Set target to reach
            target = nums[targetIndex]*-1

            #Set left and right pointers
            left = 0
            right = len(nums)-1

            while left < right:

                #If left or right is at target
                #index, update
                while left == targetIndex:
                    left +=1
                while right == targetIndex:
                    right -= 1

                #Now we check the sum
                if nums[left]+nums[right] < target:
                    #We need a bigger number
                    #Shift left up
                    left += 1
                elif nums[left]+nums[right] > target:
                    #We need a smaller number
                    #Shift right down
                    right -= 1
                else:
                    #We have found a triple that 
                    #sums to zero!
                    
                    #Sort, this is an O(1) time operation since we only deal with triples
                    solution = [nums[left], nums[right], nums[targetIndex]]
                    solution.sort() 
                    #We can only add non-mutable elements to a hash set
                    solution = tuple(solution)

                    solutions.add(solution)
                    break

        #Convert solutions to a list
        solutions = list(solutions)
        #Convert entries in solutions to list
        for i in range(len(solutions)):
            solutions[i] = list(solutions[i])

        return solutions
                     
if __name__ == "__main__":
    sol = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(sol.threeSum(nums)) # [[-1,-1,2],[-1,0,1]]
    nums = [0,1,1]
    print(sol.threeSum(nums)) # []
    nums = [0,0,0]
    print(sol.threeSum(nums)) # [[0,0,0]]
        