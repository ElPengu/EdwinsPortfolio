class Solution:

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

    - The '.' is not too difficult, but the 
    '*' makes things difficult

    - BRUTE FORCE
    - Let us try match aa, a*
    - We have TWO choices, don't apply * on a or 
    apply * on a once
    - "" or "a*", since ""!="aa" this branch ends
    - We have "a*", do we want to not apply * on a 
    or apply * on a once
    - "a" or "aa*", since "a" != "aa" this branch 
    ends
    - We have "aa*", since "aa" == "aa" this branch 
    returns TRUE!
    - Let us try match s=aab, p=c*a*b
    - Let i point at index 0 in s, j point at index 0 
    in p
    - Let strGen="" be the string that we are 
    generating
    - We see '*' at j=1
    - We have two choices, apply * at j=0 or don't
    -> strGen="c" OR strGen=""
    - In the first choice, strGen[-1]!=s[i], so that 
    branch FAILS
    - In the second choice, strGen is empty, so that 
    branch can continue
    - i=0,j=2
    -> (i,j+2)
    -> Since we did NOT match at i=0, leave it
    -> Since we choose NOT to apply *, we shift j by 2
    - We see '*' at j=3
    - We have two choices, apply * at j=2 or don't
    -> strGen="a" OR strGen=""
    - Either could branch further, but not applying * 
    fails, so let's focus on the branch for applying *
    - i=1, j=2
    -> (i+1,j)
    -> Since we match at i=0, shift up to the next 
    letter
    -> Since we CHOOSE to apply * on j=2, we can do so 
    again
    - We have two choices, apply * at j=2 or don't
    -> strGen="aa" OR strGen="a"
    - In the first choice, strGen[-1]==s[i], so continue 
    on THAT branch
    - In the second choice, strGen[-1]!=s[i], so that 
    branch FAILS
    - i=2, j=2
    -> (i+1,j)
    -> Since we match at i=0, shift up to the next 
    letter
    -> Since we CHOOSE to apply * on j=2, we can do so 
    again
    - We have two choices, apply * at j=2 or don't
    -> strGen="aaa" or strGen="aa"
    - In the first choice, strGen[-1]=s[i], so that branch 
    FAILS
    - In the second choice, strGen[-1]=s[i], so that branch 
    can continue
    - i=2,j=4
    -> (i,j+2)
    -> Since we do NOT match at i, leave it
    -> Since we choose NOT to apply *, shift j twice
    - We have one choice, apply b
    - strGen = "aab"
    - strGen[-1]=s[i]
    - Continue on this branch
    - i=3, j=5
    -> Since we do match at i, shift it
    -> Since we choose to apply b, shift j once
    - i AND j are out of bounds, we have found a match!
    
    - Edge cases
    - What if j goes out of bounds but i is not?
    - This means that we have ran out of selections to generate 
    the remaining letters in s, so we must return FALSE
    - What if i goes out of bounds but j is not?
    - This means that we could possibly make 0 selections to 
    generate no new letters
    -> Consider this: we could be in a situation where we have a 
    '*' at j+1, meaning we can select 0 times. Then again at j+3, 
    and so on
    
    
    - O(2^n) time <- two choices at every character

    
    - CACHING
    - O(n * m) <- using a cache
    -> n = size of s
    -> m = size of p
    - We want to know whether we evaluate true or 
    false given that the pointers are at i and j
    - Therefore whenever we return, we store what 
    we get in the cache at whatever i and j is
    - It is literally an extra 3 lines of code but 
    it is so much more efficient
    -> Top 10th percentile to top 80th percentile

    '''

    def isMatchBRUTEFORCE(self, s: str, p: str) -> bool:


        def dfs(i, j):
            # i: index in s
            # j: index in p

            # BASE CASES

            if i >= len(s) and j >= len(p):
                # We have matched all letters!
                return True
            if j >= len(p):
                # We cannot generate any more letters 
                # to produce s
                return False
            
            # INDUCTIVE STEP
            
            # We can only check the letter at p[j] against 
            # s[i] if i is a valid index
            # We have a match if i and j point to the same 
            # letters
            # If j points to a '.' then we can force a match 
            # at index j
            match = i<len(s) and (s[i]==p[j] or p[j]=='.')

            if j+1 < len(s) and p[j+1] == "*":
                # Given j+1 is a valid index, we peek to see 
                # a '*'

                # We can choose to NOT use the '*'
                # So we leave i where it is, and explore this 
                # branch hoping that j+2 matches it
                return (dfs(i,j+2) or
                # We can choose to use the '*'
                # We can only generate p[j] if it matches s[i], 
                # so we check that before exploring this branch
                (match and dfs(i+1,j)))
            
                # If either is true then we return true
            if match:
                # There is no star and we can match at i,j
                return dfs(i+1,j+1)

            # The characters did not match, so this branch fails!
            return False
        
        return dfs(0,0)
    
    def isMatchMEMOIZATION(self, s: str, p: str) -> bool:

        # TOP-down Memoization

        # We create a cache
        cache = {}

        def dfs(i, j):
            # i: index in s
            # j: index in p
            
            if (i,j) in cache:
                # Literally all we do is refer to the 
                # cache if we have evaluated at indices 
                # i and j
                return cache[(i,j)]

            # BASE CASES

            if i >= len(s) and j >= len(p):
                # We have matched all letters!
                return True
            if j >= len(p):
                # We cannot generate any more letters 
                # to produce s
                return False
            
            # INDUCTIVE STEP
            
            # We can only check the letter at p[j] against 
            # s[i] if i is a valid index
            # We have a match if i and j point to the same 
            # letters
            # If j points to a '.' then we can force a match 
            # at index j
            match = i<len(s) and (s[i]==p[j] or p[j]=='.')

            if j+1 < len(s) and p[j+1] == "*":
                # Given j+1 is a valid index, we peek to see 
                # a '*'

                # We can choose to NOT use the '*'
                # So we leave i where it is, and explore this 
                # branch hoping that j+2 matches it
                cache[(i,j)] = (dfs(i,j+2) or
                # We can choose to use the '*'
                # We can only generate p[j] if it matches s[i], 
                # so we check that before exploring this branch
                (match and dfs(i+1,j)))

                return cache[(i,j)]
                # If either is true then we return true
            if match:
                # There is no star and we can match at i,j
                cache[(i,j)] =  dfs(i+1,j+1)
                return cache[(i,j)]
            # The characters did not match, so this branch fails!
            cache[(i,j)] = False
            return cache[(i,j)]
        
        return dfs(0,0)

if __name__ == "__main__":
    sol = Solution()
    s = "aa"
    p = ".b"
    print(sol.isMatchBRUTEFORCE(s,p)) # False
    print(sol.isMatchMEMOIZATION(s,p)) # False
    s = "nnn"
    p = "n*"
    print(sol.isMatchBRUTEFORCE(s,p)) # True
    print(sol.isMatchMEMOIZATION(s,p)) # False
    s = "xyz"
    p = ".*z"
    print(sol.isMatchBRUTEFORCE(s,p)) # True
    print(sol.isMatchMEMOIZATION(s,p)) # False
    