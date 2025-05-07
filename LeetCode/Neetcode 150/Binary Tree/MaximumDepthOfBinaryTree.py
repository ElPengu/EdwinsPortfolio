from collections import deque

class TreeNode:

    def __init__(self, val=0, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Recursive DFS, iterative DFS, BFS
    # These three methods could work

    def maxDepthRecursiveDFS(self, root: TreeNode)->int:
        # At every node, return 1+max(L,R)
        # L->left subtree
        # R->right subtree

        # Take care of the base case
        if not root:
            return 0
        
        # Return 1+maxDepth found
        return 1+max(self.maxDepthRecursiveDFS(root.left), self.maxDepthRecursiveDFS(root.right))
    
    def maxDepthBFS(self, root: TreeNode)->int:
        # We traverse level by level
        # So we go to level 1, level 2, ..., level N
        # It is an intuitive way of counting!
        # We set a queue (FIFO)
        # For each node in our queue, we pop it 
        # and add its children to our queue. This
        # brings us to the next level
        # We initialise the queue with our root
        
        # Base case
        if not root:
            return 0
        
        # Set our level to 0 and add root to the queue
        level = 0
        q = deque([root])
        while q:

            # We remove all elements in the current 'snapshot'
            # of the queue
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # Since our queue is non-empty, increment level
            level+=1
        return level
    
    def maxDepthIterativeDFS(self, root: TreeNode)->int:
        # We will implement PRE-ORDER DFS
        # Process the node, then we process the left node, then 
        # the right node
        # We add each node to the stack, and keep the depth 
        # of it (just 1+parent)
        # We use a stack. 
        # Add the root to the stack. Pop it and add its children.
        # Repeat the popping and population for the top of the stack
        # Keep track of the max depth seen in the stack

        if not root:
            return 0
        
        # We at least have a node
        res = 1

        # Set a stack with the root and depth 1
        stack = [[root, 1]]

        # Now we loop over the stack
        while stack:
            node, depth = stack.pop()

            # If the node is non-Null, we update our result
            # Else, we would just skip it!
            if node:
                res = max(res, depth)
                # We possibly add null nodes.
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])

        # Just return the result
        return res


if __name__ == "__main__":
    sol = Solution()

    #root = [1,2,3,null,null,4]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    print(sol.maxDepth(root)) # 3

    #root = []
    root = None
    print(sol.maxDepth(root)) # 0