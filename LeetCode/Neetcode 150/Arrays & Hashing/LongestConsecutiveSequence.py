class Solution:

    def longestConsecutive(self, nums):
        #Conceptually you can imagine a number line: (-inf,inf)
        #You want to place every num in nums on the number line
        #The longest sequence with no gaps is the solution
        #Note that a sequence starts with a number preceded by 
        #a gap

        #We check each number
        #If it has a predecessor in the set, we do nothing
        #Else, it is the start of a sequence. 
        #We check for each successor until a successor is not in the set
        #We keep track of the sequence

        numsSet = set(nums)
        maxLength = 0

        for num in numsSet:
            if (num-1) not in numsSet:
                #This is the start of a new sequence
                length = 1
                while (num+length) in numsSet:
                    #We check for successors
                    length += 1
                maxLength = max(maxLength, length)            

        return maxLength




if __name__ == "__main__":
    sol = Solution()
    nums = [2,20,4,10,3,4,5]
    print(sol.longestConsecutive(nums)) # 4

    nums = [0,3,2,5,4,6,1,1]
    print(sol.longestConsecutive(nums)) # 7