from typing import List

class Solution:

    def binarySearch(self, nums: List[int], target: int):

        res = -1

        # Set left and right pointers
        left, right = 0, len(nums)-1

        while left <= right:

            # Set mid
            mid = (left+right)//2

            if target == mid: return mid
            elif target > mid: left = mid+1
            else: right = mid-1

        return res

if __name__ == "__main__":
    sol = Solution()
    nums = [2,4,3,1,6,3]
    target = 3
    print(sol.binarySearch(nums, target)) # 2
