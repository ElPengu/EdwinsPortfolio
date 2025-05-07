from typing import List
from collections import defaultdict
from collections import deque

class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        - Not super difficult, there is only one annoying thins
        - We have a beginWord, endWord, and a sequence of words in 
        wordList
        - Every adjacent pair of words can only differ by a single letter
        - We want the **length** of the **shortest** sequence of words
        - Every word is same length
        - Using a 
        - A naive solution to creating the adjacency list would be a nested
        loop.
        - O(n2m) time for naive solution 
        -> n number of words 
        -> m characters for character checks
        - However this is too inefficient for LeetCode!
        - We'll get down to O(nm2), why do we care? The limit for 
        characters is smaller than words
        -> n number of words 
        -> m characters for character checks
        - ADJACENCY LIST
        - We take a word, let's say "hot"
        - Introduce wild card *
        - Possible transformations: *ot,h*t,*ot
        - We move to the next word, let's say that it is 'dot'
        - Possible transformations: *ot, d*t, ho*
        - We move to the next word, let's say that it is 'lot'
        - Possible transformations: *ot, l*t, lo*
        - Notice that only the first possible transformations are the 
        - same. This means that hot and dot could be connected.
        - How do we show this connection?
        - In the adjacency list we will store {pattern: [possible 
        transformations]}
        - So in this example: {*ot: [hot,dot,lot]}
        - This means that we will have patterns for every possible 
        - transformation
        - How do we get to O(nm2) though?
        - So we go through every word ONCE <- n
        - We go through every character that we remove <- m
        - For every character that we can remove we add the word to 
        the pattern list in adjList <- m
        - SEARCH FOR THE PATH
        - We do BFS
        - Let us abstract FINDNEIGHBOURS(word) for now
        - We apply FINDNEIGHBOURS and do BFS on the found neighbours
        of beginWord and return when we get to the first layer
        - 
        - We get O(nm) for this part. How, and why not O(n2m)?
        - n = words, m = characters
        - With an edge being a transformation, n2 assumes that every
        word COULD connect to at most n-1 other words
        - In this particular case a word n can only change at most 25 
        different times
        - So what?
        - With n=words, as n increases we have a *constant* limit 
        on how many edges we can introduce!
        - For m characters we will consider every possible character 
        in the word at most once when traversing
        '''
        
        # Base case
        if endWord not in wordList:
            return 0

        # We create a dictionary mapping patterns to words
        nei = defaultdict(list)
        # We do not have beginWord in wordList which is pretty stupid
        wordList.append(beginWord)
        # We build the adjacency list
        for word in wordList:
            # We find every possible pattern of this word!
            for j in range(len(word)):
                # word[:j] takes all letters up to and EXCLUDING that at
                # index j
                # "*" is the wildcard
                # word[j+1:] takes all letters from and INCLUDING that 
                # at index j+1 to the end of the word
                pattern = word[:j] + "*" + word[j+1:]
                
                # In our neighbour list we append the word to that 
                # pattern!
                nei[pattern].append(word)
        
        # Now we do our BFS
        # We create a set of visited nodes
        visit = set()
        # Add the beginning word as we will start here
        visit.add(beginWord)
        # We need a queue
        q = deque() #
        # Again the queue starts with beginWord
        q.append(beginWord)
        # We start with a length of 1, as beginWord is on the first 
        # layer
        res = 1
        
        while q:
            for i in range(len(q)):
                # Pop words at this layer

                # We get a word on this layer
                word = q.popleft()
                
                # We check if we are at the end word yet
                if word == endWord:
                    # We are at the end word!
                    # Return the layer that we are on
                    return res
                
                # We need to get the neighbours of this word!

                # Go through every character
                for j in range(len(word)):
                    # This is a pattern
                    pattern = word[:j] + "*" + word[j+1:]
                    # Iterate through the list of words in the 
                    # neighbour list
                    for neiWord in nei[pattern]:
                        # We have ONE check!
                        # CHECK: We are NOT at a word that we have 
                        # already seen on a previous layer
                        if neiWord not in visit:
                            # We are at a word on the next layer!
                            # Since we are VISITING this word 
                            # we add it to the VISIT set
                            visit.add(neiWord)
                            # We add this word to the queue
                            q.append(neiWord)
                        
                        

            # We move onto the next layer
            res += 1

        
        # No word found!
        return 0



if __name__ == "__main__":
    sol = Solution()
    beginWord = "cat"
    endWord = "sag"
    wordList = ["bat","bag","sag","dag","dot"]
    print(sol.ladderLength(beginWord, endWord, wordList)) # 4
    beginWord = "cat"
    endWord = "sag"
    wordList = ["bat","bag","sat","dag","dot"]
    print(sol.ladderLength(beginWord, endWord, wordList)) # 0