import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # A Binary Search Tree has every node in 
        # its left subtree SMALLER in value than 
        # it, and vice versa for the right subtree
        # NOT just the children!
        # 
        # We can set RANGES in each DFS call!
        # 
        # When we check the root, we care if it is
        # -math.inf < root.val < math.inf
        # Then for the left child of root, we care
        # if it is smaller
        # I.E. -math.inf < root.left.val < root.right
        # Conversely, for right child
        # root.right.val < root.val < math.inf
        # 
        # More generally...
        # When we enter the left subtree, we update 
        # the UPPER BOUNDARY
        # When we enter the right subtree, we update
        # the LOWER BOUNDARY

        # Set a recursive DFS function with left and
        # right boundaries
        def valid(node, left, right):

            # An empty binary search tree is valid
            if not node:
                return True
            
            # Check if node value lies in boundaries
            if not(node.val < right and node.val > left):
                return False
            
            # Check if left and right nodes are valid

            # For left node, we update the RIGHT boundary
            return (valid(node.left, left, node.val) 
                    and valid(node.right, node.val, 
                              right))

        # Call valid on root with maximum boundaries
        return valid(root, -math.inf, math.inf)
    
    


if __name__ == "__main__":
    sol = Solution()
    # root = [2,1,3]
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(sol.isValidBST(root)) # true

    # root = [1,2,3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(sol.isValidBST(root)) # false
    