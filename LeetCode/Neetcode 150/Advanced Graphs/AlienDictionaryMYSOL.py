from typing import List

class Solution:

    def answer(words: List[str]) -> str:
        '''
        - A foreign language uses the latin alphabet
        - The order of letters is NOT "a","b",...,"y","z"
        - We receivea non-empty strings words from the dictionary
        - The words are sorted lexographically based on the rules 
        of this new language!
        - Derive AN ordering of letters in this language
        - If the order is invalid, return an empty string
        - a is smaller than b if
        -> OPTION 1: Up to index i all letters are the same, and 
        a[i] is lexographically smaller than b[i]
        - OPTION 2: All letters up to last index of a are identical

        - Okay this is interesting
        - We are saying that we have a SET LETTERS
        - Looking at the first letter of each word IN ORDER and popping
        that letter from our LETTERS those will be the first letters in
        the alphabet
        - Now it gets tricky
        - The same holds for the second letter IFF they have the same 
        first letter, but only within that group of letters will the 
        same property hold
        - There is also the issue of words differing in length

        - Let's start with the issue of tertiary letters
        - There will be multiple paths
        - If we think of this alike a physical dictionary, the order 
        between two letters is derived by whether the preceding letter
        (or lack thereof) is the same

        - We could generate a graph of the letters
        - Loop over every pair of words
        - For every index, if the preceding index (or lack thereof) is 
        identical AND there exist DISTINCT letters at this index then 
        we can say that a[i]->b[i]

        - Assume that this builds the graph
        - How do we search the graph?
        - We want to be able to travel from SOME letter to every other 
        letter along some path, otherwise the order cannot be derived
        - IN FACT, we want a MINIMUM SPANNING PATH that takes us FROM
        some letter PAST every letter used in ONE DIRECTION
        - All I can think of is performing BFS or DFS starting at EVERY 
         letter and BACKTRACKING if we repeat a letter or cannot travel
         but have an incomplete graph

         - This should work! 
         - Ah, it would only not work because I did not consider 
         word1[i] = " " XOR word2[i] = " "
        
        '''

        pass


if __name__ == "__main__":

    sol = Solution()
    words = ["z","o"]
    print(sol.answer(words)) # "zo"
    words = ["hrn","hrf","er","enn","rfnn"]
    print(sol.answer(words)) # "hernf"
