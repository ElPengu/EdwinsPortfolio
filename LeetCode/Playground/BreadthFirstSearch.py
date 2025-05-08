from typing import List
from collections import deque
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def breadthFirstSearch(self, node: Node)->List[int]:
        # Set up a queue
        q = deque()

        # Load it with the node
        q.append(node)

        res = []

        while q:
            popped = q.popleft()
            res.append(popped.val)
            if popped.left: q.append(popped.left)
            if popped.right: q.append(popped.right)
        return res

if __name__ == "__main__":
    sol = Solution()
    node = Node(6)
    node.left = Node(4)
    node.right = Node(3)
    node.left.left=Node(5)
    node.left.right=Node(10)
    print(sol.breadthFirstSearch(node))