class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        '''
        - We have strings text1 and text2
        - Find the length of the common subsequence
        - Subsequence: sequece that can be derived by deleting >=0 
        elements without changing the relative order of the remaining
        elements
        - "cat" is subsequence of "crabt"
        - Common subsequence is two that exist in both strings

        - We want the longest common subsequence up to index i in text1 
        and index j in text2
        - We'll work backwards to build the habit
        - Okay, let M = length of text1, N be length of text2
        - What is the length of the longest common subsequence starting
        at (M,N)? 0, it will be ""
        - BASE CASE: (M,N)->0
        - How can we derive the longest common subsequence starting at 
        (i,j)?
        - Okay, let's say that this can be done through (i+1,j+1). What 
        does it MEAN? What would make it certain that this is the case?
        - ...
        - It would be each time you match!
        - Take "cat", "crabt"
        - (3,5)->0
        - (3,4),...,(3,0)->0
        - (2,5)->0, (2,4)->1, (2,3),...,(2,0)->1
        
        - ENHANCEMENT
        - In fact, our base case can be enhanced!
        - BASE CASE
        - (M-1,N-1)-> 1 IFF text[M-1]==text[N-1]
        - (i,j) = max(I,J) s.t. I>i, J>j
        - (i,j)+=1 IFF text1[i]==text2[j]

        - DAKIKA ISHIRINI NA NANE, WAJUA!
        - URA!
        '''

        # Get lengths of text1 and text2
        m,n = len(text1), len(text2)

        curMax = 0
        
        # BASE CASE - generate mxn grid
        dp = []
        for i in range(m):
            iList = []
            for j in range(n):
                iList.append(0)
            dp.append(iList)
        # INDUCTIVE STEP
        for i in range(m-1,-1,-1):
            
            curMaxClone = curMax
            for j in range(n-1,-1,-1):
                

                dp[i][j] = curMax
                if text1[i] == text2[j]:
                    dp[i][j]+=1

                curMax = max(curMax,dp[i][j])
        # Length found at (0,0)
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