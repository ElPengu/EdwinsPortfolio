from typing import List

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # We will use pre-order traversal with DFS 
    # INSTEAD of BFS traversal
    # Why? Because it requires a bit less code
    # 
    # PREORDER: Root, left subtree, right subtree
    # 
    # We will use , as a delimiter
    # We will use N for an empty subtree
    # 
    # We will build the tree using pre-order 
    # DFS. So build the root, then the entire
    # left subtree, then the entire right subtree,
    # recursively
    # 
    # We will deserialise by recursively creating
    # the left subtree until we see a NULL.
    # Then we will create the right subtree until
    # we see a NULL
    # The base case is where both subtrees have 
    # NULLs. 
    # We pop back up to the parent node at the base 
    # case


    def serialize(self, root: TreeNode)-> str:
        # Set an empty array
        res = []

        # Define a pre-order DFS traversal
        def dfs(node):
            if not node:
                # We have a null node
                res.append("N")
                return
            
            # Append value
            res.append(str(node.val))

            dfs(node.left)
            dfs(node.right)
        dfs(root)
        # Join everything in res by ,
        return ",".join(res)
        
    def deserialize(self, data: str)-> TreeNode:
        # Create an array of the data
        vals = data.split(",")

        # Set global pointer
        self.i= 0

        def dfs():
            # If we see N, just return None
            if vals[self.i] == "N":
                # Increment i
                self.i+=1
                return None
            
            # We must set a node with the value 
            # at the pointer
            node = TreeNode(int(vals[self.i]))

            # Increment i
            self.i+=1

            # Now we create the left and right 
            # subtrees
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()


if __name__ == "__main__":
    sol = Solution()

    # root = [1,2,3,null,null,4,5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print(sol.serialize(root)) # 1,2,N,N,3,4,N,N,5,N,N
    print(sol.deserialize(sol.serialize(root))) # Binary tree [1,2,3,null,null,4,5]

    # root = []
    root = None
    print(sol.serialize(root)) # N
    print(sol.deserialize(sol.serialize(root))) # Binary tree []