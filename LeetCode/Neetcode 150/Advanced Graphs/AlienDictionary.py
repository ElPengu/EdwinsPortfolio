from typing import List

class Solution:

    def foreignDictionary(self, words: List[str]) -> str:
        '''
        - A foreign language uses the latin alphabet
        - The order of letters is NOT "a","b",...,"y","z"
        - We receive a non-empty strings words from the dictionary
        - The words are sorted lexographically based on the rules 
        of this new language!
        - Derive AN ordering of letters in this language
        - If the order is invalid, return an empty string
        - a is smaller than b if
        -> OPTION 1: Up to index i all letters are the same, and 
        a[i] is lexographically smaller than b[i]
        - OPTION 2: All letters up to last index of a are identical
        - Basically how a dictionary works :^)

        - Now this is a pretty HARD graph problem
        - We will need the algorithm Topological Sort

        - We can immediately see a base case where we return []
        - One case where we have an invalid ordering
        -> If we see something like [...,apes,...,ape,...] we 
        immediately know that the dictionary is wrong

        - PHASE 1: Building our graph
        - We begin by considering adjacent pairs of words, let's call 
        them word1 and word2
        - We look at every index of word1 and word2, and the MOMENT they
        are not the same, we can say that word1[i]->word2[i]
        - If we see something like word1[i]=" " but not word2[i] we don't
        gain any new infromation
        - If we see something like word2[i]=" " but not word1[i] then we
        have an invalid ordering, so we know that this dictionary is 
        wrong!

        - We could do a BFS or DFS solution
        - The issue with a BFS solution is that there is SO MUCH 
        bookkeeping (according to Neet), so we will use DFS to search the 
        graph

        - PHASE 2: Searching the graph
        - If we were to see a cycle? 
        - This means that we have something like x->y->x, and you can 
        see that this is an invalid ordering. 
        -> We could have ["xx","xy","xx"] which doesn't make sense
        - If we were to have two orderings which are separate?
        - This is the case of something like w->x and y->z
        - This is still valid! An ordering could by "wxyz" or "yzxw" or
        even stuff like "wyxz".
        -> Confused? Read the question. We want SOME valid ordering of
        letters. The letters could be organised like this and the 
        dicionary would still be readable. We only care about precedence
        
        - Another question is which way should we branch. What if we 
        have A->B->C and A->C. We could DFS from A to C getting "AC", 
        then down A to B to C which results in "ACABC" by the end
        - The work-around to this is **post-order DFS**
        -> We go down A->C
        -> We see that C has no children
        -> Only now do we add C to our list: "C"
        -> We bubble back up to A
        -> We go down A->B
        -> We go down B->C
        -> We see that C has no children and is already in our list
        -> We bubble back up to B
        -> B has no more branches to search
        -> Only now do we ADD B to our list: "CB"
        -> We bubble back up to A
        -> A has no more branches to search
        -> Only now do we ADD A to our list: "CBA"
        -> Return valid REVERSE ordering "ABC"

        - Finally what about loops?
        - We care about letters that we visit on the current path along 
        a DFS call
        - We will require a mapping of each character to two states
        - VISIT <- Once we visit a letter we add it to this with a value
        of FALSE
        - PATH <- Once we visit a letter on the path we add it to this 
        with a value of TRUE 
        - We use a hash map VISIT
        - When you start processing a character you add it to VISIT with 
        boolean TRUE to say that you have seen this character on the 
        path
        - After processing it you switch it to boolean FALSE to say that
        you have seen it, but it is no longer on the path. This helps 
        us because we do DFS on **every** node, but we don't do DFS 
        if we have already visited the node AT ALL

        - This makes a lot more sense in the code, if you are struggling
        to keep all of these cogs turning

        - O(n) where n is the number of characters
        '''

        # Set up the adjacency list - use set to avoid duplicates
        adj = {c:set() for w in words for c in w}

        for i in range(len(words)-1):
            # Select a pair of adjacent words
            w1,w2 = words[i],words[i+1]

            # We only care about the letters up to the end of the first
            # word
            minLen = min(len(w1),len(w2))

            # Base case: prefix is same but first word is LONGER, hence
            # invalid
            if len(w1) > len(w2) and w1[:minLen]==w2[:minLen]:
                return ""
            for j in range(minLen):
                # We check characters
                if w1[j] != w2[j]:
                    # Now we have differing letters for the first time!
                    adj[w1[j]].add(w2[j])
                    # There are no subsequent orderings to find after
                    # this state
                    break
        
        # Each character is mapped to two values
        # FALSE=visited, TRUE=visited and on current path
        # We can remove some redundancy
        # FALSE=visited, TRUE=current path
        visit = {}

        # We create a list to put characters in
        res = []

        def dfs(c):
            if c in visit:
                # If we have seen this letter and it is NOT IN our 
                # path we'll return FALSE
                # If we have seen this letter and it is IN our current
                # path we'll return TRUE

                # What this is saying is okay, we went once to this 
                # letter on this path. We'll add it to our visit.
                # But then if we come back and it IS in our path, we 
                # add it again which makes a cycle

                # Hence, we WANT this to be FALSE. 
                # If DFS returns true then we know that SOME letter 
                # caused a cycle
                return visit[c]
            
            # We now add the character to visit with TRUE since we 
            # found it on our path
            visit[c] = True

            for nei in adj[c]:
                # We go through every character that comes after c
                if dfs(nei):
                    # We have detected a cycle on the path going along
                    # this neighbour!
                    return True

            # Now we are exiting the path with this character
            # We might see it again on a different path! So we 
            # switch it OFF in our hash map in case we see it on a new
            # path (in which case the character would be allowed to be 
            # added)
            visit[c] = False

            # Only NOW do we add the character to our result
            # Remember, we are doing post-order traversal!
            res.append(c)

        # Let us call our DFS
        # It doesn't matter where in the graph we start because it is
        # post-order
        # AS LONG AS WE MARK VISITED CHARACTERS AS VISITED
        for c in adj:
            if dfs(c):
                # We cannot join the list as there is a cycle
                return False

        # Sort the list
        res.reverse()

        # We join and return the list
        return "".join(res)


if __name__ == "__main__":

    sol = Solution()
    words = ["z","o"]
    print(sol.foreignDictionary(words)) # "zo"
    words = ["hrn","hrf","er","enn","rfnn"]
    print(sol.foreignDictionary(words)) # "hernf"
