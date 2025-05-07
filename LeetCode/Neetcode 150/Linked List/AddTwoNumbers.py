class Node:

    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:

    def add(self, l1: Node, l2: Node)->Node:
        # At an elementary level, you add the digits. 
        # If the sum is greater than 10, you carry over
        # 1 
        # 
        # To find the result we set it to the value of the 
        # nodes at l1 and l2. 
        # We can find the result by module 10
        # We can find the carry by floor dividing by 10
        #  
        # We go until BOTH lists are exhausted. 
        # Just set l1 or l2 value to 0 if they don't exist
        # Now there is an edge case: what if we add the 
        # two final elements and end up with a carry?
        # Currrently, we would just miss it
        # To deal with this edge case, we have an 
        # additional consideration: loop until carry 
        # is zero
        # 

        # Create a dummy node to make it easy for adding
        dummy = Node()
        # Set cur equal to dummy
        cur = dummy

        # Set carry to zero
        carry = 0

        # We loop over heads both lists until one is exhausted
        # If either is None, default to zero
        # Note that the edge case of carry after adding the final
        # nodes means that we must insert that final carry!
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # New digit to consider!
            val = v1 + v2 + carry
            # Calculate the carry and val
            # carry is just the remainder, so we can floor divide
            # by 10
            carry = val // 10
            # val is the unit. I.e., the remainder after dividing
            # by 10. We use mod to get it
            val = val%10

            
            # We insert a new list node with this value
            cur.next = Node(val)

            # Set cur to next pointer
            cur = cur.next

            # Finally, we update the pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        node = dummy.next
        while node:
            print(node.val)
            node = node.next

        return dummy.next
            


if __name__ == "__main__":
    sol = Solution()
    # l1 = [1,2,3]
    l1 = Node()
    l1 = Node(3, l1)
    l1 = Node(2, l1)
    l1 = Node(1, l1)

    # l2 = [4,5,6]
    l2 = Node()
    l2 = Node(6, l2)
    l2 = Node(5, l2)
    l2 = Node(4, l2)

    print(sol.add(l1,l2)) # [5,7,9]

    # l1 = [9]
    l1 = Node()
    l1 = Node(9, l1)

    # l2 = [9]
    l2 = Node()
    l2 = Node(9, l2)

    print(sol.add(l1,l2)) # [8,1]