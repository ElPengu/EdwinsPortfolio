from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        - We have a string s and strings in wordDict
        - We want to see if s can be segmented into
        words, as if it is a sentence
        - E.g., "neetcode" -> "neet" + " " + "code" 
        - You may reuse dictionary words
        - You needn't use ALL words
        - You may assume all dictionary words are 
        unique

        - Let's start with a base case
        - An empty string may or may not be in 
        wordDict
        - We can set DP[-1] to this value
        - Now we start at index 0
        - BASE CASE: DP[-1] = True or False

        - INDUCTIVE STEP
        - Is DP[i-len(word):i+1] == word?

        - Hm
        - I think more info is needed in DP

        - DP[-1] is for the empty string
        - We ask ourselves, is "" a valid substring?
        - Always! Just use a word in wordDict 0 times!
        - Specifically, we should check every word in 
        wordDict
        - Now we move onto index 0
        - We ask ourselves: is substring s[0:1] in 
        wordDict?
        - If this is the case AND DP[-1] is TRUE, 
        set DP[0] = TRUE

        - O(n*m) extra time
        -> n = characters in s
        -> m = words in wordDict

        - I AM SO CLOSE, UGHHHH
        - Work day is over, maybe 25 mins on this
        - I swear it is the logic of the IF statement,
        because the logic of the entire thing seems
        great!

        - Checked with GPT, just ~5 lines need to be 
        tweaked and 1 added
        '''
        
        # Size of s
        N = len(s)-1

        # Initialise DP array
        dp = {}
        # -1 => empty substring, always valid
        dp[-1] = True


        for i in range(N):
            # Check every character index

            # Initially set DP at this index to false
            dp[i] = False

            for word in wordDict:
                
                if (s[i-len(word):i+1] == word
                    and
                    dp[i-len(word)-1] == True
                    ):
                    # The splice of s UP TO AND 
                    # INCLUDING i must be the word
                    # I.e....
                    # Start index of splice: i-len(word)
                    # End index of splice: i
                    # 
                    # We must ALSO be able to create
                    # a sentence ending at the index BEFORE
                    # the start of the splice
                    # dp[i-len(word)-1]



                    dp[i] = True


        return dp[N-1]


if __name__ == "__main__":
    sol = Solution()
    s = "neetcode"
    wordDict = ["neet","code"]
    print(sol.wordBreak(s,wordDict)) # True
    s = "applepenapple"
    wordDict = ["apple","pen","ape"]
    print(sol.wordBreak(s,wordDict)) # True
    s = "catsincars"
    wordDict = ["cats","cat","sin","in","car"]
    print(sol.wordBreak(s,wordDict)) # False