class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        # O(n) time
        # O(h) space
        # 
        # We will use pre-order
        # PRE-ORDER: Evaluate the root, then the 
        # left then the right subtrees
        # 
        # Naturally the root node is a good node
        # 
        # We use DFS. We pass the greatest value
        # seen so far, so we need a separate 
        # DFS function
        # 
        # Was the MOST popular question from 
        # Microsoft in 2021

        # Setting up dfs
        def dfs(node, maxVal):
            # If we have a null node then we return
            # 0
            if not node:
                return 0
            
            # We set res flag if this is at least 
            # biggest value seen so far
            res = 1 if node.val >= maxVal else 0
            # Update maxVal
            maxVal = max(maxVal, node.val)
            # We add the returns from the left and 
            # right subtrees to res
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        
        # We return the call to this function
        return dfs(root, root.val) 


    def goodNodesMYSOL(self, root: TreeNode) -> int:

        # This could be completed with a dfs approach
        # Set a global res to count the number of good nodes
        # Now what do we want the dfs function to do?
        # 
        # Really, we are asking the following question: have we
        # NOT seen a bigger value in a node so far?
        # 
        # We can pass the value into the dfs function (starting) 
        # with the value of the root.
        # 
        # If we enter a function and the value of the node is the 
        # equal to or greater that the previously biggest seen
        # then we increment res
        # 
        # We always pass max(biggestValSeen, node.val) as the argument

        # If root is null, return 0
        if not root:
            return 0
        
        # Set up global result variable
        # Starts at 0, we increment for every node with biggest value
        self.res = 0

        # Recursive DFS function
        def dfs(node, biggestValSeen):
            
            # If value of node is equal to or greater than seen on 
            # path then update global result variable
            if node.val >= biggestValSeen:
                self.res += 1

            # Now we update biggestValSeen
            biggestValSeen = max(biggestValSeen, node.val)

            # Finally we check the children (if they exist!)
            if node.left:
                
                dfs(node.left, biggestValSeen)
            if node.right:
                dfs(node.right, biggestValSeen)


        # We pass the root node into the dfs function
        dfs(root, root.val) 

        
        # We return res
        return self.res



if __name__ == "__main__":
    sol = Solution()
    # root = [2,1,1,3,null,1,5]
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)
    print(sol.goodNodes(root)) # 3

    # root = [1,2,-1,3,4]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(-1)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    print(sol.goodNodes(root)) # 4