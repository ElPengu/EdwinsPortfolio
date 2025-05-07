class Solution:

    def CheckInclusion(self, s1: str, s2: str) -> bool:
        #If s1 is longer, return false immediately
        if len(s1) > len(s2):
            return False
        
        #Create an array for s1 and s2 
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            #We create a mapping from letter (by 
            #an index relative to 0->a) to frequency
            #count for the length of s1
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0

        #Compare the maps/arrays for each letter
        for i in range(26):
            #Increment matches for each equal mapping
            if s1Count[i] == s2Count[i]:
                matches += 1

        #Now we start analysing the sliding window
        #We assign left pointer to 0, and right pointer to 
        #however long s1 is. Then we start shifting along!
        l = 0
        for r in range(len(s1), len(s2), 1):

            #Return true if we have 26 matching letters
            if matches == 26:
                return True

            #Get index of the character at r
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                #In this case, they WERE equal, but
                #by adding the character the substring
                #s2 has one more of the character
                matches -= 1

            #We also removed a character since l moves
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                #In this case, they WERE equal, but 
                #by removing the character the substring
                #s2 has one less of the character
                matches -= 1

            #Finally, increment left counter
            l += 1
        
        #Return if matches == 26
        return matches == 26

    def CheckInclusionBADRUNTIME(self, s1: str, s2: str) -> bool:
        # Put s1 into s1Set
        # Create a list called s2SubList
        # Loop over s2 <- O(len(s2))
        # If the length of s2SubList < length of s1, append char
        # Else, create s2SubSet, check if s2SubSet == s1Set <- O(len(s1))
        # If so, return True
        # Else, remove first element of s2SubList and append char <-O(1)
        
        #1. Put s1 into s1Set
        s1Set = set(s1)

        #2. Create s2SubList
        s2SubList = []

        #3. Iterate over s2
        for c in s2:
            if len(s2SubList) < len(s1):
                s2SubList.append(c)
            else:
                s2SubSet = set(s2SubList)
                if s2SubSet == s1Set:
                    return True
                else:
                    #Remove value at index 0
                    s2SubList.pop(0)
                    #Append c
                    s2SubList.append(c)

        #No permutation of s1 found in s2
        return False



if __name__ == "__main__":
    sol = Solution()
    s1, s2 = "abc", "lecabee"
    print(sol.CheckInclusion(s1, s2)) # true
    s1, s2 = "abc", "lecaabee"
    print(sol.CheckInclusion(s1, s2)) # false