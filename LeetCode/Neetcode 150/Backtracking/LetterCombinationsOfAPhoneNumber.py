from typing import List

class Solution:

    def letterCombinations(self, digits: str)->List[str]:

        # Mappings:
        # 2->(a,b,c), 3->(d,e,f), 4->(g,h,i), 5->(j,k,l),
        # 6->(m,n,o), 7->(p,q,r,s), 8->(t,u,v), 9->(w,x,y,z)
        # Clearly this is backtracking!
        # Store the mappings above in a hash map
        # Read through digits
        # At every possible choice make a recursive call
        # to DFS
        # In effect we consider every branch at a digit 
        # O(n*4^n)
        # > 4^n <- at worst case 7 and 9 we branch 
        # 4 times
        # > n <- Length of each output string is that 
        # of the input string

        # Stores our results
        res = []

        # Hash map of numbers to letters
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6" : "mno",
            "7":"pqrs",
            "8": "tuv",
            "9": "wxyz"

        }
        
        def backtrack(i, curStr):
            # i = index
            # curStr: The string that we are on

            # Base case
            # We have finished reading digits
            if len(curStr) == len(digits):
                # Add our current string
                res.append(curStr)
                # Exit this call
                return
            
            # We want to map our digit to the 
            # characters that it maps to
            # and loop over them
            for c in digitToChar[digits[i]]:
                # Make a call to backtrack 
                # on the next index
                # We also update our current
                # string
                backtrack(i+1, curStr+c)

        # Make a call on the first index
        if digits:
            # If we have no digits, we 
            # cannot call backtrack
            
            # Otherwise we'd return [[]] and not []
            backtrack(0, "")

        return res

if __name__ == "__main__":
    sol = Solution()
    digits = "34"
    print(sol.letterCombinations(digits)) # ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
    digits = ""
    print(sol.letterCombinations(digits)) # []
    