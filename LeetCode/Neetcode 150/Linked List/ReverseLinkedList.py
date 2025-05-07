from typing import List


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        # We specifically re-orient the pointers

        # We will store the previous and current node
        prev, curr = None, head

        while curr:
            # We save whatever the next of the current 
            # node is
            temp = curr.next

            # We set the next of the current node to the 
            # previous node
            curr.next = prev

            # We move the previous and current node 
            # up to the original next nodes
            prev = curr
            curr = temp
        return prev

        pass


if __name__ == "__main__":
    sol = Solution()

    # Generate list node
    #head = [0,1,2,3]
    head = ListNode(3, None)
    head = ListNode(2, head)
    head = ListNode(1, head)
    head = ListNode(0, head)
    print(sol.reverseList(head)) # [3,2,1,0]
    # head = []
    head = ListNode(None, None)
    print(sol.reverseList(head)) # []