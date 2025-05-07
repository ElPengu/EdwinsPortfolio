from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def rightSideView(self, root: TreeNode) -> List[int]:

        # A right side tree is whatever nodes are 
        # NOT blocked from the right each level
        #
        # So you cannot just take the nodes on the 
        # right. Consider a tree with a subtree
        # on the left of depth 10 and a subtree
        # on the right of depth 3.
        # The final 7 levels will have nodes on
        # the left subtree which can be seen!
        # 
        # Another framing of the problem
        # At each level we just want the right-most
        # node
        # 
        # We use a BFS solution
        # 
        # At each level we take the last value in 
        # the queue and add it to res
        
        # Set our res
        res = []
        # We set our queue initialised with root
        q = deque()
        q.append(root)

        # We search each level of tree
        while q:
            # We initialise rightSide
            rightSide = None
            # We iterate over the current 'snapshot'
            # of the queue
            qLen = len(q)

            # Loop over the current "snapshot"
            for i in range(qLen):
                # Pop a node
                node = q.popleft()

                # We check if node is not null
                if node:
                    # Update rightSide
                    rightSide = node

                    # Now rightSide will have latest
                    # node

                    # We append the left and right
                    # nodes
                    # You must add the left and then 
                    # the right node!
                    q.append(node.left)
                    q.append(node.right)

            # Add value of rightSide to res IF it is
            # not null
            if rightSide:
                res.append(rightSide.val)
            
        # Return our result
        return res

            

    


if __name__ == "__main__":
    sol = Solution()

    # root = [1,2,3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(sol.rightSideView(root)) # [1,3]

    # root = [1,2,3,4,5,6,7]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(sol.rightSideView(root)) # [1,3,7]