from typing import List

class Solution:

    def merge(self, nums:List[int], leftHalf:List[int], rightHalf:List[int]):

        k = 0
        i,j=0,0
        while (i<len(leftHalf)) and (j<len(rightHalf)):
            if leftHalf[i]<rightHalf[j]:
                nums[k]=leftHalf[i]
                i+=1
            else:
                nums[k]=rightHalf[j]
                j+=1
            k+=1
        while (i<len(leftHalf)):
            nums[k]=leftHalf[i]
            k+=1
            i+=1
        while (j<len(rightHalf)):
            nums[k]=rightHalf[j]
            k+=1
            j+=1
        return nums

    def mergeSort(self, nums: List[int]):
        if len(nums)>1:
            # We have to sort this array

            mid = len(nums)//2

            # Split it up into left and right halves
            leftHalf = self.mergeSort(nums[0:mid])
            rightHalf = self.mergeSort(nums[mid:len(nums)])

            # Merge them
            nums = self.merge(nums, leftHalf, rightHalf)
            
        return nums

if __name__ == "__main__":
    sol = Solution()
    nums = [3,5,2,5,1,11,0]
    print(sol.mergeSort(nums)) # [0,1,2,3,5,5,11]
    nums = [3,1]
    print(sol.mergeSort(nums)) # [1,3]
    nums = [0]
    print(sol.mergeSort(nums)) # [0]