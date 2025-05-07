from typing import List
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # An anagram will have the same character counts
        # We store info in array of 26 indices

        charCountMap = defaultdict(list)

        for str in strs:
            # Generate array of 26 zeroes
            count = [0]*26

            for c in str:
                #Map letter using ascii
                count[ord(c)-ord('a')]+=1
            # Make count hashable
            count = tuple(count)
            #Store in map
            charCountMap[count].append(str)

        res = []

        for key,val in charCountMap.items(): res.append(val) 

        return res
    
    
if __name__ == "__main__":
    sol = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"] # [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(sol.groupAnagrams(strs)) # [["bat"],["nat","tan"],["ate","eat","tea"]]
    strs = [""]
    print(sol.groupAnagrams(strs))  # [[""]] 
    strs = ["a"] # [["a"]]
    print(sol.groupAnagrams(strs)) # [["a"]] 