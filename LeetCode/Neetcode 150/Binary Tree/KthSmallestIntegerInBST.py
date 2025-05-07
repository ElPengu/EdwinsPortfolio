class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int)-> int:
        # If we traverse this BST in-order, then 
        # we will have the elements of the BST in 
        # increasing order!

        # n until we reach k
        n = 0
        # stack because we are doing this iteratively
        stack = []
        cur = root

        # Traverse the tree while the cur and stack exists
        while cur and stack:
            # If we have a left subtree then we 
            # explore it
            while cur:
                # We add cur to the stack
                cur = cur.left

                # Go to the left immediately
                cur = cur.left

            # Now we have exhausted the left subtree
            
            # Pop the node that we have seen BEFORE 
            # checking with its left subtree (whether
            # it existed or not!)
            cur = stack.pop()

            # Update n
            n += 1
            if n == k:
                # This always executes

                # No need to visit extra nodes
                return cur.val
            
            # Now we can go to its right subtree!
            cur = cur.right

    
    def kthSmallestMYSOL(self, root: TreeNode, k: int)-> int:

        # The fact that we are dealing with a BST is probably important
        # 
        # Naively I'd load all elements into an array using DFS or BFS,
        # then I'd sort it
        #
        # I think that pre-order would not work. However, the order 
        # where you go left subtree, root, right subtree might work
        # 
        # The absolute smallest value would be the first value 
        # evaluated in this fashion. 
        # The 2nd smallest would be the 2nd value evaluated
        # The 3rd smallest would be the 3rd value evaluated
        # ...
        # The nth smallest would be the nth value evaluated
        # 
        # I think I could implement this now, actually!
        # 
        # Use recursive DFS, but immediately call it on the left 
        # subtree
        # Once there is no left subtree then you increment a global
        # counter
        # Once the global counter is equal to k, you set res to 
        # the value of THAT node


        def dfs(node):

            # Immediately call this on the left node IF it exists
            if node.left:
                dfs(node.left)

            # If counter is equal to k, set res accordingly
            if self.counter == k:
                self.res = node.val
            
            # Update counter
            self.counter += 1

            # Call this on the right node IF it exists
            if node.right:
                dfs(node.right)


        
        # Global counter initialised to 1
        self.counter = 1
        # Res value initialised to None
        self.res = None

        dfs(root)

        return self.res



if __name__ == "__main__":
    sol = Solution()
    
    # root = [2,1,3], k=1
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    k = 1
    print(sol.kthSmallest(root, k)) # 1

    # root = [4,3,5,2,null], k=4
    root = TreeNode(4)
    root.left = TreeNode(3)
    root.right = TreeNode(5)
    root.left.left = TreeNode(2)
    k = 4
    print(sol.kthSmallest(root, k)) # 5
