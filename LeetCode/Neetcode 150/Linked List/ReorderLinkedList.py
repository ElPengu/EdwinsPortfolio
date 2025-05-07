class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next


class Solution:

    def reorderList(self, head: ListNode)->None:
        # We want to alternate from picking nodes 
        # at the beginning and the end
        # We will do this without extra space which 
        # is a tiny bit more tricky
        # 
        # There will be two phases
        # Phase 1: Take the second half of the linked
        # list and reverse it
        # Phase 2: Merge the two halves of the list
        # 
        # We will use two pointers. A fast and a slow
        # pointer
        # Slow pointer: Starts at the first node, iterates
        # one at a time. 
        # Fast pointer: Starts at the second node, iterates
        # two at a time. 
        #
        # We stop when the fast pointer reaches the last 
        # value OR null. This will tell us that the slow
        # pointer has covered half the linked list (whether
        # odd or even). 
        # At this point we can say that slow.next is the 
        # beginning of the second-half of the linked list!
        # We save slow.next, and then we set slow.next to Null
        # So that the two halves are separated.
        #
        # The second-half will be bigger or the same, but 
        # in this case this is desirable. We will reverse it
        # EX1: [1,2,3,4] -> [1,2],[3,4] -> [1,4,2,3]
        # EX2: [1,2,3,4,5] -> [1,2,3],[4,5] -> [1,5,2,4,3]
        # 
        # We will now have a left and right pointer.
        # We will save leftNext and rightNext
        # We will set left to point to right, and right 
        # will point to leftNext
        # Finally, update left to leftNext, right to 
        # rightNext

        # Set slow and fast pointer
        slow, fast = head, head.next

        while fast and fast.next:
            # Shift slow by 1, fast by 2
            slow = slow.next
            fast = fast.next.next

        # We set a second node to the current start of the 
        # second half of the linked list
        second = slow.next
        # Now we can separate the lists
        slow.next = None
        # Let us set previous node to None
        prev = None

        # Now we can reverse the second half of the list
        while second:
            # This is basically just saving the "first" 
            # and "second" nodes, setting the "second" 
            # to point to the "first" node, and then 
            # updating "first" and "second" to be 
            # "second" and "third"
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # Now we merge the two halves of the lists
        first, second = head, prev # Remember second will be None

        # Since the second half is the bottleneck seeing 
        # as it could be the same length or smaller than 
        # the first half, we loop based on the second node
        while second:
            # Store the next nodes temporarily
            tmp1, tmp2 = first.next, second.next

            # Update pointers
            first.next = second
            second.next = tmp1

            # Update first and second
            first, second = tmp1, tmp2


if __name__ == "__main__":
    sol = Solution()
    # [2,4,6,8]
    head = None
    head = ListNode(8, head)
    head = ListNode(6, head)
    head = ListNode(4, head)
    head = ListNode(2, head)
    print(sol.reorderList(head)) # [2,8,4,6]

    # head = [2,4,6,8,10]
    head = None
    head = ListNode(10, head)
    head = ListNode(8, head)
    head = ListNode(6, head)
    head = ListNode(4, head)
    head = ListNode(2, head)
    print(sol.reorderList(head)) # [2,10,8,4,6]