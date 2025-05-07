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

        - Let us set an i and j pointer
        - How would we find ONE subsequence?
        - s = rabbbit, t = rabbit
        -> i,j=0,0
        -> s[i]==t[j]
        -> i,j=1,1
        -> s[i]==t[j]
        -> i,j=2,2
        -> s[i]==t[j]
        -> i,j=3,3
        -> s[i]==t[j]
        -> i,j=4,4
        -> s[i] = 'b', t[j] = 'i'
        -> We must INCREMENT i! Maybe the subsequence continues later 
        in the string
        -> i=i+1
        -> i,j = 5,4
        -> s[i] = 'i', t[j] = 'i'
        -> s[i] = 't', t[j] = 't'
        -> i,j = 6,5
        -> Base case, both remaining strings are "empty"
        -> RETURN 1

        - General solution SO FAR
        - SET i,j = 0,0
        - IF s[i]==t[j]: i,j=i+1,j+1
        - ELSE: i=i+1

        - How do we get the rest of the subsequences (there are three, 
        try and find them!)
        - In our IF condition we only consider subsequences where the 
        characters in s and t FIRST match
        - Another subsequence would be where s and t match, and we 
        compute that, but THEN we also consider the case where we peek at 
        the NEXT character in s
        - We essentially do the ELSE condition anyway and sum the 
        results!

        - Updated solution
        - SET i,j = 0,0
        - IF s[i]==t[j]: 
        -> DFS(i+1,j+1) + DFS(i+1,j)
        - ELSE:
        -> DFS(i+1,j)

        - CACHE
        - We notice that by doing this recursively, we WILL end up 
        looking at DFS(i+x,j) FORALL x>=0
        - The solution implies that repeated work may be done!
        -> Consider worst case, starting at i,j=0,0
        -> You'll do DFS(0,0) then maybe DFS(1,1) and DFS(1,0)
        -> Within the DFS(1,0) call you'll do maybe DFS(2,1) and 
        DFS(2,0)
        -> But then DFS(1,1) call may do DFS(2,2) and DFS(2,1)
        -> We repeat the DFS(2,1) call!
        - DFS(i,j) returns the number of distinct subsequences of s[i:] 
        to form t[j:]
        - We can store this in a cache to reduce repeated work!  
        - We will store dp[(i,j)]->paths
        - O(nm) time
        - O(nm) space

        - There are two more base cases
        - s, t = 'a', ''
        - There is ONE subsequeunce of s, that takes no elements
        - Hence, there is one distinct subsequence
        - RETURN 1

        - s, t = '', 'a'
        - No subsequence of s can be used to form t
        - RETURN 0
        
        '''

        # Set up cache
        cache = {}

        def dfs(i,j):
            if j == len(t):
                # We are at the base case as discussed, return 1
                return 1
            
            if i == len(s):
                # We are at the other base case, return 0
                return 0
            
            if (i,j) in cache:
                # Use the number of paths that has 
                # been calculated already
                return cache[(i,j)]
            
            if s[i] == t[j]:
                # We must run DFS

                # Call on remainder of s and t, then only on the 
                # remained of i
                cache[(i,j)] = dfs(i+1,j+1) + dfs(i+1,j)
            else:
                # Maybe the next character of s is the same as what 
                # we are pointing to in t
                cache[(i,j)] = dfs(i+1,j)
            return cache[(i,j)]
        
        # Call on the start of the strings
        return dfs(0,0)


if __name__ == "__main__":
    sol = Solution()
    s = "caaat"
    t = "cat"
    print(sol.numDistinct(s,t)) # 3
    s = "xxyxy"
    t = "xy"
    print(sol.numDistinct(s,t)) # 5