class Solution(object):
    def topKFrequent(self, nums, k):
        #Hash map for frequency of elements
        count = {}
        #Index frequency, value is list of values
        #occurring at that frequency
        #Hence we create as many empty lists for 
        #frequencies 0->size of nums
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
			#We use the dictionary to hold counts
			#for each num
            count[num] = 1 + count.get(num, 0)
	    # Get every key value pair that we added
        for num, cnt in count.items():
		    #The count is the index, we append 
		    #the num associated with that count
            freq[cnt].append(num)
        
        #This is the result output
        res = []
        
        #We start with the most frequently appearing
        #nums
        for i in range(len(freq) - 1, 0, -1):
            #We check each sublist, whether empty 
            #or not
            for num in freq[i]:
		        #We append, and stop when we have k
		        #values
                res.append(num)
                if len(res) == k:
                    return res
                
if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    print(sol.topKFrequent(nums,k)) #[1,2]
    nums = [1]
    k = 1
    print(sol.topKFrequent(nums,k))#[1]