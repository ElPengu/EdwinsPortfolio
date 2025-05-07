class Solution:

    def isMatch(self, s: str, p: str) -> bool:

        '''
        - We have s, lower case English letters
        - Pattern p, lowercase English letters 
        AND '.' and '*' characters
        - '.' matches ANY single character
        - '*' matches zero or more of the 
        preceding element
        - E.g., ".*" means match zero or more of 
        ANY character
        - E.g., "a*" means match zero or more of
        the 'a' character

        - Clearly we need a matrix, so lets put s 
        on the x-axis and p on the y-axis
        - It would be easier to match p to s than 
        the other way round
        - We build string s using pattern p

        - If we reach from index 0 in p, if you see 
        a letter you want to match it, if you see a 
        '.' you continue
        - What do you do if you see a '*'?
        - You need to see what the previous character 
        is
        - Now you have a choice, do you repeat it or 
        do you stop?
        - You must have a branch for the number of times 
        that you select the character, and then try to 
        complete each branch. If any can create s, you 
        must return TRUE

        - That was the brute force way, is there any 
        repeated work that we can cache?
        - Every branch must terminate when a pattern 
        has generated a string equal to the size of 
        p
        - So we can say that ...

        - Now I am a bit confused
        - When you make a choice at index i, what do you 
        want to store?
        '''


        pass


if __name__ == "__main__":
    sol = Solution()
    s = "aa"
    p = ".b"
    print(sol.isMatch(s,p)) # False
    s = "nnn"
    p = "n*"
    print(sol.isMatch(s,p)) # True
    s = "xyz"
    p = ".*z"
    print(sol.isMatch(s,p)) # True