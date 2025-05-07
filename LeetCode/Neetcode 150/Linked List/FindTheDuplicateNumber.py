from typing import List

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def findDuplicate(self, nums: List[int])->int:
        # We want to use O(1) extra space AND leave 
        # nums unmodified!
        # This is a linked list cycle
        # This uses Floyd's algorithm
        # Every number appears from [1,n], there are
        # n+1 numbers
        #
        # Consider nums[i] as a next pointer for index i
        # Due to the range of numbers, a cycle WILL 
        # appear
        # There will be a part OUTSIDE of the cycle
        # that points to the start of the cycle
        # and a node just BEFORE the cycle
        # 
        # Read the problem, index i can NEVER be in the 
        # cycle because forall i: nums[i] in {1,...,n} 
        # 
        # We use Floyd's algorithm to find the start of 
        # the cycle
        # 
        # Floyd's algorithm: Set a slow and a fast pointer
        # Slow pointer: jumps one node at a time
        # Fast pointer: jumps two nodes at a time
        # Find the node that the slow and fast pointer 
        # intersect at
        # Set a second slow pointer
        # Shift the second slow pointer together with the 
        # slow and fast pointer (now moving one at a time)
        # Until they intersect. This WILL be the start 
        # of the cycle!
        # 
        # WHY Floyd's algorithm works
        # The first intersection between slow and fast pointer
        # is as far from the start of the cycle as the starting
        # point distance from the cycle
        # Set p = distance from original point to start of cycle
        # Set x = distance from first intersection to start of 
        # cycle
        # Set c = length of cycle
        # c-x = distance from start of cycle to first intersection
        # 
        # 2xslow iterations = fast iterations
        # fast iterations = p + c-x + c (fast pointer does one full 
        # loop before meeting the slow pointer)
        # 2xslow iterations = 2(p+c-x) (fast meets slow before slow 
        # completes loop)
        # 2xslow iterations = fast iterations -> 2p+2c-2x=p+2c-x
        # -> (2p-p)+(2c-2c)=(-x+2x)
        # -> p+0=x
        # p=x
        # distance from original point to start of cycle = distance 
        # from first intersection to start of cycle 
        # This works for where p is a distance of 1. Where p is a 
        # distance of M it still works, it would mean that the fast
        # pointer does N cycles before the slow pointer does 1 loop
        # (could be M, unsure though) 
        # 
        # Simple derivation to remember
        # 
        # Note that the "NEXT" of the pointer is nums[i]
        
        # We set a slow and a start pointer
        slow, fast = 0, 0

        # We will iterate until the slow and fast meet
        # again
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                # Now slow and fast intersect
                break

        # Phase 2
        # Set another slow pointer
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                # Floyd's algo tells us that we are at the start 
                # of the cycle. 
  
                return slow


if __name__ == "__main__":
    sol = Solution()

    nums = [1,2,3,2,2]
    print(sol.findDuplicate(nums)) # 2

    nums = [1,2,3,4,4]
    print(sol.findDuplicate(nums)) # 4

    nums = [1,2,2]
    print(sol.findDuplicate(nums)) # 1