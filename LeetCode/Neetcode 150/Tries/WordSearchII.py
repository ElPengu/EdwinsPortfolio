from typing import List

class TrieNode:

    def __init__(self):
        # Map children characters to nodes
        self.children = {}

        # Mark whether this is the final character for a word
        self.isWord = False

    # Helper function to add words
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True



class Solution:
    # O(mn) <- We can run DFS from each position from each position
    # O(4^mn) <- Each word can go in four directions across the
    # mxn board
    # O(mn*4^mn)
    # Interestingly, we do NOT store the board itself in a Trie
    # Rather, we store the words THEMSELVES in a Trie. 
    # >I.e. a prefix tree!
    # We use a helper function to add words to the prefix tree
    # Now imagine this, when we search the board we can IMMEDIATELY
    # tell if we are on a path to find a valid word.
    # > If no word starts with the first character at a certain 
    # position on the board, then we immediately know that the 
    # word is INVALID
    # > On the other hand, if we keep on finding successive characters 
    # that corresponding to successive children nodes and reach the
    # end of a word, we know that this word is on the board
    # To search the board we must start from every position
    # With this in mind we must supply the following arguments
    # > row, column <- self-explanatory
    # > node <- So that we know where in the prefix tree we are searching
    # from
    # > word <- So that if we reach the end of the word we have the word
    # immediately available
    # Searching the board lends itself to backtracking, since we have four
    # choices each time
    # > left, right, up, down
    # In the backtracking function we IMMEDIATELY return if any of these
    # are true
    # > Are we out of bounds
    # > Have we SEEN this position before <- use a global visit set
    # > Is this character not a child of the current node
    # Otherwise we add this coordinate to our visit set
    # We move to the child node
    # We update the word by appending the character at the board position
    # We add the word to a global res set if we are at the end
    # We call dfs on left, up, down, right with the updated arguments
    # After the DFS calls we naturally remove the coordinate from the  
    # visit set

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # We create a root Trie node
        root = TrieNode()

        # Add every node to our Trie
        for w in words:
            root.addWord(w)

        # Find the rows and columns
        ROWS, COLS = len(board), len(board[0])
        # We maintain a result set of words to avoid duplicates
        # We also don't want to repeat characters so we maintain
        # # a visit set
        res, visit = set(), set()

        # Backtracking solution to search the board
        def dfs(r,c,node,word):
            # Row and column to know where we are at
            # Node we are at in our Trie of words so that we 
            # know the children!
            # What the word is so far, in case we finish
        
            # Base case 1: Out of bounds
            # Base case 2: coordinate has been visited
            # Base case 3: The character is NOT even a child 
            # of the current node
            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS or 
                board[r][c] not in node.children or 
                (r,c) in visit):
                # Must exit call!
                return
            
            # We are now visiting this coordinate
            visit.add((r,c))
            # Since we always start at the root node, we now
            # move to the child node corresponding to this 
            # coordinate
            node = node.children[board[r][c]]
            # We start with an empty string, so we add the character
            # found at the child node above
            word += board[r][c]
            # We check if this newly-found is an end of a word
            if node.isWord:
                # Add the string word to our result set
                # Only if it is a word that we were looking for
                res.add(word)
            
            # Now we call dfs and move to the children
            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)

            # We finished visiting this node
            visit.remove((r,c))
        

        # We call dfs from each coordinate
        for r in range(ROWS):
            for c in range(COLS):
                # We always start at the root and with an empty string
                dfs(r,c,root,"")

        # We must return our result in list format
        return list(res)



if __name__ == "__main__":
    sol = Solution()
    board = [
    ["a","b","c","d"],
    ["s","a","a","t"],
    ["a","c","k","e"],
    ["a","c","d","n"]
    ]
    words = ["bat","cat","back","backend","stack"]
    print(sol.findWords(board, words)) # ["cat","back","backend"]

    board = [
    ["x","o"],
    ["x","o"]
    ]
    words = ["xoxo"]
    print(sol.findWords(board, words)) # []



