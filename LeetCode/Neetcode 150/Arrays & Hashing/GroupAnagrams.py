from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        #To map character count to a list of anagrams
        res = defaultdict(list)
        
        #Loop over each string
        for s in strs:
		        #Start with an empty array of 26 zeroes
            count = [0] * 26
            #Count how many times each char appears
            for c in s:
		            #We use the ASCII value of the characters to 
		            #make this easier
                count[ord(c) - ord('a')] += 1
            #Convert to a tuple which is non-mutable
            #NOTE: Even if the count is not a key,
            #as soon as the new key is added its 
            #default value is a list, so we can add to 
            #it immediately
            
            res[tuple(count)].append(s)
            
        #We return the values (read lists) of the 
        #map in list format!
        return list(res.values())
    
    # Run test cases
if __name__ == "__main__":
    sol = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"] # [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(sol.groupAnagrams(strs)) # [["bat"],["nat","tan"],["ate","eat","tea"]]
    strs = [""]
    print(sol.groupAnagrams(strs))  # [[""]] 
    strs = ["a"] # [["a"]]
    print(sol.groupAnagrams(strs)) # [["a"]] 