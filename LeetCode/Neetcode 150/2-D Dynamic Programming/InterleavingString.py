class Solution:

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
    
    - That is one complicated explanation...
    - Basically, can we take s1 and s2, split them into substrings 
    with RELATIVE ORDER MAINTAINED and add them together and form 
    s3 <- what Neet said
    
    - BRUTE FORCE
    - Consider s1 = "aabcc", s2="dbbca", s3="aadbbcbcac"
    - We set i1, i2, i3 as pointers initialise to 0 for s1, 
    s2, s3
    - We consider the first character needed to form s3
    - We need an a
    - Select s1[0]
    - Subproblem: use s1[1:] and s2 to form s3[1:]
    - i1=1,i2=0,i3=0
    - IMPORTANT NOTES ON POINTERS
    -> i1,i2 <- the positions in s1,s2 that we are CONSIDERING
    -> i3 <- the position in s3 that we are FILLING
    - Notice that i1+i2=i3 by nature, so we can set i3=i1+i2
    - If we carry on, we can reach i1=2,i2=1,i3=3
    - Now we want i3=4, i.e. aadb->b<-cbcac
    - We have two options
    -> We can shift i1 to 3 for s1 = aa->b<-cc
    -> We can shift i2 to 2 for s2 = d->b<-bca
    - At worse we could have these two options each time
    - O(2^n)

    - MEMOISATION
    - There are multiple ways that we could reach s1=i and s2=j
    -> Consider selecting 1 character from both, then 2 from both
    -> Consider selecting 2 characters from both, then 1 from both 
    - We reach O(nm) by caching
    -> n <- number of ways to set s1
    -> m <- number of ways to set s2

    - WHAT EXACTLY WILL WE CACHE
    - From (s1,s2) can we form s3
    - (s1,s2)->can_form_s3Sub
    -> can_form_s3Sub means can we form the unfilled portion of s3 
    using the unused characters from s1 and s2?

    - DYNAMIC PROGRAMMING
    - If s1 and s2 reach out of bounds, we have built the strings 
    - BASE CASE
    - Therefore we store the base case can_form_s3Sub at out of bounds
    - We specifically want to find out when can_form_s3Sub is true
    - (len(s1),len(s2))-> TRUE
    -> We say that when the s1 and s2 pointers are one step 
    past the maximum index of s1 and s2
    -> Given that s1+s2=s3, our s3 pointer is also one step past 
    the maximum index of s3
    -> In plain language we are asking: with no characters from s1, 
    s2, can we select a character from either to build no 
    characters from s3?
    -> Clearly the answer is TRUE! 
    - INDUCTIVE STEP
    - Let's abstract this mapping to (i1,i2)->can_form_s3Sub
    - We start at the base case
    - Now we shift i3 onto the final index of s3
    - We are interested in what exactly happens when we shift i1 
    XOR i2
    - If we CAN shift i1 back AND s1[i1]==s3[i3]: (i1-1,i2)->TRUE
    - Else: (i1-i,i2)->FALSE
    - We ask ourselves the same for i2
    - If we CAN shift i2 back AND s2[i2]==s3[i3]: (i1,i2-1)->TRUE
    - Else: (i1,i2-1)-> FALSE
    - Now what? We could branch out... but let me cook something

    - DYNAMIC PROGRAMMING SPACE OPTIMISED
    - If you imagine this as a grid, the choice of shifting i1 or 
    i2 back is like moving left or up respectively
    -> i1,i2 on x-,y-axis
    -> (len(s1),len(s2)) at the bottom right
    - I encourage you to draw this out if this gets confusing...
    - Whether we shift i1 left or i2 up at an iteration, the hard 
    limit where we cannot do this is where i1 goes to -1 or i2 goes 
    to -1
    -> ix=-1 is to shift farther behind the first index in sx
    - Given this constraint, let's try solely focus on i1 for now
    - We shift i1 left from len(s1) to 0, which we can do given our 
    understanding so far
    - Once we reach (0,len(s2)) we have filled all values i2=len(s2)
    - We can repeat this step again, but now starting at 
    (len(s1),len(s2)-1)
    - But how do we calculate what (len(s1),len(s2)-1) maps to?
    - We go right back to (len(s1),len(s2)) on the bottom right, but 
    instead of shifting i1 leftwards, WE SHIFT I2 UPWARDS
    - Thus we can fill in the second-to-last row
    - Now take a step back and realise the following
    -> To compute row i2 you need row i2+1
    -> To compute row len(s2) you need (len(s1),len(s2))
    -> You start with (len(s1),len(s2))=True  
    -> You want to return (0,0)
    - With all of this in mind, it make complete sense to only store 
    row i2 and i2+1
    '''

    def isInterleaveDYNAMICPROGRAMMING(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            # It is impossible to interleave these strings
            return False
        
        # Initialise dp to false for everything possible (i,j) position
        dp = [ [False] * (len(s2)+1) for i in range(len(s1)+1)]
        
        # Set base case
        dp[len(s1)][len(s2)] = True

        # The rest of the code is actually very similar to the 
        # memoisation code
        # We just make a few adjustments

        # Loop up row-by-row a la the matrix
        for i in range(len(s1),-1,-1):
            # Loop to the left column-by-column a la the matrix
            for j in range(len(s2),-1,-1):
                
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    # Ensure that i is in bounds
                    # Ensure that the character in s1 matches that in 
                    # s3
                    # Ensure that at we have verified that 
                    # (s1[i+1],s2[j])->s3[i+1+j]

                    # Update dp
                    dp[i][j] = True
                
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    # Ensure that j is in bounds
                    # Ensure that the character in s2 matches that in 
                    # s3
                    # Ensure that at we have verified that 
                    # (s1[i],s2[j+1])->s3[i+j+1]

                    # Update dp
                    dp[i][j] = True

                # Neither of the IF conditions passed
                # So s1[i],s2[j]-/->s3[i+j]
                # We don't need to do this because dp by default is 
                # false
                
        return dp[0][0]

    def isInterleaveMEMOIZATION(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1)+len(s2)!=len(s3):
            return False

        # Cache as a hash map
        dp = {}

        def dfs(i,j):
            # k = i+j
            if i == len(s1) and j == len(s2):
                # We have considered all characters in s1 and s2 and 
                # correctly saw that they could match characters in 
                # s3 as described
                # If we reach this state return True
                return True

            if (i,j) in dp:
                # We have already seen whether we could interleave 
                # the characters AFTER s1[i],s2[j] to form the 
                # characters AFTER s3[k]  
                # So we return whatever is stored in dp for this case
                return dp[(i,j)]
            
            if i < len(s1) and s1[i] == s3[i+j] and dfs(i+1,j):
                # First we check that we are considering a valid index 
                # in s1

                # Next we consider whether the character s1[i], which 
                # we are CONSIDERING, is equal to s3[i+j], which we 
                # intend to FILL

                # Given the two prerequisites above we finally ask 
                # ourselves: okay, if we shift i up, can we select 
                # the remaining characters in s1 and s2 to form the 
                # remainder of s3

                # If all the prerequisites above hold, then we know 
                # that from (i,j) in s1,s2 we CAN form s3 from k 
                return True
            if j < len(s2) and s2[j] == s3[i+j] and dfs(i,j+1):
                # This is literally the same as above, but instead 
                # we just check whether we can do so by shifting j
                
                return True
            
            # You may wonder why we return immediately in the IF 
            # conditions
            # Consider what exactly we are checking for dfs(i,j)
            # We are asking: can we form the remainder of s3 using 
            # s1,s2 from i,j?
            # We are NOT basing the answer on which pointer we shift!
            # Therefore, whether we can do so by shifting i to i+1 
            # or j to j+1 does not matter. So we return immediately
            


            # You may also wonder why we do not cache within the IF 
            # statement
            # Let's say (i,j)->True
            # If we go back to the base case, we take it for granted 
            # that (s1[M],s2[N])->s3[M+N] (M,N = len(s1),len(s2))
            # We never explicitly check this with our function, we 
            # return true if you look at the first IF statement
            # With this in mind, (i,j)->True <=> (s1[i],s2[j])->s3[i+j] 
            # Hence, when we evaluate True in THAT case we can treat it 
            # like a new base case 


            # Given that we have not returned, we cannot shift neither 
            # i nor j as desired
            dp[(i,j)] = False
            return False
        
        return dfs(0,0)


if __name__ == "__main__":
    sol = Solution()
    s1 = "aaaa"
    s2 = "bbbb"
    s3 = "aabbbbaa"
    print(sol.isInterleaveMEMOIZATION(s1,s2,s3)) # True
    print(sol.isInterleaveDYNAMICPROGRAMMING(s1,s2,s3)) # True
    s1 = ""
    s2 = ""
    s3 = ""
    print(sol.isInterleaveMEMOIZATION(s1,s2,s3)) # True
    print(sol.isInterleaveDYNAMICPROGRAMMING(s1,s2,s3)) # True
    s1 = "abc"
    s2 = "xyz"
    s3 = "abxzcy"
    print(sol.isInterleaveMEMOIZATION(s1,s2,s3)) # False
    print(sol.isInterleaveDYNAMICPROGRAMMING(s1,s2,s3)) # False
