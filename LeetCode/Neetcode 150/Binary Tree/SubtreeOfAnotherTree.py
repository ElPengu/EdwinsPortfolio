class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode)->bool:
        # Let S = tree, T = subtree
        # We use a helper function to check whether T is a subtree of 
        # S
        # We also have another helper function called isSubTree
        # 
        # Now we begin at the root and check if s and t are the same
        # subtree (using our helper function)
        # If they are not, then we say okay, is t a subtree of 
        # the left or right subtree of s?
        # So we call the subtree function again! Why?
        # In the subtree function, we check if they are the same 
        # tree! 
        # 
        # It is difficult to code up initially, but this is the 
        # entire idea of the solution!
        

        if not t:
            # If T is null then trivially it is a subtree of S
            return True
        if not s and t:
            # It is impossible for T to be a subtree of S
            return False
        
        # We immediately check if the subtree from this node is the 
        # same as t
        if self.sameTree(s, t):
            # If both trees are the same, then we can return true!
            return True
        
        # Now this is tricky, but we now need to call isSubtree, NOT 
        # sameTree, on the left and right subtrees
        # If t is a subtree of the left or right subtree, NOT the same, 
        # then we return true
        return (self.isSubtree(s.left, t) or self.isSubtree(s.right, t))

    # Checks if two trees are the same
    def sameTree(self, s, t):
        if not s and not t:
            # Both trees are null, and the same
            return True
        
        if s and t and s.val == t.val:
            # We know that the two nodes are the same
            
            # We must compare the left and right subtrees of s and t
            # We return true if both are true!
            return (self.sameTree(s.left, t.left) and
            self.sameTree(s.right, t.right))


        # At this point, at least one tree is empty and one tree 
        # is non-empty. So the trees cannot be the same!
        return False


if __name__ == "__main__":
    sol = Solution()

    # root = [1,2,3,4,5], subRoot = [2,4,5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    subRoot = TreeNode(2)
    subRoot.left = TreeNode(4)
    subRoot.right = TreeNode(5)
    print(sol.isSubtree(root, subRoot)) # True
    
    # root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    subRoot = TreeNode(2)
    subRoot.left = TreeNode(4)
    subRoot.right = TreeNode(5)
    print(sol.isSubtree(root, subRoot)) # False