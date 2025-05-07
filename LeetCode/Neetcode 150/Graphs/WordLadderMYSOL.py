from typing import List

class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        - We are given two words, beginWord and endWord
        - You can transform beginWord to any word on word list, provided
        exactly ONE (1) position has a different word
        - We want the MINIMUM number of transformations to reach the word

        - We want to find the shortest possible path from beginWord to 
        endWord
        - To abstract the idea of connecting two words, we can use a graph
        - I don't know how exactly to implement this, so let's say that 
        we can do this

        - With the graph we start at beginWord
        - We call DFS on beginWord
        - DFS gives us the minimum positive distance travelled from node 
        n to endWord, 0 if it is impossible to reach endWord
        - We return DFS(beginWord)

        - Okay I have the idea for DFS, now how do we transform this 
        into a graph?
        - In an inexpensive way...
        - We could store the graph as an adjList in a hash map
        - We could use a function CreateEdge(n1,n2)
        - Within CreateEdge you update adjList for BOTH entries n1 and 
        n2
        - To avoid duplicate edges... you automatically skip any VISITED 
        nodes in subsequent loops across wordList
        - Here is what I mean...
        - INITIALISE VISITED AS SET
        - LOOP word1 over wordList
        - > LOOP word2 over wordList
        - >> IF word2 NOT IN VISITED AND Transformation(word1,word2)
        - >>> CreateEdge(word1,word2)
        - >> VISITED.add(word2)
        - 
        - Now we just need a Transformation function
        - Transformation(word1,word2):
        - COUNT = 0
        - FOR i in LENGTH OF word1:
        - > IF word1[i] == word2[i]: COUNT+1
        - IF COUNT == 1: RETURN TRUE
        - RETURN FALSE
        - 
        - Yes, that would work completely! I wish I had more than 2 mins
        to implement it though
        - Good abstract thinking though Edwin!
        '''
        


        pass



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