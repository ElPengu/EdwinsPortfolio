class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # This is a surprisingly easy problem!
        # 
        # Binary search tree: left child is smaller, right child is bigger
        # than root
        # 
        # A common ancestor is the lowest node such that p and q are 
        # either descendants of it, OR at least one of them is equal to it
        # 
        # Relying on the definition of a binary search tree, we just want 
        # to find a SPLIT where the value of p is smaller than a node 
        # X's AND the value of q is larger than node X's value
        # 
        # We also note that since a node can be an ancestor of itself, 
        # another admissible case is where node X itself has the value 
        # of p and one of its subtrees has the value of q, or vice 
        # versa
        # 
        # We don't even need DFS! We can just check every level of the 
        # tree
        # 
        # Also note that p and q are nodes from the tree, and that 
        # all nodes in the tree are unique
        #
        # O(log n) time because we only visit 1 node for every 
        # level of the tree, not every tree
        # O(1) space

        # Start at root
        cur = root

        while cur:
            # Execute until we get result

            if p.val > cur.val and q.val > cur.val:
                # Since both are bigger, we need to go down the right 
                # subtree
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                # Since both are smaller, we need to go down the right 
                # subtree
                cur = cur.left
            else:
                # We have found our result!
                return cur
            
        # No return because we are guaranteed to find
        # a result



if __name__ == "__main__":
    sol = Solution()
    
    # root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8
    root = TreeNode(5)
    p = root.left = TreeNode(3)
    q = root.right = TreeNode(8)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.left.right = TreeNode(2)
    print(sol.lowestCommonAncestor(root, p, q)) # 5

    # root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4
    root = TreeNode(5)
    p = root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(1)
    q = root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.left.right = TreeNode(2)
    print(sol.lowestCommonAncestor(root, p, q)) # 3