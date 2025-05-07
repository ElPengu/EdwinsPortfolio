from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        # We want the k most frequent
        # Can we do this in n time?
        # 
        # Every number can appear at most len(nums) times
        # PHASE 1: Store count for each number
        # PHASE 2: Map each possible count to num list
        # PHASE 3: Return k top numbers

        # PHASE 1
        numCount = {}
        for num in nums:
            if num not in numCount: numCount[num]=0
            numCount[num]+=1
        
        #PHASE 2
        countMap = defaultdict(list)
        for num, count in numCount.items():
            countMap[count].append(num)

        # PHASE 3
        res = []

        for i in range(len(nums),-1,-1):
            numList = countMap[i]
            for num in numList:
                res.append(num)
                k-=1
                if k == 0: return res

        
        pass
                
if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    print(sol.topKFrequent(nums,k)) #[1,2]
    nums = [1]
    k = 1
    print(sol.topKFrequent(nums,k))#[1]