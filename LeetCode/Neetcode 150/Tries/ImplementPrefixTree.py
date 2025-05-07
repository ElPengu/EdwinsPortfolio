class TrieNode:

    def __init__(self):
        
        # A node has a set of UP TO 26 children
        # We store using a hash map
        self.children = {}
        # We have a marker for end of word
        self.endOfWord = False

        # Note that we do NOT store the character
        # It is implicit since we look at the children
        pass


class PrefixTree:

    # Trie works by starting from a base node
    # Attributes of a node
    # > children: A mapping of next character literal
    # to corresponding node
    # > endOfWord: Boolean telling us if this is the
    # end of a word
    # No need to store the literal character as an
    # attribute, it is implicitly found when you 
    # move from node to child node using the children
    # map
    # 
    # Everything else can be understood in terms
    # of linked lists

    def __init__(self):
        # Set a root node
        self.root = TrieNode()

    def insert(self, word: str)->None:
        # Start at the root
        cur = self.root

        # Iterate through every character in the word
        for c in word:
            if c not in cur.children:
                # If we cannot see this in our children 
                # hash map yet, we add it as a child!
                cur.children[c] = TrieNode()
            # Move to the child
            cur = cur.children[c]

        # Now we mark this node we are at as the end
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        # Start at the root
        cur = self.root
        
        # Loop over characters
        for c in word:
            if c not in cur.children:
                # The word is certainly NOT here
                return False
            # Move to the child
            cur = cur.children[c]

        # Are we at the end of word?
        return cur.endOfWord
        
    def startsWith(self, prefix: str) -> bool:
        # Start at the root
        cur = self.root

        # Loop over characters
        for c in prefix:
            if c not in cur.children:
                # The word is certainly NOT here
                return False
            # Move to the child
            cur = cur.children[c]

        # We don't care if we are at the end of the
        # word or not
        return True
        
        
if __name__ == "__main__":
    prefixTree = PrefixTree()
    print(prefixTree.insert("dog"))
    print(prefixTree.search("dog"))   # return true
    print(prefixTree.search("do"))    # return false
    print(prefixTree.startsWith("do")) # return true
    print(prefixTree.insert("do"))
    print(prefixTree.search("do"))     # return true