from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):

        self.val=val
        self.left=left
        self.right=right

class Solution:

    def isSameTree(self, p: TreeNode, q: TreeNode)->bool:
        # Intuitively: Start from the root and check if they 
        # are the same
        # Now we have two subtrees. The left and right subtree
        # We must check if the corresponding subtrees are equivalent
        # 
        # O(P+Q) time complexity
        # 
        # We recursively check
        
        if not p and not q:
            # Both trees are empty
            return True 
        
        if not p or not q or p.val != q.val:
            # Exactly one tree is not empty, since the previous statement
            # was not executed

            # ORRRR
            # The values at the root are not the same

            return False
        
        # Now we call this on the left and right subtrees
        # If any returns false then the entire tree is not equal,
        # so we use AND
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))
        


if __name__ == "__main__":
    sol = Solution()

    # p = [1,2,3], q=[1,2,3]
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    print(sol.isSameTree(p,q)) # True

    # p = [4,7], q = [4,null,7]
    p = TreeNode(4)
    p.left = TreeNode(7)
    q = TreeNode(4)
    q.right = TreeNode(7)
    print(sol.isSameTree(p,q)) # False

    # p = [1,2,3], q = [1,3,2]
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(3)
    q.right = TreeNode(2)
    print(sol.isSameTree(p,q)) # False
