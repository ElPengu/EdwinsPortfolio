class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        '''
        - This is a *very* popular problem!

        - We have strings text1 and text2
        - Find the length of the common subsequence
        - Subsequence: sequece that can be derived by deleting >=0 
        elements without changing the relative order of the remaining
        elements
        - "cat" is subsequence of "crabt"
        - Common subsequence is two that exist in both strings

        - We have to handshake on these two pieces 
        of intuition: 
        -> s1="abcde" and s2="ace" combined with the 
        fact that s1[0]=s2[0] implies that the 
        comSub(s1,s2) = 1+comSub(s1[1:],s1[1:])
        -> s1="abcde" and s2="cae" combined with the 
        fact that s1[0]!=s2[0] implies that the 
        comSub(s1,s2)=max(comSub(s1[1:],s2),
        comSub(s1,s2[1:]))
        
        - INTUITION THROUGH EXAMPLE
        - Let s1, s2 = "abcde", "ace"
        - Let comSub = common subsequence
        - Generate matrix where i is for s1, j is 
        for s2
        - Start at i,j=0,0
        - s1[0]==s2[0]=>TRUE
        - Therefore longest comSub at (0,0) = 1+(1,1)
        - Why?
        - At (1,0) and (0,1) we SKIP an 'a'... but 
        we do this already at (1,1), so we needn't 
        consider it because we want a longer comSub
        - Okay, at i,j=1,1
        - s1[1]==s2[1]=>FALSE
        - The longest comSub is EITHER (1,1)=0+(1,2) 
        OR (1,1)=0+(2,1)
        - We continue on

        - BASE CASE
        - LET m = len(text1), n = len(text2)
        - We will initialise all elements at the mth 
        column and nth column to 0
        - INDUCTIVE CASE
        - IF text1[i]==text2[j]: dp[i][j] = 1+dp[i+1][j+1]
        - ELSE: dp[i][j] = max(dp[i+1][j],dp[i][j+1])

        - O(mn) space <- We consider every way that 
        a character at index i in text1 can match 
        a character at index j in text2 EXACTLY once
        - O(mn) time <- each space takes constant 
        time operations

        - DAKIKA ISHIRINI NA NANE, WAJUA!
        - URA!
        '''

        # BASE CASE - All elements are 0
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                # Work from the bottom right of the 
                # matrix inwards

                if text1[i] == text2[j]:
                    # They match! Use the diagonal!
                    dp[i][j] = 1+dp[i+1][j+1]
                else:
                    # They don't match
                    # Take the max of the right and 
                    # the bottom
                    dp[i][j] = max(dp[i+1][j],
                                   dp[i][j+1])

        # Longest subsequence found at (0,0)
        return dp[0][0]

if __name__ == "__main__":
    sol = Solution()
    text1 = "cat"
    text2 = "crabt" 
    print(sol.longestCommonSubsequence(text1,text2)) # 3
    text1 = "abcd"
    text2 = "abcd"
    print(sol.longestCommonSubsequence(text1,text2)) # 4
    text1 = "abcd"
    text2 = "efgh"
    print(sol.longestCommonSubsequence(text1,text2)) # 0