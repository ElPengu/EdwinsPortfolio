class Solution(object):
    def containsDuplicate(self, nums):
        #Create a set
        mySet = set()

        #Loop over nums
        for num in nums:
            #If num is not in mySet, add it
            if (num in mySet) == False:
                mySet.add(num)
            else:
                #We have seen a duplicate
                return True
        #Exited loop, hence no duplicates seen!
        return False
    
# Run test cases
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1]
    print(sol.containsDuplicate(nums))  # Output: True
    nums = [1,2,3,4]
    print(sol.containsDuplicate(nums))  # Output: False
    nums = [1,1,1,3,3,4,3,2,4,2]
    print(sol.containsDuplicate(nums))  # Output: True