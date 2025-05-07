from collections import defaultdict

class Solution(object):
    def twoSumATTEMPTONE(self, nums, target):
        # We want the indices of two nums that sum to target
        # A solution: 
        # - Mapping 1: {num: index}
        # Loop over nums. If num and target-num appear in mapping,
        # return indices!
        # 
        # How to separate indices...
        # 
        # Every number can map to multiple indices
        # So we need each number to map to a LIST 
        # of indices
        # Then if we have num == target we return 
        # the first two elements in the list

        numToIndex = defaultdict(list)
        # Create mappings
        for i in range(len(nums)):
            numToIndex[nums[i]].append(i)

        for num in nums:
            # Check if num and difference appear 
            # in mapping
            difference = target - num
            if (num in numToIndex) and (difference in numToIndex):
                # Return smaller index first
                if num != difference: return [numToIndex[num][0], numToIndex[difference][0]]
                else: 
                    if not len(numToIndex[num]) > 1: continue
                    return [numToIndex[num][0], numToIndex[difference][1]]
            
        # We are guaranteed a solution

    def twoSum(self, nums, target):
        # We check each index, number
        # If its difference is NOT in the hash map,
        # add num->index to a map

        # Create hash map
        numToIndex = {}

        # Enumerate nums
        for i, num in enumerate(nums):
            # Get difference
            difference = target - num
            # See if difference in map
            if difference in numToIndex:
                return [numToIndex[difference], i]
            numToIndex[num] = i

# Run test cases
if __name__ == "__main__":
    sol = Solution()
    nums = [2,7,11,15]
    target = 9
    print(sol.twoSum(nums, target)) # [0,1] or [1,0]
    nums = [3,2,4]
    target = 6
    print(sol.twoSum(nums, target)) # [1,2] or [2,1]
    nums = [3,3]
    target = 6
    print(sol.twoSum(nums, target)) # [0,1] or [1,0]