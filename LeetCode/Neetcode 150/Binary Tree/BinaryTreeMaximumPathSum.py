class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode)->int:
        # Path = sequence of nodes where each pair 
        # of adjacent nodes in the sequence appear 
        # in the edge list (G=(V,E), remember?)
        # AND there are NO repeat nodes in the 
        # sequence
        # 
        # We use DFS but we evaluate the best path 
        # on the left and right subtrees to begin 
        # with
        # 
        # At ANY node, we want the maximum path 
        # passing through it. There are three 
        # components of the path
        # COMPONENT 1: Maximum path connected 
        # through left child
        # COMPONENT 2: Maximum path connected 
        # through right child
        # COMPONENT 3: The node itself
        # 
        # We calculate the maximum path with 
        # these components, and can choose 
        # whether to use the left or right 
        # children if the paths through them 
        # are negative or not (if they are, 
        # use 0)
        # 
        # Now we must return a possible path 
        # that the parent could use!
        # 
        # The node itself must be used as the 
        # connecting child to its parent
        # It must pick AT MOST one path through
        # its children, otherwise its parent 
        # could not use the path#
        # So it picks itself, and then the 
        # maximum path through either its left
        # OR right child!
        # 
        # 
        # O(n) because each node is visited once
        # O(h) space

        # Set a global variable
        # List so that it is easier to modify 
        # in recursive function
        res = [root.val]

        # Return the max path sum without split
        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # If either left or right is negative, 
            # we don't need to add it
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Compute max path sum WITH split
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # To the parent we give the max path sum WITHOUT
            # a split
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]


if __name__ == "__main__":
    sol = Solution()

    # root = [1,2,3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(sol.maxPathSum(root)) # 6

    # root = [-15,10,20,null,null,15,5,-5]
    root = TreeNode(-15)
    root.left = TreeNode(10)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(-5)
    print(sol.maxPathSum(root)) # 40