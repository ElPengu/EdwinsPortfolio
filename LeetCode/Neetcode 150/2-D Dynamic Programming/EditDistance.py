class Solution:

    def minDistance(self, word1: str, word2: str) -> int:

        '''
        - We have strings word1 and word2
        - Lowercase English letters
        - You may perform three operations as many times as you want
        - Insert a character at any position in word1
        - Delete a character at any position in word1
        - Replace a character at any position in word1
        - Find minimum number of operations to make word1 equal word2

        - Let us look at some simple cases
        -> word1, word2 = "","" -> 0
        -> Above implies base case: if both empty, return 0
        -> word1,word2 = "abc", "abc"
        ->> a==a, b==b, c==c -> 0
        -> Above implies base case: if both are identical, return 0
        -> word1,word2 = "abc", "" -> 3 <- Delete at every index
        -> word1,word2 = "", "abc" -> 3 <- Insert at every index
        -> Above implies base case: either is empty, return 
        max(len(word1),len(word1))
        
        - DYNAMIC PROGRAMMING
        - i is a pointer for word1, j is a pointer for j
        - w1, w2 = "abc", "acd"
        - i,j = 0,0
        - w1[i]==w2[j] -> i=i+1,j=j+1
        - IMPLIES: IF w1[i]==w2[j]: (i+1,j+1)
        - i,j=1,1
        - w1[i]!=w2[j] (<-'b'!='c')
        - Let us try all three operations then
        - INSERT
        - We insert 'c' at w1[i], and push all character after in w1 up
        - The result would be that w1[i]==w2[j]
        - We represent this by incrementing j, since we have matched it
        - We don't actually insert 'c' though, so we must leave i 
        the same
        - Hence: INSERT->operations+=1;(i,j+1)
        - DELETE
        - We delete 'b' at w1[i]
        - We hope that the next character does match
        - We represent this by incrementing i, hoping that it matches j
        - Hence: DELETE->operations+=1;(i+1,j)
        - REPLACE
        - We set w1[i] to have value 'c'
        - Well, they match now
        - We represent this by incrementing BOTH i,j
        - Hence: REPLACE->operations+=1;(i+1,j+1)
        
        - Carrying on the example, it happens to be ideal to REPLACE at 
        i,j=1,1
        - REPLACE at i,j=1,1
        - i,j=2,2, ops = 1 (<-0+1)
        - w1[i]==w2[j] -> i=3,j=3
        - i=len(word1) AND j = len(word2): RETURN ops

        - DYNAMIC PROGRAMMING BOTTOM UP
        - We see that it is easier to work from the base case instead 
        of branching to it
        - Imagine a grid
        - w2 on x-axis, w1 on y-axis
        - LET N,M = len(word1), len(word2)
        - (0,0) is on top-left
        - (M,N) is on bottom-right
        - We saw that the base case is at (N,M)
        - Hence: (N,M)->0 (<- 0 operations to match empty strings)
        - We also know the nature when row=N OR column = M
        - IF row==N: (N,j) -> len(w2[j:])
        - IF column==M: (i,M) -> len(w1[i:])
        - If you look at how you evaluate (i,j), you will check either 
        diagonally (i+1,j+1), vertically (i+1,j) or horizontally 
        (i,j+1)
        - The only position where this is the case is at (M-1,N-1)
        -> We have ((M-1)+1,(N-1)+1), ((M-1)+1,N-1), and (M-1, (N-1)+1) 
        - Let's say we evaluate (M-1,N-1), what now?
        - Now you could evaluate (M-2,N-1) (shift left) or evaluate 
        (M-1,N-2) (shift up) since we have filled in coordinates in the 
        matrix where row==N or column==M
        - We arbitrarily choose to always shift left until we hit 
        column == 0, then we repeat this for (M-1, N-2)  
        '''

        # Create 2D array as a cache
        # A list of float infinite for every character in
        # word2 + 1, and one of these for every element +1 in word1
        # We initialise to infinity because we minimise for each position
        cache = [[float("inf")] * (len(word2)+1) for i in range(len(word1)+1)]

        for j in range(len(word2)+1):
            # We fill up the bottom row, i.e., where the y-axis, 
            # which is for indices in word1, is at maximum which is 
            # length of word1
            # This is basically matching empty string to word2, so we 
            # are asking how many INSERTIONS do we need from word2 to 
            # we need to match word2
            cache[len(word1)][j] = len(word2)-j
    
        for i in range(len(word1)+1):
            # We fill up the right-most column, i.e., where the 
            # x-axis, which is for indices in word2, is at maximum 
            # which is length of word2
            # This is basically matching word1 to empty string, so we 
            # are asking how many DELETIONS do we need from word1 to 
            # match empty string
            cache[i][len(word2)] = len(word1)-i

        # DYNAMIC PROGRAMMING PORTION

        for i in range(len(word1)-1,-1,-1):
            # len(word1)-1,...,0

            for j in range(len(word2)-1,-1,-1):
                #len(word2)-1,...,0
        
                if word1[i] == word2[j]:
                    # Easy, just use the cache as we need no more 
                    # operations
                    cache[i][j] = cache[i+1][j+1]
                else:
                    # We ask ourselves what is the most efficient 
                    # way out of DELETE, INSERT, and REPLACE in that 
                    # order
                    # This is an operation so we add 1
                    cache[i][j] = 1 + min(
                        cache[i+1][j],
                        cache[i][j+1],
                        cache[i+1][j+1]
                    )
        
        # The solution is at (0,0)
        return cache[0][0]


if __name__ == "__main__":
    sol = Solution()
    word1 = "monkeys"
    word2 = "money"
    print(sol.minDistance(word1,word2)) # 2
    word1 = "neatcdee"
    word2 = "neetcode"
    print(sol.minDistance(word1,word2)) # 3