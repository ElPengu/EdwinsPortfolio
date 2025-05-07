class TreeNode:
    def __init__(self, val=0, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode)->int:
        # Diameter: length of the longest path between any
        # two nodes
        # 
        # This is NOT like calculating the height, this is diameter
        #
        # At a basic level, the diameter of a subtree of height 1
        # will have a diameter which is equal to the height on its left
        # and right
        # 
        # We extend this idea by having a global result variable
        # We run DFS to find the height of the left and right subtree
        # at a time, and we update res = max(res, left+right)
        # Each node calculates its height = 1+max(left,right)
        # 
        # This way, the node through which the biggest diameter passes
        # through will dominate the res variable!
        # 
        # height = 1+max(left,right)
        # diameter = left+right
        # O(n) time
        # O(h) space 

        # Let us create a member variable for the result
        self.res = 0

        # Returns height
        def dfs(curr):
            if not curr:
                # At null node
                return 0
            
            # Get height of the left and right subtree
            left = dfs(curr.left)
            right = dfs(curr.right)

            # We update res
            self.res = max(self.res, left + right)

            # Now we return the height up to curr node
            return 1 + max(left, right)
        
        # We call dfs from root
        dfs(root)
        return self.res




if __name__ == "__main__":
    sol = Solution()
    # root = [1,null,2,3,4,5]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.left.left = TreeNode(5)
    root.right.right = TreeNode(4)
    print(sol.diameterOfBinaryTree(root)) # 3

    # root = [1,2,3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(sol.diameterOfBinaryTree(root)) # 2