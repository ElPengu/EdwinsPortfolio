class ListNode:

    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int)-> ListNode:
        # Note that we must remove the nth node from 
        # the END of the list
        # 
        # We can use two pointers. A left and a right 
        # pointer. 
        # Left pointer: starts at first node
        # Right pointer: starts at an offset of n
        # 
        # When the right pointer is at None, we want to 
        # set the node that points to the left node to 
        # instead point to the next of the left node
        # 
        # So we need to ACTUALLY redefine the left pointer
        # Left pointer: starts at a dummy node that 
        # points at the first node
        
        # Set dummy node
        dummy = ListNode(0, head)
        # Set left and right pointer
        left = dummy
        right = head

        # Shift right by n spots from the head
        while n > 0 and right:
            right = right.next
            n -= 1

        # Shift both left and right until right is 
        # at the end of the list
        while right:
            left = left.next
            right = right.next

        # Update the next pointer of the left pointer
        left.next = left.next.next

        # Dummy points to the head
        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    #head = [1,2,3,4]
    head = None
    head = ListNode(4, head)
    head = ListNode(3, head)
    head = ListNode(2, head)
    head = ListNode(1, head)
    n = 2
    print(sol.removeNthFromEnd(head, n)) #[1,2,4]

    #head = [5]
    head = None
    head = ListNode(5, head)
    n = 1
    print(sol.removeNthFromEnd(head, n)) # []