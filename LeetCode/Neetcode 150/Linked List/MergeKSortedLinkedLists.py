from typing import List

class Node:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Node]) -> Node:
        # The most efficient solution is to use merge sort!!
        # Take the solution for merging TWO linked lists
        # 
        # We begin by looping until there is only 1 linked list
        # In each loop, we create a mergedLists variable. We
        # merge two lists with a helper function and append 
        # each to the merged list. Once all lists have been considered,
        # we set lists to be merged lists
        # 
        # Merging two lists: O(n) time
        # Lists to merge halves: O(log k) time

        # Edge case of list being None or of length 0
        if not lists or len(lists) == 0:
            return None
        
        # Take pairs of linked lists until there is a final one
        while len(lists) > 1:
            # Create a list of merged linked lists
            mergedLists = []

            # We increment by 2 at a time to merge pairs of lists
            for i in range(0, len(lists), 2):
                # We must consider whether there are an even or odd 
                # number of lists
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None

                # Merge these two lists and append it to merged lists
                mergedLists.append(self.mergeList(l1,l2))
            # Update lists to be merged lists
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = Node()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1: 
            tail.next=l1

        if l2:
            tail.next = l2
        
        return dummy.next


if __name__ == "__main__":
    sol = Solution()

    #list1 = [1,2,4]
    #list2 = [1,3,5]
    #list3 = [3,6]
    #lists = [[1,2,4], [1,3,5], [3,6]]
    head = None
    head = Node(4, head)
    head = Node(2, head)
    head = Node(1, head)
    list1 = head
    head = None
    head = Node(5, head)
    head = Node(3, head)
    head = Node(1, head) 
    list2 = head
    head = None
    head = Node(6, head)
    head = Node(3, head)
    list3 = head
    lists = [list1, list2, list3]
    print(sol.mergeKLists(lists)) # [1,1,2,3,3,4,5,6]

    #lists = []
    lists = []
    print(sol.mergeKLists(lists)) # []

    #list1 = []
    #lists = list1
    head = Node()
    list1 = head
    lists = [list1]
    print(sol.mergeKLists(lists)) # []
