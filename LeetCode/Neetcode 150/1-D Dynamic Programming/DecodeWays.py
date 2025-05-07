class Solution:

    def numDecodings(self, s: str) -> int:

        '''
        - 'A'->"1", 'B'->"2", ..., 'Z'->"26"
        - The message 1012 can be decoded like this
        -> "JAB" -> (10 1 2)
        -> "JL" -> (10 12)
        
        - NOTE: 
        -> No letter maps to 0
        -> Any double digits can start with 1
        -> A double digit starting with 2 MUST end 
        in 0-6

        - We use a cache dp to map indices to the 
        number of decodings starting at index i.
        
        - BASE CASE
        - We use the following BASE CASE: the empty 
        string maps to a single decode of ""
        -> Hence we set dp[N] = 1
        
        - INDUCTIVE STEP
        - We build up from the bottom, i.e. the end 
        of s, assuming that we start at index i in
        each turn
        - If we cannot start at i, set dp[i]=0
        - Else set dp[1]
        - If we can make a double from i, 
        set dp[i]+=dp[i+2] 

        - It is critical to understand the 
        distinction between cache dp and string s. It
        is subtle but important for the inductive 
        proof to work

        - This is unironically best understood by 
        reading the pseudocode and the comments 
        below. It will click basically immediately

        - # No string starting with 0 can be decoded
        - s[i]='0' -> dp[i]=0
        - s[i]!='0' -> dp[i]=dp[i+1] (i.e., no change)
        - IF i+1 < len(s):
        -> # If we have a 1 or 2 at i then we might
        have another choice!
        -> IF s[i] == '1' OR s[i] == '2' AND s[i+1] 
        in "0123456":
        ->> # We are saying that using s[i] AND s[i+1],
        we can create decoding for the REST of the 
        substring
        ->> # Rest assured, our base case is the EMPTY
        substring, and we only check when there is 
        index i+1 in s, so dp[i+2] will ALWAYS exist!
        ->> dp[i] += dp[i+2]


        - O(n) extra time
        - O(n) extra space
        '''

        # We initialise our cache
        # We map the entire string to 1. If we 
        # have an empty string we want to return 1
        # An empty string can be decoded in 1 way...
        # to nothing
        dp = {len(s):1}

        for i in range(len(s)-1,-1,-1):
            # We loop from the end index
            if s[i] == "0":
                # We cannot make a new way if we 
                # have a zero
                # More than that, as the start of a 
                # substring exactly ZERO decodings 
                # can be generated
                dp[i]=0
            else:
                # Using the number of ways from i+1, 
                # we can prepend the character at 
                # i for each of them. So no NEW ways
                dp[i]=dp[i+1]
            if (i+1 < len(s) and (s[i]== '1' or 
                s[i]=='2' and s[i+1] in "0123456")):
                # If we have a succeeding character 
                # AND we are at a 1 or a 2 followed 
                # by a value 0-6, we 
                dp[i]+=dp[i+2]
        return dp[0]


        

if __name__ == "__main__":
    sol = Solution()
    s = "12"
    print(sol.numDecodings(s)) # 2
    s = "01"
    print(sol.numDecodings(s)) # 0