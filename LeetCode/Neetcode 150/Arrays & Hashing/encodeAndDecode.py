#To import List
from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        #We want to be able to read the string 
        #and decompose it into its constituent 
        #segments
        #
        #We create a new arr array
        #For each string, we count how many characters are in it
        #Next, we append the length,
        #then a pound symbol, and finally the string
        #In this way, we know that when we are at the start or we 
        #have exhausted a string, we expect a number
        #This number could be 1, 8, 1000, or whatever, but we read it
        #until we hit a pound symbol
        #At this point, we read characters until we are done. And repeat!

        #1. Create str
        myStr = ""

        #2. Start reading strings
        for s in strs:
            #Update str to have length of s
            myStr = myStr + str(len(s))
            #Update str to have pound symbol
            myStr = myStr + '#'
            #Update str to have s
            myStr = myStr + s 

        #3. Add '0' and a pound symbol to terminate
        myStr = myStr + '0'
        myStr = myStr + '#'

        #4. Return str
        return myStr
        
    def decode(self, s: str) -> List[str]:

        #Let charCount be for how many characters are left to count
        #When charCount hits zero, we now need to start 
        #reading numbers into an array until we hit a pound symbol
        #At this point we update charCount to be what is in the number
        #array
        #And we start reading characters into a string array, until
        #charCount hits zero, when we convert the string array to a string
        #and add it to a list of strings
        # 

        #1. Create string list
        stringList = [] 

        #2. Create charCount variable, set to 0
        charCount = 0

        #3. Create a charCount array
        charCountArr = []

        #4. Create a stringToAdd array
        stringToAddArr = []

        #5. Loop over chars in s <- O(n)
        for char in s:
            if charCount > 0:
                #If charCount is not zero, just append to stringToAddArr
                stringToAddArr.append(char)
                #Decrement charCount
                charCount -= 1
            else:
                #If we have a string to add, we add it!
                if len(stringToAddArr) > 0:
                    #Convert to a string
                    stringToAdd = "".join(stringToAddArr)
                    #Append to stringList
                    stringList.append(stringToAdd)
                    #We reset stringToAddArr
                    stringToAddArr = []
                #Regardless, we check if we are at a pound symbol or not
                if char == '#':
                    #In this case, convert charCountArr to charCount
                    charCount = "".join(charCountArr)
                    #Convert to int
                    charCount = int(charCount)
                    #Reset charCountArr
                    charCountArr = []
                else:
                    #We append it to charCountArr
                    charCountArr.append(char)

        #Return stringList
        return stringList
                




if __name__ == "__main__":
    sol = Solution()
    input = ["neet","code","love","you"]
    print(sol.decode(sol.encode(input))) # ["neet","code","love","you"]

    input = ["we","say",":","yes"]
    print(sol.decode(sol.encode(input))) # ["we","say",":","yes"]