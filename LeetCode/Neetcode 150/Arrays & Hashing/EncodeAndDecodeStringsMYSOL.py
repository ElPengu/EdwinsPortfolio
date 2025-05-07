#To import List
from typing import List

class Solution2: 

    '''
    - Any string has x characters
    - To encode we shall prepend a string with some 
    characters for length
    - Followed by '#' as delimiter
    '''

    def encode(self, strs: List[str]) -> str:

        res = ""

        # Read strs
        for s in strs:
            # Find size of s
            sLen = len(s)
            # Convert sLen to string
            sLen = str(sLen)
            # Append to res with delimiter and s
            res += sLen + '#' + s
        return res

    
    def decode(self, s: str) -> List[str]:
        res = []
        
        # Read until we are at the end of s
        i = 0
        while i < len(s):
            # Find sLen
            sLen = ""
            while s[i] != '#':
                sLen+=s[i]
                i+=1
            # Now i is at '#'
            # Convert sLen to integer
            sLen = int(sLen)
            # Increment i
            i+=1

            # Read sLen characters to add
            sToAdd = ""
            sLen+=i
            while i < sLen:
                sToAdd+=s[i]
                i+=1
            res.append(sToAdd)
        return res
        

class Solution:
    '''
    - We want to be able to know how many characters
    - to read for per string within the encoded 
    - string
     
    - We store the length of the string in characters
    - E.g. 12 -> "12"

    - We know the string ends at delimiter '#'

    - After which we read the string

    - If we see '0#' then we know that the last string
    is size zero, so we don't add
    '''

    def encode(self, strs: List[str]) -> str:
        # Create a base string
        encodedStr = ""

        # Read each string
        for s in strs:
            # Find the length of the string
            strLen = len(s)
            # Convert string length to string format
            strLen = str(strLen)
            # Append this to the encoded string with delimiter
            encodedStr+=strLen+'#'+s
        
        # Now each string component is prepended by a readable size

        # We append 0# to know that there are no more strings to read
        encodedStr+="0#"

        # Return the encoded string
        return encodedStr
        
    def decode(self, s: str) -> List[str]:

        # Read the encoded string
        encodedStr = s

        # Create a list of strings
        decodedStr = []
        i = 0
        while i < len(encodedStr):
            # Read digits
            digits = ""
            while encodedStr[i] != '#':
                digits+=encodedStr[i]
                i+=1
            # Convert digits to integer
            digits = int(digits)
            if digits == 0:
                # There are no more digits to read
                break
            # There are digits to read
            strToAdd = ""
            # Move past delimiter
            i+=1
            for j in range(digits):
                strToAdd+=encodedStr[i]
                i+=1
            # Add the string
            decodedStr.append(strToAdd)


        return decodedStr
           
if __name__ == "__main__":
    sol = Solution2()
    input = ["neet","code","love","you"]
    print(sol.decode(sol.encode(input))) # ["neet","code","love","you"]

    input = ["we","say",":","yes"]
    print(sol.decode(sol.encode(input))) # ["we","say",":","yes"]