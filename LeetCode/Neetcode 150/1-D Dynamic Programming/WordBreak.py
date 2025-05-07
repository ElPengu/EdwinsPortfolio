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

        - BRUTE FORCE
        - We could naively check one character at a time until 
        we reach a word in wordDict.
        -> E.g., for ["neet","code"]
        -> n, ne, nee, neet -> neet, "neet"c, ... 
        - Instead we will check entire words substrings
        at a time
        -> E.g., for ["neet","code"]
        -> neet != "code", neet == "neet", "neet"code ...
        
        - DECISION TREE
        - For every word we will check the associated prefix
        - E.g., s="neetcode", wordDict = ["neet","leet","code"]
        -> i=0
        -> 'neet' == "neet" -> i=4
        ->> neet'code' != "neet"
        -> RETURN FALSE
        ->> neet'code' == "code" i=8
        ->> i=8=len(s)
        ->> RETURN TRUE

        - BOTTOM-UP APPROACH
        - We want to only check every index at most ONCE in the 
        decision tree
        - Let DP be a cache, where DP[i] marks whether the substring
        starting at s[i] is a valid wordbreak
        - DP[N] = TRUE
        -> This is an empty substring, use a word zero times to create
        it
        - DP[i] = DP[i+len(word)]
        -> s[i:] can only be word broken after fitting the word
        if the remainder of the substring can also be word broken
        - EXAMPLE
        - s="neetcode", wordDict = ["neet",
        "leet","code"]
        -> DP[8] = True <- BASE CASE
        -> i=7,6,5
        -> i=4
        -> Can a word in wordDict start at i=4 AND be equal?
        -> Yes! code
        -> DP[4] = DP[4+len("code")] = DP[8] = True
        -> i=3,2,1
        -> i=0
        -> Can a word in wordDict start at i=0 AND be equal?
        -> Yes! "neet"
        -> DP[0] = DP[0+len("neet")] = DP[4] = True
        -> RETURN DP[0]
        '''

        # Set DP with base case as last position being true
        dp = [False] * (len(s)+1)
        dp[len(s)]=True

        for i in range(len(s)-1,-1,-1):
            # Check each index IN REVERSE

            for w in wordDict:
                # Try every word for portion
                if (i+len(w)) <= len(s) and s[i:i+len(w)]==w:
                    # Can the string s even fit word from index i?
                    # Does the portion of s from index i prefix with 
                    # word?

                    # We only care about fitting this word here IF
                    # the rest of the string is also word break
                    dp[i] = dp[i+len(w)]
                    
                    pass
                if dp[i]:
                    # We only care about ONE possible
                    # match at index i
                    break
        return dp[0]



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