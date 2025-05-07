class ListNode:

    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:

    def hasCycle(self, head: ListNode) -> bool:
        # We loop over the linked list
        # In the case that there is no loop, we will get to the 
        # tail. We can return false in this case
        # However if there is a loop, we will see the same 
        # node twice. So we keep a set of visitedNodes 
        # and if we read a node that is already in visitedNodes 
        # there are no more checks to make. Return false!

        # Create a set of seen nodes
        seen = set()

        # Set the current to be the head. We iterate over this node
        cur = head

        # Loop over the list
        while cur:
            if cur in seen:
            # If the head is ever in seen we have found a 
            # loop!
                return True

            # Add to seen
            seen.add(head)

            # Update cur
            cur = cur.next

        return False

if __name__ == "__main__":
    sol = Solution()
    # head = [1,2,3,4]
    # [1->2->3->4->2->...]
    head = None
    head = ListNode(4, head)
    headCycle = head
    head = ListNode(3, head)
    head = ListNode(2, head)
    headCycle.next = head
    head = ListNode(1, head)
    
    print(sol.hasCycle(head)) # true

    # head = [1,2]
    head = None
    head = ListNode(2, head)
    head = ListNode(1, head)
    print(sol.hasCycle(head)) # false