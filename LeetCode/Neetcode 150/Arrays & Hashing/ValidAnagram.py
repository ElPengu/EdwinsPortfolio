class Solution(object):
    def isAnagram(self, s, t):
        #Two strings are anagrams if they contain the same letters at the same occurrences
        #Create a hash map
        #Counter for each letter in s
        #Decrement letters in map against t
        #Loop over map

        myMap = {}
        #Loop over string s
        for char in s:
            if char in myMap:
                myMap[char]+=1
            else:
                myMap[char]=1
        
        #Loop over string t
        for char in t:
            if char in myMap:
                myMap[char]-=1    
            else:
                return False
        
        for key in myMap:
            if myMap[key] != 0:
                return False
        return True
            

# Run test cases
if __name__ == "__main__":
    sol = Solution()
    s, t = "anagram", "nagaram"
    print(sol.isAnagram(s,t))  # Output: True
    s, t = "rat", "car"
    print(sol.isAnagram(s,t))  # Output: False
    