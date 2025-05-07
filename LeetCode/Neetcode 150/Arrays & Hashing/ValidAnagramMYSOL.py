class Solution(object):
    def isAnagram(self, s, t):
        # Create a mapping for string s
        sMap = {}
        for char in s:
            if char not in sMap: sMap[char] = 1
            else: sMap[char] +=1

        # Check if characters in t appear as much as in s
        for char in t:
            if char not in sMap: return False
            # We now guarantee that the character is in s
            sMap[char]-=1

        # If all characters in s appear as much as in t then all
        # keys should map to zero
        for char in sMap:
            if sMap[char] != 0: return False
        # No characters map to a count that is not zero!
        return True
            

# Run test cases
if __name__ == "__main__":
    sol = Solution()
    s, t = "anagram", "nagaram"
    print(sol.isAnagram(s,t))  # Output: True
    s, t = "rat", "car"
    print(sol.isAnagram(s,t))  # Output: False
    