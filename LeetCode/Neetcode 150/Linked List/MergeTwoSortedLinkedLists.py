class ListNode:

    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class Solution:

    def mergeTwoLists(self, list1: ListNode, list2 = ListNode)->ListNode:
        # We begin by exhausting either list by updating the pointer 
        # of the node with the smaller value
        # 
        # After this, we can just set the next pointer of the node 
        # to be the not None list (if such a list exists) 

        # We save the original head of the node
        dummy = node = ListNode()

        # Exhaust either list
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                # Move list 1 head along
                list1 = list1.next
            else:
                node.next = list2
                # Move list 2 head along
                list2 = list2.next

            # Move node up
            node = node.next

        # Update node pointer
        node.next = list1 or list2

        # Dummy now points to the head
        return dummy.next

if __name__ == "__main__":
    sol = Solution()
    #list1 = [1,2,4]
    #list2 = [1,3,5]
    list1 = None
    list1 = ListNode(4, list1)
    list1 = ListNode(2, list1)
    list1 = ListNode(1, list1)
    list2 = None
    list2 = ListNode(5, list2)
    list2 = ListNode(3, list2)
    list2 = ListNode(1, list2)
    print(sol.mergeTwoLists(list1,list2)) # [1,1,2,3,4,5]

    #list1 = []
    #list2 = [1,2]
    list1 = None
    list2 = None
    list2 = ListNode(2, list2)
    list2 = ListNode(1, list2)
    print(sol.mergeTwoLists(list1, list2)) # [1,2]

    #list1 = []
    #list2 = []
    list1 = None
    list2 = None
    print(sol.mergeTwoLists(list1, list2)) # []