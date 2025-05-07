class Solution(object):
    def containsDuplicateONE(self, nums):
        # Create a set
        numsSet = set()

        # Initialise size variable
        size = len(numsSet)

        # Iterate over nums
        for num in nums:
            # Add a numbers
            numsSet.add(num)

            # If the size is the same we added a duplicate
            if len(numsSet) == size:
                return True

            # Update size
            size = len(numsSet)
        # We never added a duplicate
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