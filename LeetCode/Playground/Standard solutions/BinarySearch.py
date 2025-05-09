from typing import List

class Solution:

    def binarySearch(self, nums: List[int], target:int)->int:

        def binSearch(subList, firstIndex):
            if not subList:
                # Target not found
                return -1

            # Get left and right indices
            l, r = 0, len(subList)-1

            # Get midpoint
            m = l+((r-l)//2)

            if subList[m] == target:
                return firstIndex+m
            
            if subList[m] < target:
                return firstIndex+binSearch(subList[m+1:],m+1)
            else:
                return firstIndex+binSearch(subList[:m],firstIndex)
            
        print(nums)
        return binSearch(nums, 0)

    pass

if __name__ == "__main__":
    sol = Solution()
    nums = [1,4,5,7,12,25]
    target = 12
    print(sol.binarySearch(nums, target))