import math

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left = left
        self.right = right


class Solution:

    def balancedBinaryTree(self, root:TreeNode)->bool:
        # Calculate the maximum height of the left and #
        # right subtree of every node. Check if difference
        # is greater than 1
        # A recursive DFS will take O(n) operation each 
        # time we ask if a node is balanced. Since we 
        # do this O(n) times we take O(n2)
        # 
        # We improve this by calculating the heights in 
        # a bottom-up approach
        # 
        # We will return [is subtree balanced, height of 
        # sub tree]
        # 
        # 

        # Recursive call
        def dfs(root):
            if not root:
                # Balanced with height of 0
                return [True, 0]
            
            # Now we call DFS on the left and right subtrees 
            # BEFORE calculating
            left = dfs(root.left)
            right = dfs(root.right)

            # We check if this node is balanced by first checking if 
            # either left or right is not balanced, and then checking
            # if the difference between left and right heights exceeds
            # 1
            balanced = (left[0] and right[0] and abs(left[1]-right[1]) <=1)

            return [balanced, 1+max(left[1], right[1])]


        return dfs(root)[0]

    def balancedBinaryTreeMYSOL(self, root:TreeNode)->bool:
        # This is effectively asking whether the maximum height 
        # of the left subtree and right subtree of any node 
        # has a difference in excess of 1

        # Set a global variable for balanced
        # We assume the tree is balanced
        self.isBalanced = True

        # Trivial case
        if not root:
            return True
        
        # We used recursive DFS
        def dfsMaxHeight(curr):

            # If curr is none then return 0
            if not curr:
                return 0
            
            # Call dfs on left and right subtrees
            maxLeft = dfsMaxHeight(curr.left)
            maxRight = dfsMaxHeight(curr.right)

            # Calculate the maximum POSITIVE difference between the 
            # left and right subtrees
            maxDiff = abs(maxLeft - maxRight)
            # Check if the maxDiff > 1
            if maxDiff > 1:
                self.isBalanced = False
            
            # Return 1+ maximum height of the left and right subtree
            return 1+max(maxLeft,maxRight)
        
        # Call dfs on root
        dfsMaxHeight(root)

        # Return isBalanced
        return self.isBalanced


if __name__ == "__main__":

    sol = Solution()
    # root = [1,2,3,null,null,4]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    print(sol.balancedBinaryTree(root)) # true

    # root = [1,2,3,null,null,4,null,5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.left.left = TreeNode(5)
    print(sol.balancedBinaryTree(root)) # false

    # root = []
    root = None
    print(sol.balancedBinaryTree(root)) # true