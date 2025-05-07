class Solution:

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        - We have strings s1,s2,s3
        - Can s3 be formed by interleaving s1 and s2
        - Interleaving strings s and t is done by dividing them into 
        substrings n and m s.t.
        -> |n-m| <= 1 <- There is at most a difference of 1 between 
        |n| and |m| 
        -> s = s1+s2+...+sn
        -> t = t1+t2+...+tm
        -> Interleaving s and t is s1+t1+s2+t2+... OR t1+s1+t2+s2+...
        - Lower-case English letters for s1,s2,s3
        
        - That is one explanation...
        - From what I got, you want to choose letters from s1 in order, 
        then letters from s2, and back and forth, and then reach a 
        string t
        - At t you want s1Count=number of times you have selected from s1, 
        same idea for s2Count regarding s2
        - If you reach string t but your |s1Count-s2Count|>1 you have failed 
        - Else return t==s3

        - Okay, wow
        - BRUTE FORCE 
        - Start with empty string t
        - Set s1Pointer, s2Pointer
        - Set s1Count, s2Count
        - Choose to either select a character from s1Pointer or s2Pointer 
        and append to t in DFS fashion
        - Update all variables appropriately
        - When s1Pointer and s2Pointer finished s1 and s2, verify that 
        |s1Count-s2Count| <= 1
        - If so, return t == s3

        - Memoisation
        - What are we going to repeat?
        - You might select from s1 3 times, then s2 3 times
        - You might also select from s1, then s2, and repeat this 3 times 
        - In both cases we want to know about the same remaining branches 
        - Hence, we can store DP[s1Pointer][s2Pointer] = bool
        - How about s1Count and s2Count?
        - Do we need s1Count and s2Count?
        - 
        '''


        pass


if __name__ == "__main__":
    sol = Solution()
    s1 = "aaaa"
    s2 = "bbbb"
    s3 = "aabbbbaa"
    print(sol.isInterleave(s1,s2,s3)) # True
    s1 = ""
    s2 = ""
    s3 = ""
    print(sol.isInterleave(s1,s2,s3)) # True
    s1 = "abc"
    s2 = "xyz"
    s3 = "abxzcy"
    print(sol.isInterleave(s1,s2,s3)) # False
