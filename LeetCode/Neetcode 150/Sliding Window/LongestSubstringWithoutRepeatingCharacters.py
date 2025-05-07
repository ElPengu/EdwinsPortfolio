class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # 1. Set variables for the maxLength seen so far, 
        # the current length we are at, and a set of chars
        maxLength = 0
        currLength = 0
        mySet = set()

        # 2. Loop over all elements in s
        for i in range(len(s)):
            
            # If we have NOT seen this element, we must 
            # add it to the set
            if s[i] not in mySet:
                mySet.add(s[i])
                # We see that the current length is incremented
                currLength += 1
            else:
                # We HAVE seen this element, so the substring 
                # has ended
                # Update maxLength and reset the current length
                maxLength = max(maxLength, currLength)
                currLength = 0

                # We also empty the set
                mySet = set()
        return maxLength

if __name__  == "__main__":
    sol = Solution()
    s = "zxyzxyz"
    print(sol.lengthOfLongestSubstring(s)) # 3
    s = "xxxx"
    print(sol.lengthOfLongestSubstring(s)) # 1