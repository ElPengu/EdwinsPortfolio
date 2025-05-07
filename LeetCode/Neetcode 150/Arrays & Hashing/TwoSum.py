class Solution(object):
    def twoSum(self, nums, target):
        #Create a hash map
        #Key = value
        #Value = index
        #Add to the hash map **after** checking the value

        #Create hash map
        myMap = {}
        #Loop over nums
        for i in range(len(nums)):
            #Check against the hash map
            if myMap.get(target-nums[i]) != None:
                return [i, myMap.get(target-nums[i])]
            else:
                myMap[nums[i]] = i

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