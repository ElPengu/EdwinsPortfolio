class Solution:

    def numDistinct(self, s: str, t: str) -> int:
        '''
        - We have strings s and t
        - s and t consisting of ENGLISH characters
        - How many DISTINCT subsequences of s are equal to t?

        - EXAMPLE
        - s = "caaat", t = "cat"
        -> (c)aa(at)
        -> (c)a(a)a(t)
        -> (ca)aa(t)

        - Let's think
        - We could start at every letter and try to branch to every 
        possible subsequent letter recursively
        - Every recursive tree that creates t would be distinct

        - Clearly we can tidy this up!
        - First of all, let's start from the end of s
        - Every time a recursive tree returns TRUE we have a subsequence
        - To ensure that the subsequences are distinct, we can only 
        count a sequence if a call all the way down returns true

        - Let's go further!
        - How do we avoid repeating these DFS calls. I mean, we call at 
        the index -1 in s, and then at index -2 we recursively call at 
        -1 
        - What exactly do we ASK in a recursive call?
        - ...
        - At index i, we want to know whether there exists a path from 
        index i+1 such that we can form t by prepending the value at 
        index i
        - This implies that we must map every index to a set of strings 
        - There is also some criteria to adding a string to this set
        - The string must strictly be in t[1:]. I.e., it must be a 
        string starting at SOME index after index 0 in t, up to the end 
        of t

        - SOLUTION
        - Create dp: i->empty set
        - Iterate from the final index of s
        -> IF s[i] == t[-1]: ADD s[i] to dp[i]; BREAK
        - 
        - Iterate from i to 0
        -> FOR j>i:
        ->> IF s[i]+...

        - I am so close!!!

        
        '''

        pass

if __name__ == "__main__":
    sol = Solution()
    s = "caaat"
    t = "cat"
    print(sol.numDistinct(s,t)) # 3
    s = "xxyxy"
    t = "xy"
    print(sol.numDistinct(s,t)) # 5