from typing import List
from collections import deque

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # This is basically BFS!
        # We use a queue to search the tree
        # We use this LIFO approach from the ROOT
        # Every time we search a level we add it as a 
        # list to the list of lists

        # Holds our results
        res = []

        # Set up a queue
        q = deque()
        q.append(root)

        while q:
            # Until q is empty

            # We search each level by searching the 
            # "snapshot" of the queue at this point
            qLen = len(q)

            # Set a list
            level = []

            for i in range(qLen):
                # We pop a node
                node = q.popleft()

                # We only add the value and its children
                # if the node is valid
                if node:
                    # Append to this level
                    level.append(node.val)
                    # Append the children to the queue
                    q.append(node.left)
                    q.append(node.right)

            # Make sure the level is non-empty in case
            # the queue is empty
            if level:
                # We add the level to the result
                res.append(level)
        # Now we can return res
        return res


    def levelOrderMYSOL(self, root: TreeNode) -> List[List[int]]:

        # This is basically just BFS
        # We create a queue called nodes
        # We put the root in nodes
        # We repeatedly pop a node from nodes and add its children
        # to the stack
        # For each popped node we add its value to a list called vals

        # Base case: return empty list if the tree is empty
        if not root:
            return [[]]

        # Set up nodes queue
        nodes = deque()

        # Add root to nodes
        nodes.append(root)

        # Set up a vals list
        vals = []

        # Search the nodes queue until it is empty
        while nodes:
            # Create a sublist of vals
            sublistOfVals = []

            # We only search the current 'snapshot' of the queue
            snapshotLen = len(nodes)

            for i in range(snapshotLen):
                # We pop a node from our queue FIFO
                poppedNode = nodes.popleft()

                # We add its value to our sublist
                sublistOfVals.append(poppedNode.val)

                # We add its existing children to the queue!
                if poppedNode.left:
                    nodes.append(poppedNode.left)

                if poppedNode.right:
                    nodes.append(poppedNode.right)

            # We add our sublist to nodes
            vals.append(sublistOfVals)

        # We return our vals list
        return vals


if __name__ == "__main__":

    sol = Solution()

    # root = [1,2,3,4,5,6,7]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(sol.levelOrder(root)) # [[1],[2,3],[4,5,6,7]]

    # root = [1]
    root = TreeNode(1)
    print(sol.levelOrder(root)) # [[1]]

    # root = []
    root = None
    print(sol.levelOrder(root)) # []
