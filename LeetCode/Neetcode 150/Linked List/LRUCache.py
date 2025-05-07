class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    # We aim for constant time operations
    # Get: Use a hash map for O(1) time
    # Put: Update the map, if map exceeds capacity
    # remove the LEAST RECENTLY USED key!
    # 
    # Left points to the least recently used key
    # Right points to the most recently used key
    # We need a *double* linked list so that 
    # we can quicky put a node at the least or most
    # recently used position
    # 
    # Our node is a bit different!
    # Each node has a key, value pair
    # Since the linked list is double linked, 
    # we store the previous and next
    # 
    # This makes our get and put operations easier!
    #
    # 
    # Also our cache maps keys to NODES. It is only 
    # used to check for its presence, really...

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # maps key to node
        
        self.left, self.right = Node(0,0), Node(0,0)
        
        # Left=LRU, right = most recent
        # The left and right must point to each other
        self.left.next = self.right
        self.right.prev = self.left

    # Some helper functions to add and remove!

    # Remove node from the list (totally)
    def remove(self, node):
        # Conceptually, the previous node must 
        # now point its next to the next of this node

        # And the next node must now point its 
        # previous to the previous of this node

        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    # Insert at right
    def insert(self, node):
        # Conceptually, we want the previous of the 
        # right to point its next to the node
        # And we want the right to point its previous
        # to the node
        # Finally, the node must point its next to 
        # the right, and its previous to the 
        # previous of right

        prev, nxt = self.right.prev, self.right

        prev.next, nxt.prev = node, node

        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        
        # We just see if the key is in the map
        if key in self.cache:
            
            # We remove the node from the list initially
            self.remove(self.cache[key])

            # And we insert the node at the right
            self.insert(self.cache[key])

            # Remember, self.cache[key] gets a NODE
            return self.cache[key].val
        return -1
    
    def put(self, key: int, value: int) -> None:
        # We see if it is in the cache
        if key in self.cache:
            # We remove from the linked list
            self.remove(self.cache[key])
        # Add this node to the list
        self.cache[key] = Node(key, value)
        # We insert to the list
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # If our cache exceeds the capacity, we 
            # must remove the LRU

            # lru is pointed to by the left pointer
            lru = self.left.next
            # Delete from linked list
            self.remove(lru)
            # Delete from the cache
            del self.cache[lru.key]



if __name__ == "__main__":
    lRUCache = LRUCache(2)
    print(lRUCache.put(1, 10)) # cache: {1=10}
    print(lRUCache.get(1)) # 10
    print(lRUCache.put(2,20)) # cache: {1=10, 2=20}
    print(lRUCache.put(3,30)) # cache = {2=20, 3=30}
    print(lRUCache.get(2)) # 20
    print(lRUCache.get(1)) # -1 (not found)