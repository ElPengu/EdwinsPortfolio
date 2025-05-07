class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        # Every node points to a next node and a random node
        # We want to copy every node so that the ith copy 
        # - has the value of the ith node
        # - has a next pointer corresponding to that of the ith 
        # node
        # - has a random pointer corresponding to that of the ith 
        # node
        # 
        # You may not point to any nodes of the original list
        # 
        # TWO PASSES
        # PASS 1: Create the nodes, also set a hash 
        # map to map the OLD NODE to the NEW COPY 
        # PASS 2: We use our hash map to set up the 
        # value, next pointer, and random pointer!

        # Creat the hash map to map the old to copy
        oldToCopy = {}

        # # CASE: if cur points to a None, 
        # we want our copied node to point to None
        # We explicitly add this mapping to the hash 
        # map 
        oldToCopy[None] = None

        # PASS 1 - set the value
        cur = head
        while cur:
            # Set old to cur
            old = cur
            # Create the node copy
            copy = Node(cur.val)
            # Set the old to map to copy
            oldToCopy[old] = copy
            cur = cur.next
        
        # PASS 2 - set the pointers
        cur = head
        while cur:
            # For ease of understanding, we set 
            # old to cur
            old = cur

            # Get the node
            copy = oldToCopy[old]
            
            # Set the pointers
            copy.next = oldToCopy[old.next]
            copy.random = oldToCopy[old.random]
            
            cur = cur.next

        # Return the head of the *deep copied* linked 
        # list
        return oldToCopy[head]


if __name__ == "__main__":

    sol = Solution()

    # head = [[3,null],[7,3],[4,0],[5,1]]
    node1 = Node(3)
    node2 = Node(7)
    node3 = Node(4)
    node4 = Node(5)
    node5 = None
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node1.random = node5
    node2.random = node4
    node3.random = node1
    node4.random = node2
    print(sol.copyRandomList(node1)) #[[3,null],[7,3],[4,0],[5,1]]


    # head = [[1,null],[2,2],[3,2]]
    node1 = Node(1)
    node3 = Node(2)
    node2 = Node(3)
    node1.next = node2
    node2.next = node3
    node3.next = None
    node1.random = None
    node2.random = node3
    node3.random = node3
    print(sol.copyRandomList(node1)) # [[1,null],[2,2],[3,2]]