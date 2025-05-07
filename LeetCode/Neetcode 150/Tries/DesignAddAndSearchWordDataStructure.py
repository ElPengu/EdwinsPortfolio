class TrieNode:

    def __init__(self):

        # A trie node has two attributed
        # > children: Maps characters to 
        # nodes
        # > endOfWord: Self-explanatory 
        # boolean

        self.children = {}
        self.word = False
        

class WordDictionary:

    # This is a trie in the most literal sense
    # Start with a root node
    # Node attributes
    # > children: Maps following letter to its
    # node
    # > word: Boolean for the end of a word
    # 
    # Adding a word is trivial. 
    # Start at the root, iteratively move to child
    # node for the next character. Create that 
    # node if its does not exist
    # Mark the final character's node s.t. word 
    # is True
    # 
    # Searching for a word requires backtracking 
    # on '.', where you search all child nodes
    # Else you search the next character child 
    # node as usual
    # 
    
    def __init__(self):
        # Create a root trie node

        self.root = TrieNode()

    def addWord(self, word: str)->None:
        
        # Starting from the root, add 
        # characters in word
        # Mark end of the word!
        
        # Start at root
        cur = self.root

        # Iterate through word
        for c in word:
            if c not in cur.children:
                # We must create a node 
                # for this character!
                cur.children[c] = TrieNode()

            # Move to the next node
            cur = cur.children[c]

        # Set the node we have landed on as the
        # end of the word
        cur.word = True

    def search(self, word: str)->bool:
        # We must consider if we land on a 
        # . or not.
        # If we land on a branch then we want 
        # to choose between ALL children
        # This implies recursion!

        # We start at the node
        cur = self.root

        def dfs(j, root):
            # j is the index parameter

            cur = root

            for i in range(j, len(word)):
                # We loop over from j index til the 
                # end

                # Get the character at index i
                c = word[i]

                if c == ".":
                    # We use backtracking to check every
                    # possible child
                    for child in cur.children.values():
                        # Call dfs on the next child
                        # and the next index
                        if dfs(i+1, child):
                            return True
                    # We have not found any true if 
                    # we get here
                    return False
                    
                else:
                    # We have a regular character
                    if c not in cur.children:
                        # This word does NOT exist!
                        return False
                    # Move to that node
                    cur = cur.children[c]

            # If we are at the end of the word, 
            # this will be true. Else false
            return cur.word
        
        return dfs(0, self.root)


if __name__ == "__main__":
    wordDictionary = WordDictionary();
    print(wordDictionary.addWord("day"))
    print(wordDictionary.addWord("bay"))
    print(wordDictionary.addWord("may"))
    print(wordDictionary.search("say")) # return false
    print(wordDictionary.search("day")) # return true
    print(wordDictionary.search(".ay")) # return true
    print(wordDictionary.search("b..")) # return true