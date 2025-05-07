class Node:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverseKGroup(self, head: Node, k: int)->Node:
        # We want to look at each group of size k
        # Each group must be reversed
        # 
        # We use a dummy node to point to the head, this 
        # makes things easy
        # 
        # For the first group, we go over the first group, 
        # and we set the first k nodes to point to the previous 
        # node. 
        # At this point we explicitly set the dummy to point to
        # the kth node of this first group
        # This breaks the list. 
        # We start iterating over the next k nodes, reversing
        # the group. We set the kth node of the first group 
        # to point to the kth node of the second group.
        # This breaks the list
        # We ignore the dummy, but otherwise repeat

        # We want a dummy node pointing to the head of the linked list
        dummy = Node(0, head)

        # We set a previous group node right before the group, so 
        # that we can easily reverse groups
        groupPrev = dummy

        while True:
            # We get the kth node
            kth = self.Kth(groupPrev, k)

            # If there is no kth element, then that means that the group 
            # is smaller than k. By definition of the problem, we neednt
            # reverse the list, so we can return!
            if not kth:
                break

            # We will keep track of the node right after our group.
            # This will be our stopping condition
            groupNext = kth.next

            # We reverse the group. 
            # curr is at the first node in our group
            # To prevent splitting the group, we set the prev to be 
            # the next of k. Why?!
            # Think about it! We want to keep this sub list 
            # chained to the NEXT sub list, so the first node
            # will need to point to the node right after this sublist!!
            prev, curr = kth.next, groupPrev.next 

            # We start by pointing the start of the group to the start 
            # of the next group. From there, each node after the start 
            # of the group points to the previous.
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # What we essentially do now
            #3->2->1->4->5->6->7->8->9
            #3->2->1->4<-5<-6, (4->)7->8->9
            #3->2->1->6->5->4->7->8->9

            # groupPrev currently points to the original start of the
            # group. We save this
            tmp = groupPrev.next
            # We put the kth node at the beginning of this list
            groupPrev.next = kth
            # groupPrev must be at the preceding node of the next 
            # group. We already saved the original start of the 
            # group, which will now be the node before the start 
            # of the next group. We set groupPrev accordingly!
            groupPrev = tmp

                
            pass

    # Helper function
    def getKth(self, curr, k):

        # Shift k times and get kth node
        while curr and k > 0:
            curr = curr.next
            k -= 1

        return curr

        pass


if __name__ == "__main__":
    sol = Solution()
    # head = [1,2,3,4,5]
    # k = 3
    head = None
    head = Node(5, head)
    head = Node(4, head)
    head = Node(3, head)
    head = Node(2, head)
    head = Node(1, head)
    k = 3
    print(sol.reverseKGroup(head, 3))