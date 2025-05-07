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

        - Let pointer i be for word1, pointer j be for word2
        - Let N,M = size(word1),size(word2)
        - BASE CASE
        - (word1[N],word2[M])->0
        - What does this mean
        - Starting from the ends of word1 and word2, the empty string 
        word1 can become the empty string word2 in 0 operations
        - INDUCTIVE STEP
        - Let us say that we are still at the base case, what is the 
        next step?
        - We want to see the minimum number of operations at 
        word1[N-1] to form word1[N-1:] into word2[M-1:]
        - Specifically, we want to see what we need to do to match 
        word1[N-1] into word2[M-1]
        - IF word1[N-1]==word2[M-1], we move to N-2,M-2
        - But what if the ELSE condition is true
        - We can insert, delete, or replace a character
        - Why not try all three
        - So to begin with, we INSERT word2[M-1] AT word1[N-1], which can 
        be done with string splicing to get to O(1) time for this
        - After trying that, we DELETE at word1[N-1] and continue
        - Finally, we try to REPLACE at word1[N-1] and continue
        
        - Okay, we have SOMETHING. But what exactly do we do in the ELSE 
        condition
        - What is the STOP condition?  
        - Wait, the stop is okay, we insert the character we want, so 
        we'd do this at most for every character in word2
        - OHHHHHH
        - We go until pointer j finishes at 0, then we return 1 for 
        every operation done so far along the branch
        
        - Now we can start pruning branches
        - We'll store this in cache DP: (i,j)->number of operations
        - A base case is that we have already cached the number of 
        operations AND it is... somehow less than the minimum that 
        we'd find (let's abstract this for now)
        - In this case we just return whatever the cache says for (i,j)
        
        - I think that is literally it
        - Our solution would be the maximum found at j=0
        '''

        pass


if __name__ == "__main__":
    sol = Solution()
    word1 = "monkeys", word2 = "money"
    print(sol.minDistance(word1,word2)) # 2
    word1 = "neatcdee", word2 = "neetcode"
    print(sol.minDistance(word1,word2)) # 3