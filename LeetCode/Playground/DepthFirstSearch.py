from typing import List
from collections import deque
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def depthFirstSearchRecursive(self, node: Node)->List[int]:

        res = []

        def dfs(node):
            if not node:
                return
            res.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(node)
        return res    

    def depthFirstSearchIterative(self, node: Node)->List[int]:
        # Set up a queue
        q = deque()

        # Load it with the node
        q.append(node)

        res = []

        while q:
            popped = q.pop()
            res.append(popped.val)
            if popped.left: q.append(popped.right)
            if popped.right: q.append(popped.left)
        return res

if __name__ == "__main__":
    sol = Solution()
    node = Node(6)
    node.left = Node(4)
    node.right = Node(3)
    node.left.left=Node(5)
    node.left.right=Node(10)
    print(sol.depthFirstSearchRecursive(node))
    print(sol.depthFirstSearchIterative(node))